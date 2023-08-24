import random
import builder

class MonsterSpawn(builder.Builder):

	def __init__(self):
		self._amont = []
		self._monsterB = None

	@property
	def amont(self):
		return self._amont
	@amont.setter
	def amont(self, val):
		if val != None:
			if isinstance(val, int):
				self._amont = [val, val]
			else:
				self._amont = val

	@property
	def monster(self):
		return self._monsterB
	@monster.setter
	def monster(self, val):
		if val != None:
			self._monsterB = val

	def build(self):
		n = random.randrange(1, self._amont)
		ret_monsters_list = []
		for i in range(0, n):
			ret_monsters_list.append(self._monsterB.build())
		return ret_monsters_list

			


class Location():
	def __init__(self):
		self.name = None
		self.spawn_vars = [[]]
		self.bossfight = []
		self.quest_items = [] # cellNumber : item
		self._currentPlayerPose = 0
		self.isFinished = False
		self.size = 10

	def getCell(self):
		retMonstersPack = []

		if not self.currentPlayerPose < self.size:
			for b in self.bossfight:
				retMonstersPack.append(b)
			
			self.currentPlayerPose += 1

			sv = builder.get_random_element(spawn_vars)
			if sv:
				for spawn in sv:
					for monster in spawn.buiild():
						retMonstersPack.append(monster)


			return retMonstersPack


		
		
		self.currentPlayerPose += 1

		return retMonstersPack

	def getLoot(self):
		loot = []
		for qi in self.quest_items:
			if qi[0] == self.currentPlayerPose:
				loot.append(qi[1])
		return loot
				

	def reset(self):
		self._currentPlayerPose = 0

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

		
	def __generate_location(self, difficulty, size):
		pass
	def __place_quest_item(self, item, position):
		pass
