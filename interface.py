class Showable():
	def show(self):
		pass

class InputVariant(Showable):
	def __init__(self, command = '', description = ''):
		self.command = command
		self.description = description

	def equals(self, variant):
		return self.command == variant.command

	def show(self):
		print(self.command, "-", self.description)

class Message(Showable):
	def __init__(self, text = "",  inputVars = []):
		self.text = text
		self.inputVars = inputVars
	def show(self):
		print(self.text)
		for iv in self.inputVars:
			iv.show()

	def get_result(self):
		c = input()
		for iv in self.inputVars:
			if iv.command == c:
				return iv
		on_wrong_input()
		return None

	def on_wrong_input(self):
		pass



class Interface(Showable):
	def  __init__(self, gameClassHandler):
		self.gameClassHandler = gameClassHandler
		self.inputVars = dict()
	def show(self):
		pass
	def update(self):
		pass
	def process_commands(self):
		pass

	def show_input_vars(self):
		for iv in self.inputVars.values():
			iv.show()
	def on_wrong_input(self):
		print("Unknown command. Please try again")
		self.show_input_vars()

def default_message_yes_or_no(text):
	return Message(
				text,
				[
					InputVariant("y", "yes"),
					InputVariant("n", "no")
				]
			)

def quit_command_builder():
	return InputVariant('q', "Close window")

def yes_command_builder():
	return InputVariant('y', "Yes")

def no_command_builder():
	return InputVariant('n', "No")

_available_damage_types = { # TEMP TEMP TEMP!!!!!!!!
	0: "physiscal",
	1: "fire",
	2: "water",
	3: "air",
	4: "earth"
} 
def damage_type_to_string(dt):
	return _available_damage_types[dt]

def damage_to_string(damage):
	n = damage.n
	d = damage.d
	add = damage.add
	dt = damage_type_to_string(damage.damage_type.type)
	return f"{n}d{d}+{add} ({dt})"
	

def damage_modificator_to_string(damageMod):
	p = damageMod.percent
	dt = damage_type_to_string(damageMod.damage_type.type)
	return f"{p}% ({dt})"

def effect_to_string(effect):
	finstr = effect.name
	if effect.isActive:
		dur = effect.duration
		if dur != -1:
			finstr += f" ({dur} turns left)"
	elif not effect.isApplied:
		finstr += f" ({effect.delay} turns until activation)"
	if effect.caster != None:
		finstr += f"\n\tCasted by {effect.caster.name}"
	return finstr


def item_to_string(item):
	finstr = item.name
	if item.slot != None:
		finstr += f" [{item.slot.name}]"
	return finstr


class StatusInterface(Interface):
	def __init__(self, gameClassHandler, observable):
		self._observable = observable
		super().__init__(gameClassHandler)
		self.inputVars["quit"] = quit_command_builder()
		self.inputVars["inventory"] = InputVariant("i", "inventory")

		self.update()

	def update(self):
		pass

	def show(self):
		self.effects = [effect_to_string(ef) for ef in self._observable.effects]
		self.equipment = [item_to_string(i) for i in self._observable.equipment]
		self.damages = [damage_to_string(dmg) for dmg in self._observable.damageList]
		self.resistances = [damage_modificator_to_string(dm) for dm in self._observable.resistances]
		self.dms = [damage_modificator_to_string(dm) for dm in self._observable.damageModificators]

		print("---------------")
		print(f"\t\t{self._observable.name}")
		print(f"HP [{self._observable.health}/{self._observable.maxHealth}]")
		print(f"EXP {self._observable.experience}")
		print("---------------")
		print("\t\tEQUIPMENT:")
		for eq in self.equipment:
			print(eq)
		print("\n\t\tEFFECTS:")
		for ef in self.effects:
			print(ef)
		print("\n\t\tDAMAGE:")
		for dmg in self.damages:
			print(dmg)
		print("\n\t\tRESISTANCE:")
		for res in self.resistances:
			print(res)
		print("\n\t\tDAMAGE MODIFICATORS:")
		for dm in self.dms:
			print(dm)

		print("\n\n")
		self.show_input_vars()
		print(">", end="")
		

	def process_commands(self):
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

		if inputed.equals(self.inputVars["inventory"]):
			self.gameClassHandler.temp_showinv()
