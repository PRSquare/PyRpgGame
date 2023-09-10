import random
import builder

class MonsterSpawn(builder.Builder):
	_amount = []
	_monsterB = None

#____________________ properties ____________________
	@property
	def amount(self):
		return self._amount
	@amount.setter
	def amount(self, val):
		if val != None:
			pass

	@property
	def monster(self):
		return self._monsterB
	@monster.setter
	def monster(self, val):
		if val != None:
			self._monsterB = val

#____________________ public methods ____________________
	def build(self):
		n = random.randrange(1, self._amount)
		ret_monsters_list = []
		for i in range(0, n):
			ret_monsters_list.append(self._monsterB.build())
		return ret_monsters_list

			
class LocCell():
	monsters = []
	items = []

class Location():
	name = None
	spawnVars = [[]]
	bossfight = []
	_currentPlayerPose = 0
	isFinished = False
	_size = 10
	cells = []

#____________________ properties ____________________
	@property
	def currentPlayerPose(self):
		return self._currentPlayerPose
	@currentPlayerPose.setter
	def currentPlayerPose(self, cpp):
		self._currentPlayerPose = cpp
		if cpp < 0:
			self._currentPlayerPose = 0
		if cpp > self.size:
			self._currentPlayerPose = self.size

		if self._currentPlayerPose == self.size:
			self.isFinished = True
		elif isFinished == True:
			isFinished = False


	@property
	def size(self):
		return self._size
	@size.setter
	def size(self, val):
		if val != None:
			self._size = val


#____________________ public methods ____________________
	
	def __init__(self, size = 10):
		self.size = size

	def generate(self):
		cells.clear()
		for i in range(0, size):
			cells.append(LocCell())

	def spawn_monsters(self, poition):
		sv = builder.get_random_element(self.spawnVars)
		if sv:
			for spawn in sv:
				pass

		self.cells[position].monsters.append(None) # monster

	def place_item(self, position, item):
		self.cells[position].items.append(item)

	def place_monster(self, position, monster):
		self.cells[position].monsters.append(monster) 

	def get_next_cell(self):
		if not self.isFinished:
			self.currentPlayerPose += 1
			self.get_cell(self.currentPlayerPose)

	def get_cell(self, position):
		return self.cells[position]

	def getLoot(self):
		pass		
				

	def reset(self):
		self._currentPlayerPose = 0
		self.generate()

#____________________ private methods ____________________
	def __generate_location(self, difficulty, size):
		pass
	def __place_quest_item(self, item, position):
		pass
