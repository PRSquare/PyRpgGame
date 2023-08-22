import random

class Shop():
	def __init__(self):
		self.items = []
		self.available_items = []

	def gen_items(self, amount = 10):
		for i in range(0, amount):
			j = random.randrange(0, len(self.available_items))
			items.append(self._available_damage_types[j])

	def buy_at(self, id):
		item = None
		try:
			item = self.items[id]
		except Exception:
			raise
		return item