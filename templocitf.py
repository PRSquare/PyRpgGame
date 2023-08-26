import interface
import containerinterface
import player # Quest

def quest_to_str(quest):
	retstr = ""
	if quest.isComplited:
		retstr += "[complited]"
	if quest.isRuined:
		retstr += "[ruined]"

	retstr += f"{quest.name}:\n\t{quest.description}"

	return retstr

class TavernInterface(interface.Interface):
	def __init__(self, gameClassHandler):
		super().__init__(gameClassHandler)
		self.inputVars["take_quest"] = interface.InputVariant('t', "take quest")
		
		self.inputVars["shop"] = interface.InputVariant('h', "go to shop")
		self.inputVars["journey"] = interface.InputVariant('j', "start journey")
		
		self.inputVars["status"] = interface.InputVariant('s', "status")
		self.inputVars['inventory'] = interface.InputVariant('i', "inventory")

		self.inputVars["quit"] = interface.InputVariant('q', "quit")

		self.tavern = self.gameClassHandler.tavern 

	def show(self):
		for quest in self.tavern.available_quests
			print(quest_to_str(quest))

	def process_commands():
		self.show_input_vars()
		inputed = self.input_command()

		if inputed.equals(self.inputVars["take_quest"]):
			i = self.input_number(0, len(self.tavern.available_quests))
			# Take quest

		if inputed.equals(self.inputVars["shop"]):
			self.gameClassHandler.go_to_shop()

		if inputed.equals(self.inputVars["journey"]):
			self.gameClassHandler.go_to_journey()

		if inputed.equals(self.inputVars["status"]):
			stat = interface.StatusInterface(self.gameClassHandler, self.gameClassHandler.player)
			while stat.isOpen:
				stat.show()
				stat.process_commands()

		if inputed.equals(self.inputVars["inventory"]):
			inv = containerinterface.ContainerInterface(self.gameClassHandler, self.gameClassHandler.player.inventory)
			while inv.isOpen:
				inv.show()
				imv.process_commands()

			if inputed.equals(self.inputVars["quit"]):
				self._isOpen = False




class BuyInterface(containerinterface.ContainerInterface):
	def __init__(self, gameClassHandler, shop):
		self.shop = shop
		super().__init__(gameClassHandler, self.shop.goods)
		self.inputVars["buy"] = interface.InputVariant('b', "by item")

	def update(self):
		super().update()

	def show(self):
		super().show()

	def process_commands(self):
		super.process_commands()
		
		inputed = self.input_command()
		if inputed.equals(self.inputVars["buy"]):
			i = self.input_number(0, containerinterface.ITEMS_PER_PAGE)
			self.gameClassHandler.player.inventory.add_item(self.shop.sell_at(self._get_id_from_inputed_number(i)))

class SellInterface(containerinterface.ContainerInterface):
	def __init__(self, gameClassHandler, shop):
		self.shop = shop
		super().__init__(gameClassHandler, gameClassHandler.player.inventory)
		self.inputVars["sell"] = interface.InputVariant('s', "sell item")

	def update(self):
		super().update()

	def show(self):
		super().show()

	def process_commands(self):
		super.process_commands()
		
		inputed = self.input_command()
		if inputed.equals(self.inputVars["sell"]):
			i = self.input_number(0, containerinterface.ITEMS_PER_PAGE)
			self.shop.buy(self.gameClassHandler.player.inventory.remove_buy_id(self._get_id_from_inputed_number(i)))
			


class ShopInterface(interface.Interface):
	def __init__(self, gameClassHandler, shop):
		self.shop = shop
		super().__init__(gameClassHandler)
		self.inputVars["sell"] = interface.InputVariant('l', "sell items")
		self.inputVars["buy"] = interface.InputVariant('b', "by items")
		
		self.inputVars["tavern"] = interface.InputVariant('t', "go to tavern")
		self.inputVars["journey"] = interface.InputVariant('j', "start journey")
		
		self.inputVars["status"] = interface.InputVariant('s', "status")
		self.inputVars['inventory'] = interface.InputVariant('i', "inventory")

		self.inputVars["quit"] = interface.InputVariant('q', "quit")

		self.shop = self.gameClassHandler.shop 

	def show(self):
		print("Welcom to Mallwart!")

	def process_commands(self):
		inputed = self.input_command()

