import interface as itf

class Gameplay():
	def __init__(self, gameClass):
		self._gameClass = gameClass
		self._currentInterface = itf.Interface()
		self._valid_comands = ["q", "quit", "h", "help"]
	
	@property
	def currentInterface(self):
		return self._currentInterface
	
	def _valid_comand_input(self, commandsList):
		c = str(input())
		while not c in commandsList:
			itf.Interface.show_message("Unknown comand. Please type one of: ", commandsList)
			c = input()
		return c

	def _command_check(self, command, commandsList):
		return command in commandsList

	def _exitCheck(self, command):
		if self._command_check(command, ["q", "quit"]):
			self._currentInterface.clear()
			self._currentInterface.add_showable( ChoiseApprovalView(["Are you shure, that you want to exit?"]) )
			self._currentInterface.show()

			answer = self._valid_comand_input(["y", "yes", "n", "no"])
			return answer in ["y", "yes"]


	def _helpCheck(self, command):
		return self._command_check(command, ["h", "help"])

	def build_default_interface(self):
		self._currentInterface.clear()

	def process_commands(self):
		self.build_default_interface()
		self._currentInterface.show()
		self._comand = self._valid_comand_input(self._valid_comands)
		if self._exitCheck(self._command):
		 	gameClass.doExit = True;
		 	return
		if self._helpCheck(self._command):
		 	self._currentInterface.showHelp()
		 	return

class CharacterCreation(Gameplay):
	def __init__(self, gameClass):
		super().__init__(gameClass)

	def process_commands(self):
		super().process_commands()

class InventoryMenuGameplay(Gameplay):
	def __init__(self, gameClass):
		super().__init__(gameClass)
		self._interfacePage = 0
		for vc in ["+", "-", "0"]:
			self._valid_comands.append(vc)

	def _get_items_from_page(self, page_number):
		pass
		# player.getItemNames page_number*9 -> page_number*9+9
		# self._valid_comands.append(0-9) or less

	def next_page(self):
		self._interfacePage += 1
		# check are there any items on this page
	def previous_page(self):
		if self._interfacePage > 0:
			self._interfacePage -= 1

	def use_item(self, item_index):
		self._currentInterface.clear()
		self._currentInterface.add_showable( ChoiseApprovalView(["Are you shure, that you want to use"], 
			[""], # player.getItemName(id) 
			["?"]
		) )
		self._currentInterface.show()

		answer = self._valid_comand_input(["y", "yes", "n", "no"])
		if answer in ["y", "yes"]:
			#player.useItem(item_index)
			return 0
		return 1

	def build_default_interface(self):
		itemNames = self._get_items_from_page(self._interfacePage)
		self._currentInterface.add_showable( InventoryView(itemNames) )

	def process_commands(self):
		
		super().process_commands()
		if self._comand == "0":
			# exit
			return 0
		if self._comand == "+":
			self.next_page()
			return 1
		if self._comand == "-":
			self.previous_page()
			return 1

		return use_item(int(self._command))

		

class TownGameplay(Gameplay):
	def __init__(self, gameClass):
		super().__init__(gameClass)

	def process_commands(self):
		super().process_commands()

class TavernGameplay(Gameplay):
	def __init__(self, gameClass):
		super().__init__(gameClass)

	def process_commands(self):
		super().process_commands()

class ShopGameplay(Gameplay):
	def __init__(self, gameClass):
		super().__init__(gameClass)

	def process_commands(self):
		super().process_commands()

class JourneyGameplay(Gameplay):
	def __init__(self, gameClass):
		super().__init__(gameClass)

	def process_commands(self):
		super().process_commands()

class CombatGameplay(Gameplay):
	def __init__(self, gameClass):
		super().__init__(gameClass)

	def process_commands(self):
		super().process_commands()