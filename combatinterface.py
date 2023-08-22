import interface

class CombatInterface(interface.Interface):
	def  __init__(self, gameClassHandler, atacker, enemies):
		super().__init__(gameClassHandler)
		self._atacker = atacker
		self._enemies = enemies # Alive objects list

		self.inputVars["quit"] = interface.InputVariant("q", "quit")
		self.inputVars["atack"] = interface.InputVariant("a", "atack")
		# self.inputVars["d"] = interface.InputVariant("")
		self.inputVars["use"] = interface.InputVariant("u", "use item")
		self.inputVars["status"] = interface.InputVariant("s", "show your status")
		self.inputVars["look"] = interface.InputVariant("l", "look at enemy")
	def show(self):
		j = 0
		print("Enemies:")
		for e in self._enemies:
			print(f"{j}) {e.name} [{e.health}/{e.maxHealth}]")
			j += 1

		print(f"\n\t{self._atacker.name} [{self._atacker.health}/{self._atacker.maxHealth}]")
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
			self.gameClassHandler.exit()
			return

		if inputed.equals(self.inputVars["atack"]):
			print("chose the enemy\n> ", end="")
			c = input()
			try:
				int(c)
			except Exception:
				print("Please print a number")
				return
			if int(c) >= len(self._enemies):
				print("Invalid number")
				return
			self.gameClassHandler.atack(self._atacker, self._enemies[int(c)])
			return
		if inputed.equals(self.inputVars["look"]):
			print("chose the enemy\n> ", end="")
			c = input()
			try:
				int(c)
			except Exception:
				print("Please print a number")
				return
			if int(c) >= len(self._enemies):
				print("Invalid number")
				return
			self.gameClassHandler.temp_showstat(self._enemies[int(c)])
			return

		if inputed.equals(self.inputVars["use"]):
			items = []
			for i in self._atacker.inventory.itemsList:
				if i.isUsable == True and i.isProtected == False:
					items.append(i)
			if not items:
				print("No items to use")
				return
			j = 0
			for i in items:
				print(f"{j}) {i.name}")
			print("\nchose the item\n> ", end="")
			c = input()
			try:
				int(c)
			except Exception:
				print("Please print a number")
				return
			if int(c) >= len(items):
				print("Invalid number")
				return
			self._atacker.use(items[int(c)])
			return

		if inputed.equals(self.inputVars["status"]):
			self.gameClassHandler.temp_showstat(self._atacker)