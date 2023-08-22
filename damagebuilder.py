import builder
import damage
import random


class DamageBuilder(builder.Builder):
	def __init__(self):
		self._damage_type = ["physical"]
		self._n = [0, 0]
		self._d = [0, 0]
		self._add = [0, 0]

	@property
	def damage_type(self):
		return self._damage_type
	@damage_type.setter
	def damage_type(self, val):
		if val != None:
			self._damage_type.clear()
			self._damage_type = val


	@property
	def n(self):
		return self._n
	@n.setter
	def n(self, val):
		if val != None:
			self._n = val

	@property
	def d(self):
		return self._d
	@d.setter
	def d(self, val):
		if val != None:
			self._d = val

	@property
	def add(self):
		return self._add
	@add.setter
	def add(self, val):
		if val != None:
			self._add = val

	def build(self):
		dmg = damage.Damage()
		dmg.damage_type = builder.get_random_element(self.damage_type)
		dmg.n = random.randrange(self.n[0], self.n[1])
		dmg.d = random.randrange(self.d[0], self.d[1])
		dmg.add = random.randrange(self.add[0], self.add[1])

		return dmg

