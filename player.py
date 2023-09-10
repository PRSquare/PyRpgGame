import alive
import globaldata
import builder
import quest

class Journal():
	def __init__(self):
		self.questlist = []
		self._questLimit = 3

	@property
	def questLimit(self):
		return self._questLimit
	@questLimit.setter
	def questLimit(self, val):
		if val != None and val > 0:
			self._questLimit = val
			
	def add(self, quest):
		if len(self.questlist) >= self._questLimit:
			return False
		self.questlist.append(quest)
		return True

	def update(self):
		for q in self.questlist:
			if q.isComplited:
				self.questlist.remove(q)

	def remove(self, quest):
		self.questlist.remove(quest)


class Player(alive.Alive):
	def __init__(self, name = "Player"):
		super().__init__()

		self.name = "Player"
		self.health = 100
		self.experience = 100
		self.money = 10000

		self.eqSlots.append(alive.EquipementSlot("hand"))
		self.eqSlots.append(alive.EquipementSlot("hand"))

		self.eqSlots.append(alive.EquipementSlot("finger"))
		self.eqSlots.append(alive.EquipementSlot("finger"))
		self.eqSlots.append(alive.EquipementSlot("finger"))
		self.eqSlots.append(alive.EquipementSlot("finger"))

		self.eqSlots.append(alive.EquipementSlot("head"))
		self.eqSlots.append(alive.EquipementSlot("torso"))
		self.eqSlots.append(alive.EquipementSlot("legs"))

		self.journal = Journal()

	def update():
		self.update_effects()
		self.journal.update()
	