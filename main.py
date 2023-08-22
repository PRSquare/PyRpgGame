import gameplay
import containerinterface
import interface
import combatinterface
import player
import location
import damage
import temp as t

class Game():
	def __init__(self):
		self.player = None

STATUS_EXIT = 0
STATUS_CONTINUE = 1

class fake_game():
	def __init__(self):
		self.doExit = False
		self.player = t.create_player()
		self.interface = interface.StatusInterface(self, self.player)

		sword_for_player = t.create_sword()
		self.player.inventory.add_item(sword_for_player)
		self.player.equip(sword_for_player)
		self.player.equip(t.create_armor_plate())
		# self.player.equip(t.create_ring())
		# self.player.equip(t.create_armor_plate())
		# self.player.add_effect(t.EPoison(self.player))
		# self.player.add_effect(t.EIncreaceDamage(self.player))

		self.player.inventory.add_item(t.create_poison())
		self.player.inventory.add_item(t.create_quest_item())

		self.enemiesList = []
		for i in range(0, 2):
			g = t.create_goblin()
			g.equip(t.create_sword())
			self.enemiesList.append(g)

		self.interface = combatinterface.CombatInterface(self, self.player, self.enemiesList)


	def temp_showinv(self, container):
		self.interface = containerinterface.PlayerInventoryInterface(self, container)
	def temp_showstat(self, who):
		self.interface = interface.StatusInterface(self, who)

	def atack(self, atacker, atacked):
		dm = damage.DamageCalculator(atacker, atacked)
		atacked.health = atacked.health - dm.finaldamage
		return atacked.isDead

	def exit(self):
		self.doExit = True

	def update(self):
		self.player.update_effects()
		for e in self.enemiesList:
			e.update_effects()
		self.interface.update()
		self.interface.show()
		self.interface.process_commands()

# test = fake_game()
# while not test.doExit:
#	test.update()

# test.start()


# print("'Ok. Lets do some magic! \033[2B\033[106;95m\033[3m\033[52m Some magic happening!!! \033[0m\033[2A Are you impressed?")