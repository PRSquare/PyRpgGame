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
		self.show_input_vars()

	def update(self):
		pass
	def process_commands(self):
		print("> ", end="")
		c = input()
		inputed = None
		for iv in self.inputVars.values():
			if iv.command == c:
				inputed = iv
		if inputed == None:				
			self.on_wrong_input()
			return

		if inputed.equals(self.inputVars["quit"]):
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
		self.inputVars["status"] = interface.InputVariant("s", "show status")

	def add_optional_input_vars(self):
		pass

	def show(self):
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
		self.show_input_vars()

	def update(self):
		self._itemsList = self._get_items_list(self._currentPage)
		self._rebuild_input_vars()

	def on_wrong_input(self):
		pass

	def process_commands(self):
		print("> ", end="")
		c = input()
		inputed = None
		for iv in self.inputVars.values():
			if iv.command == c:
				inputed = iv
		if inputed == None:				
			self.on_wrong_input()
			return

		if inputed.equals(self.inputVars["quit"]):
			self.gameClassHandler.exit()
			return
		if inputed.equals(self.inputVars["look"]):
			print("Wich item you want to look at (print a number or 'c' to cancel)")
			print("> ", end="")
			c = input()
			while(c != 'c'):
				if int(c) not in range(0, ITEMS_PER_PAGE):
					print(f"{int(c)} Incorrect input. Please try again")
				else:
					itInterface = ItemDetailsInterface(self.gameClassHandler, self._container.itemsList[int(c)+self._currentPage*ITEMS_PER_PAGE])
					itInterface.show()
					itInterface.process_commands()
					return
				print("> ")
				c = input()
			return
		if "prev_page" in self.inputVars.keys():
			if inputed.equals(self.inputVars["prev_page"]):
				self._currentPage -= 1
				return
		if "next_page" in self.inputVars.keys():
			if inputed.equals(self.inputVars["next_page"]):
				self._currentPage += 1
				return


class PlayerInventoryInterface(ContainerInterface):
	def __init__(self, gameClassHandler, container):
		super().__init__(gameClassHandler, container)

	def add_optional_input_vars(self):
		self.inputVars["equip"] = interface.InputVariant("e", "equip/unequip item")
		self.inputVars["drop"] = interface.InputVariant("d", "drop item")
		self.inputVars["use"] = interface.InputVariant("u", "use item")

	def process_commands(self):
		print("> ", end="")
		c = input()
		inputed = None
		for iv in self.inputVars.values():
			if iv.command == c:
				inputed = iv
		if inputed == None:				
			self.on_wrong_input()
			return

		if inputed.equals(self.inputVars["quit"]):
			self.gameClassHandler.exit()
			return
		if inputed.equals(self.inputVars["look"]):
			print("Wich item you want to look at (print a number or 'c' to cancel)")
			print("> ", end="")
			c = input()
			while(c != 'c'):
				if int(c) not in range(0, ITEMS_PER_PAGE):
					print(f"{int(c)} Incorrect input. Please try again")
				else:
					itInterface = ItemDetailsInterface(self.gameClassHandler, self._container.itemsList[int(c)+self._currentPage*ITEMS_PER_PAGE])
					itInterface.show()
					itInterface.process_commands()
					return
				print("> ")
				c = input()
			return

		if "prev_page" in self.inputVars.keys():
			if inputed.equals(self.inputVars["prev_page"]):
				self._currentPage -= 1
				return
		if "next_page" in self.inputVars.keys():
			if inputed.equals(self.inputVars["next_page"]):
				self._currentPage += 1
				return

		if inputed.equals(self.inputVars["equip"]):
			print("Wich item you want to equip (print a number or 'c' to cancel)")
			print("> ", end="")
			c = input()
			while(c != 'c'):
				if int(c) not in range(0, ITEMS_PER_PAGE):
					print(f"{int(c)} Incorrect input. Please try again")
					print("> ")
					c = input()
				else:
					item = self._container.itemsList[int(c)+self._currentPage*ITEMS_PER_PAGE]
					if not item.isEquiped:
						self.gameClassHandler.player.equip(item)
					else:
						self.gameClassHandler.player.unequip(item)
					break
			return

		if inputed.equals(self.inputVars["use"]):
			print("Wich item you want to use (print a number or 'c' to cancel)")
			print("> ", end="")
			c = input()
			while(c != 'c'):
				try:
					int(c)
				except Exception:
					print("Please print a number!")
					print("> ")
					c = input
					continue
				if int(c) not in range(0, ITEMS_PER_PAGE):
					print(f"{int(c)} Incorrect input. Please try again")
					print("> ")
					c = input()
				else:
					print(int(c)+self._currentPage*ITEMS_PER_PAGE)
					item = self._container.itemsList[int(c)+self._currentPage*ITEMS_PER_PAGE]
					self.gameClassHandler.player.use(item)
					break

					# if not item.isUsable:
					# 	print("Can't use this item")
					# 	return

					# if item.isEquippable:
					# 	if item.isEquiped:
					# 		self.gameClassHandler.player.unequip(item)
					# 	else:
					# 		self.gameClassHandler.player.equip(item)
					# else:
					# 	for e in item.effects:
					# 		self.gameClassHandler.player.add_effect(e)
					# 	self._container.remove(item)
					# return
			return

		if inputed.equals(self.inputVars["drop"]):
			print("Wich item you want to drop (print a number or 'c' to cancel)")
			print("> ", end="")
			c = input()
			while(c != 'c'):
				if int(c) not in range(0, ITEMS_PER_PAGE):
					print(f"{int(c)} Incorrect input. Please try again")
					print("> ")
					c = input()
				else:
					item = self._container.itemsList[int(c)+self._currentPage*ITEMS_PER_PAGE]
					ausmsg = interface.default_message_yes_or_no(f"Are you shure you want to drop {item.name}? This item will be lost forever!")
					ausmsg.show()
					ans = ausmsg.get_result()
					if ans.equals(interface.InputVariant("n", "no")):
						return
					self.gameClassHandler.player.drop(item)
					return
			return

		if inputed.equals(self.inputVars["status"]):
			self.gameClassHandler.temp_showstat()
			return