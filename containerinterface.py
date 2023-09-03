import interface

ITEMS_PER_PAGE = 10

class ItemDetailsInterface(interface.Interface):
	def __init__(self, gameClassHandler, item):
		super().__init__(gameClassHandler)
		self._item = item

		self.inputVars["quit"] = interface.quit_command_builder()

	def show(self):
		print(f"\t\t{self._item.name}")
		if self._item.slot != None:
			print(f"can be weared on {self._item.slot.name}")
			if self._item.isEquiped:
				print("Equiped")
			else:
				print("Not Equiped")
		if self._item.description != None:
			print(self._item.description)
		print("--------------------")
		effectsStr = []
		for e in self._item.effects:
			effectsStr.append(interface.effect_to_string(e))
		for e in effectsStr:
			print(e)
		print()

	def _input_processor(self, inputed):
		if inputed.equals(self.inputVars["quit"]):
			self._isOpen = False
			return

		self.on_wrong_input()

class ContainerInterface(interface.Interface):
	def __init__(self, gameClassHandler, container):
		super().__init__(gameClassHandler)
		self._container = container
		self._currentPage = 0
		self._itemsList = []
		self._start = 0
		self._end = 0

	def _get_id_from_inputed_number(self, number):
		return self._currentPage*ITEMS_PER_PAGE + number

	def _get_items_list(self, pageNumber):
		self._start = pageNumber * ITEMS_PER_PAGE
		self._end = self._start + ITEMS_PER_PAGE
		if self._end > self._container.count_items():
			self._end -= self._end - self._container.count_items()

		return self._container.itemsList[self._start:self._end]

	def _rebuild_input_vars(self):
		self.inputVars.clear()
		self.inputVars["look"] = interface.InputVariant("l", "look closely")
		# self.inputVars["equip"] = InputVariant("e", "equip")

		self.add_optional_input_vars()

		if self._currentPage != 0:
			self.inputVars["prev_page"] = interface.InputVariant("p", "previous page")
		if self._currentPage*ITEMS_PER_PAGE + ITEMS_PER_PAGE < self._container.count_items():
			self.inputVars["next_page"] = interface.InputVariant("n", "next page")

		self.inputVars["quit"] = interface.quit_command_builder()
		
		#self.inputVars["status"] = interface.InputVariant("s", "show status")

	def add_optional_input_vars(self):
		pass

	def show(self):
		self.update()
		print("--------------------------------------------------------")
		print(f"\t\t{self._container.name}:")
		pagesN = int(self._container.count_items() / ITEMS_PER_PAGE)
		if self._container.count_items() % ITEMS_PER_PAGE != 0:
		 	pagesN += 1
		print(f"\t\t[page {self._currentPage+1}/{pagesN}]")
		j = 0
		for i in self._itemsList:
			print(f"{j}) {i.name}", end="")
			if i.slot != None:
				print(f" [{i.slot.name}]", end="")
			if i.isEquiped:
				print(" *", end="")
			print()
			j += 1
		print("--------------------------------------------------------")
		

	def update(self):
		self._itemsList = self._get_items_list(self._currentPage)
		self._rebuild_input_vars()

	def _input_processor(self, inputed):
		
		if inputed.equals(self.inputVars["quit"]):
			self._isOpen = False
			return
		if inputed.equals(self.inputVars["look"]):
			i = self.input_number(0, ITEMS_PER_PAGE)
			itInterface = ItemDetailsInterface(self.gameClassHandler, self._container.itemsList[self._get_id_from_inputed_number(i)])
			while itInterface.isOpen:
				itInterface.show()
				itInterface.process_commands()
			return

		if "prev_page" in self.inputVars.keys():
			if inputed.equals(self.inputVars["prev_page"]):
				self._currentPage -= 1
				return
		if "next_page" in self.inputVars.keys():
			if inputed.equals(self.inputVars["next_page"]):
				self._currentPage += 1
				return


class InventoryInterface(ContainerInterface):
	def __init__(self, gameClassHandler, holder):
		self.holder = holder
		super().__init__(gameClassHandler, holder.inventory)

	def add_optional_input_vars(self):
		self.inputVars["equip"] = interface.InputVariant("e", "equip/unequip item")
		self.inputVars["drop"] = interface.InputVariant("d", "drop item")
		self.inputVars["use"] = interface.InputVariant("u", "use item")


	def _input_processor(self, inputed):

		super()._input_processor(inputed)

		if inputed.equals(self.inputVars["equip"]):
			print("Wich item you want to equip?")
			i = self.input_number(0, ITEMS_PER_PAGE)
			if i != None:
				item = self._container.itemsList[self._get_id_from_inputed_number(i)]
				if not item.isEquiped:
					self.holder.equip(item)
				else:
					self.holder.unequip(item)
			return

		if inputed.equals(self.inputVars["use"]):
			print("Wich item you want to use?")
			i = self.input_number(0, ITEMS_PER_PAGE)
			item = self._container.itemsList[self._get_id_from_inputed_number(i)]
			self.holder.use(item)
			return

		if inputed.equals(self.inputVars["drop"]):
			print("Wich item you want to drop?")
			i = self.input_number(0, ITEMS_PER_PAGE)
			item = self._container.itemsList[self._get_id_from_inputed_number(i)]
			ausmsg = interface.default_message_yes_or_no(f"Are you shure you want to drop {item.name}? This item will be lost forever!")
			ausmsg.show()
			ans = ausmsg.get_inputed_command()
			if ans.equals(interface.InputVariant("n", "no")):
				return
			self.holder.drop(item)
			return
