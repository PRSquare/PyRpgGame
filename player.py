import alive
import globaldata
import builder

class Quest():
	def __init__():
		self.isComplited = False
		self.isRuined = False
		self.name = "quest"
		self.description = "no description"
		self.target = None # Item
		self.reward = builder.get_random_element(globaldata.ITEMS.data) 

class Journal():
	def __init__():
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
	def remove(self, quest):
		self.questlist.remove(quest)


class Player(alive.Alive):
	def __init__(self, name = "Player"):
		super().__init__()
		self.journal = Journal()
	