import alive

class Monster(alive.Alive):
	def __init__(self):
		super().__init__()
		self.drop = []

	def getDrop(self):
		return self.drop