import gameplay
import containerinterface
import interface
import combatinterface
import player
import location
import damage
import globaldata
import loader
import temp as t

class CharacterCreationInterface(interface.Interface):
	def __init__(self, gameClassHandler):
		super().__init__(gameClassHandler)
		self.name = "Player"
		self.plClass = 1
		self.inputVars["change_name"] = interface.InputVariant("n", "change name")
		self.inputVars["change_class"] = interface.InputVariant("c", "change class")
		self.inputVars["quit"] = interface.InputVariant("q", "quit")
		self.inputVars["start"] = interface.InputVariant("s", "start with this character")

	def _enter_the_name(self):
		print("Enter the name\n> ", end = "")
		self.name = input()

	def _choose_class(self):
		c = 0

		# do
		print("chose the class:\n1)Barbarian\n2)Warior\n3)Mage\n> ", end = "")
		try:
			c = int(input())
		except Exception:
			print("Please, enter a number")
		self.plClass = c
		# while
		while not c in [1, 2, 3]:
			print("chose the class:\n1)Barbarian\n2)Warior\n3)Mage\n> ", end = "")
			try:
				c = int(input())
			except Exception:
				print("Please, enter a number")
			self.plClass = c
		# ---

	def show(self):
		self._enter_the_name()
		self._choose_class()
		# self.show_input_vars()

	def get_equipemet_by_class(self, cl):
		eq = []
		if cl == 1: # Barbarian
			eq.append(globaldata.ITEMS.get("axe").build())
			eq.append(globaldata.ITEMS.get("leather_boots").build())
			eq.append(globaldata.ITEMS.get("heal_potion").build())
		if cl == 2: # Warior
			eq.append(globaldata.ITEMS.get("sword").build())
			eq.append(globaldata.ITEMS.get("armor_plate").build())
		if cl == 3: # Mage
			eq.append(globaldata.ITEMS.get("magic_ring").build())
			eq.append(globaldata.ITEMS.get("magic_crown").build())
			eq.append(globaldata.ITEMS.get("water_wand").build())
		return eq

	def process_commands(self):
		self.show_input_vars()
		inputed = self.get_input()

		if inputed.equals(self.inputVars["change_name"]):
			self._enter_the_name()
			return
		if inputed.equals(self.inputVars["change_class"]):
			self._choose_class()

		if inputed.equals(self.inputVars["quit"]):
			self.gameClassHandler.exit()
			return

		if inputed.equals(self.inputVars["start"]):
			pl = player.Player()
			pl.name = self.name
			for e in self.get_equipemet_by_class(self.plClass):
				pl.inventory.add_item(e)
			self.gameClassHandler.player = pl
			return


			

class Game():
	def __init__(self):
		self.player = None

STATUS_EXIT = 0
STATUS_CONTINUE = 1

class fake_game():
	def __init__(self):
		self.doExit = False

		loader.load_all_items(loader.get_data("data/tecnical/items.json"))
		loader.load_all_monsters(loader.get_data("data/tecnical/monsters.json"))
		loader.load_all_locations(loader.get_data("data/tecnical/locations.json"))
		self.player = None
		create_char = CharacterCreationInterface(self)
		create_char.show()
		while self.player == None:
			create_char.process_commands()

		self.interface = interface.StatusInterface(self, self.player)

		self.currentLocation = globaldata.LOCATIONS.get("forest")

		# sword_for_player = t.create_sword()
		# self.player.inventory.add_item(sword_for_player)
		# self.player.equip(sword_for_player)
		# self.player.equip(t.create_armor_plate())
		# # self.player.equip(t.create_ring())
		# # self.player.equip(t.create_armor_plate())
		# # self.player.add_effect(t.EPoison(self.player))
		# # self.player.add_effect(t.EIncreaceDamage(self.player))

		# self.player.inventory.add_item(t.create_poison())
		# self.player.inventory.add_item(t.create_quest_item())

		# self.enemiesList = []
		# for i in range(0, 2):
		# 	g = t.create_goblin()
		# 	g.equip(t.create_sword())
		# 	self.enemiesList.append(g)

		# self.interface = combatinterface.CombatInterface(self, self.player, self.enemiesList)


	def temp_showinv(self, container = None):
		if not container:
			container = self.player.inventory
		self.interface = containerinterface.PlayerInventoryInterface(self, container)
	def temp_showstat(self, who = None):
		if not who:
			who = self.player
		self.interface = interface.StatusInterface(self, who)

	def atack(self, atacker, atacked):
		dm = damage.DamageCalculator(atacker, atacked)
		atacked.health = atacked.health - dm.finaldamage
		return atacked.isDead

	def exit(self):
		self.doExit = True

	def update(self):
		self.player.update_effects()
		# for e in self.enemiesList:
		# 	e.update_effects()
		self.interface.update()
		self.interface.show()
		self.interface.process_commands()

test = fake_game()
while not test.doExit:
	test.update()

# test.start()


# print("'Ok. Lets do some magic! \033[2B\033[106;95m\033[3m\033[52m Some magic happening!!! \033[0m\033[2A Are you impressed?")