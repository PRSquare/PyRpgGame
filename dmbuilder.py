import builder
import damage
import random


class DMBuilder(builder.Builder):
	def __init__(self):
		self._damage_type = []
		self._percent = []

	@property
	def damage_type(self):
		return self._damage_type
	@damage_type.setter
	def damage_type(self, val):
		if val != None:
			self._damage_type = val

	@property
	def percent(self):
		return self._percent
	@percent.setter
	def percent(self, val):
		if val != None:
			self._percent = val

	def build(self):
		dm = damage.DamageModificator()
		dm.damage_type = builder.get_random_element(self.damage_type)
		dm.percent = random.randrange(self.percent[0], self.percent[1])

		return dm