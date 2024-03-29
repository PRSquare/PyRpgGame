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
import shop
import templocitf as tui
import tavern
import notifyerlistener
import quest

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

	def _input_processor(self, inputed):
		
		if inputed.equals(self.inputVars["change_name"]):
			self._enter_the_name()
			return
		if inputed.equals(self.inputVars["change_class"]):
			self._choose_class()

		if inputed.equals(self.inputVars["quit"]):
			self.gameClassHandler.exit()
			return

		if inputed.equals(self.inputVars["start"]):
			pl = PlayerClassNotif(self.gameClassHandler.targetKilledNotifyer, 
				self.gameClassHandler.itemPickedUpNotifyer, 
				self.gameClassHandler.itemRemovedNotifyer
			)
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

class PlayerClassNotif(player.Player):
	onKillNotifyer = None
	onItemAddedNotifyer = None
	onItemRemovedNotifyer = None
	def __init__(self, onKillNotifyer, onItemAddedNotifyer, onItemRemovedNotifyer, name="Player"):
		super().__init__(name)
		self.onKillNotifyer = onKillNotifyer
		self.onItemAddedNotifyer = onItemAddedNotifyer
		self.onItemRemovedNotifyer = onItemRemovedNotifyer

	def add_item(self, item):
		if super().add_item(item):
			self.onItemAddedNotifyer.notify(item)
			return True
		return False
	def remove_item(self, item):
		if super().remove_item(item):
			self.onItemRemovedNotifyer.notify(item)
			return True
		return False

	def kill(self):
		self.onKillNotifyer.notify(self)
		super().kill()

class fake_game():
	doExit = False

	player = None
	shop = None
	tavern = None
	interface = None
	currentLocation = None

	targetKilledNotifyer = None
	itemPickedUpNotifyer = None
	itemRemovedNotifyer = None

	def __init__(self):

		self.targetKilledNotifyer = notifyerlistener.Notifyer()
		self.itemRemovedNotifyer = notifyerlistener.Notifyer()
		self.itemPickedUpNotifyer = notifyerlistener.Notifyer()

		loader.load_all_items(loader.get_data("data/tecnical/items.json"))
		loader.load_all_monsters(loader.get_data("data/tecnical/monsters.json"))
		loader.load_all_locations(loader.get_data("data/tecnical/locations.json"))

		create_char = CharacterCreationInterface(self)
		create_char.show()
		while self.player == None:
			create_char.process_commands()

		self.shop = shop.Shop()
		self.shop.available_items = list(globaldata.ITEMS.data.values())
		self.shop.gen_items()

		self.tavern = tavern.Tavern()

		self.interface = tui.TavernInterface(self, self.tavern)

		self.currentLocation = globaldata.LOCATIONS.get("forest")

	def go_to_shop(self):
		self.interface = tui.ShopInterface(self, self.shop)
	def go_to_journey(self):
		return
	def go_to_tavern(self):
		self.interface = tui.TavernInterface(self, self.tavern)

	def temp_showinv(self, container = None):
		if not container:
			container = self.player.inventory
		self.interface = containerinterface.InventoryInterface(self, self.player)
	def temp_showstat(self, who = None):
		if not who:
			who = self.player
		self.interface = interface.StatusInterface(self, who)

	def atack(self, atacker, atacked):
		dm = damage.DamageCalculator(atacker, atacked)
		atacked.health = atacked.health - dm.finaldamage
		return atacked.isDead

	# def combat(self, groupA, groupB):
	# 	pass		

	def exit(self):
		self.doExit = True

	def update(self):
		self.player.update_effects()
		self.interface.show()
		self.interface.process_commands()
		if not self.interface.isOpen:
			self.exit()

test = fake_game()
while not test.doExit:
	test.update()

# test.start()


# print("'Ok. Lets do some magic! \033[2B\033[106;95m\033[3m\033[52m Some magic happening!!! \033[0m\033[2A Are you impressed?")