import random
import globaldata
import builder

class Shop():
	def __init__(self):
		self.items = []
		self.available_items = []
		self.items_amount = 10
	def gen_items(self):
		for i in range(0, self.items_amount):
			itemB = builder.get_random_element(self.available_items)
			items.append(itemB.build())

	def buy_at(self, it_id):
		return items.pop(it_id)

	def sell(self, item):
		self.items.append(item)
		return item.price