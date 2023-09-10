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
	def __init__(self, gameClassHandler, tavern):
		super().__init__(gameClassHandler)
		self.tavern = tavern
		self.inputVars["take_quest"] = interface.InputVariant('t', "take quest")
		
		self.inputVars["shop"] = interface.InputVariant('h', "go to shop")
		self.inputVars["journey"] = interface.InputVariant('j', "start journey")
		
		self.inputVars["status"] = interface.InputVariant('s', "status")
		self.inputVars['inventory'] = interface.InputVariant('i', "inventory")

		self.inputVars["quit"] = interface.InputVariant('q', "quit")

	def show(self):
		for quest in self.tavern.available_quests:
			print(quest_to_str(quest))

	def _input_processor(self, inputed):
		
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
			inv = containerinterface.InventoryInterface(self.gameClassHandler, self.gameClassHandler.player)
			while inv.isOpen:
				inv.show()
				inv.process_commands()

		if inputed.equals(self.inputVars["quit"]):
			self._isOpen = False




class BuyInterface(containerinterface.ContainerInterface):
	def __init__(self, gameClassHandler, shop):
		self.shop = shop
		super().__init__(gameClassHandler, self.shop.goods)
		self.inputVars["buy"] = interface.InputVariant('b', "by item")

	def update(self):
		super().update()
		self.inputVars["buy"] = interface.InputVariant('b', "by item")

	def show(self):
		super().show()
		print(f"______________________________\nYou have {self.gameClassHandler.player.money} coins\n")

	def _input_processor(self, inputed):
		super()._input_processor(inputed)

		if inputed.equals(self.inputVars["buy"]):
			i = self.input_number(0, containerinterface.ITEMS_PER_PAGE)
			item = self.shop.sell_at(self._get_id_from_inputed_number(i))
			self.gameClassHandler.player.money -= item.price
			self.gameClassHandler.player.add_item(item)

class SellInterface(containerinterface.ContainerInterface):
	def __init__(self, gameClassHandler, shop):
		self.shop = shop
		super().__init__(gameClassHandler, gameClassHandler.player.inventory)
		self.inputVars["sell"] = interface.InputVariant('s', "sell item")

	def update(self):
		super().update()
		self.inputVars["sell"] = interface.InputVariant('s', "sell item")

	def show(self):
		super().show()
		print(f"______________________________\nYou have {self.gameClassHandler.player.money} coins\n")

	def _input_processor(self, inputed):
		super()._input_processor(inputed)
		
		if inputed.equals(self.inputVars["sell"]):
			i = self.input_number(0, containerinterface.ITEMS_PER_PAGE)
			it_id = self._get_id_from_inputed_number(i)
			item = self.gameClassHandler.player.inventory.at(it_id)
			self.gameClassHandler.player.remove_item(item)
			self.shop.buy(item)
			self.gameClassHandler.player.money += item.price
			


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

	def _input_processor(self, inputed):
		
		if inputed.equals(self.inputVars["sell"]):
			si = SellInterface(self.gameClassHandler, self.shop)
			while si.isOpen:
				si.show()
				si.process_commands()


		if inputed.equals(self.inputVars["buy"]):
			bi = BuyInterface(self.gameClassHandler, self.shop)
			while bi.isOpen:
				bi.show()
				bi.process_commands()	

		if inputed.equals(self.inputVars["tavern"]):
			self.gameClassHandler.go_to_tavern()

		if inputed.equals(self.inputVars["journey"]):
			self.gameClassHandler.go_to_journey()

		if inputed.equals(self.inputVars["status"]):
			stat = interface.StatusInterface(self.gameClassHandler, self.gameClassHandler.player)
			while stat.isOpen:
				stat.show()
				stat.process_commands()

		if inputed.equals(self.inputVars["inventory"]):
			inv = containerinterface.InventoryInterface(self.gameClassHandler, self.gameClassHandler.player)
			while inv.isOpen:
				inv.show()
				inv.process_commands()

		if inputed.equals(self.inputVars["quit"]):
			self._isOpen = False


class JourneyInterface(interface.Interface):
	def __init__(self, gameClassHandler, location):
		super().__init__(gameClassHandler)
		self.location = location

		self.inputVars["quit"] = interface.InputVariant('q', "quit")
		self.inputVars["status"] = interface.InputVariant('s', "status")
		self.inputVars["inventory"] = interface.InputVariant('i', "inventory")
		self.inputVars["countinue"] = interface.InputVariant('c', "countinue jorney")
		self.inputVars["return"] = interface.InputVariant('r', "return to the village")


	def show(self):
		print(f"\t{self.location.name}")
		print(f"\t     [{self.location.currentPlayerPose}/{self.location.size}]")

	def _input_processor(self, inputed):
		
		if inputed.equals(self.inputVars["status"]):
			stat = interface.StatusInterface(self.gameClassHandler, self.gameClassHandler.player)
			while stat.isOpen:
				stat.show()
				stat.process_commands()

		if inputed.equals(self.inputVars["inventory"]):
			inv = containerinterface.InventoryInterface(self.gameClassHandler, self.gameClassHandler.player)
			while inv.isOpen:
				inv.show()
				inv.process_commands()

		if inputed.equals(self.inputVars["quit"]):
			self._isOpen = False

		if inputed.equals(self.inputVars["return"]):
			self.gameClassHandler.go_to_tavern()

		if inputed.equals(self.inputVars["countinue"]):
			nextCell = self.location.get_cell()
			# Combat