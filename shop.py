import random
import globaldata
import builder
import container

class Shop():
	def __init__(self):
		self.goods = container.Container()
		goods.name = "Shop"
		self.available_items = []
		self.items_amount = 10
	def gen_items(self):
		for i in range(0, self.items_amount):
			itemB = builder.get_random_element(self.available_items)
			self.goods.add_item(itemB.build())

	def sell_at(self, it_id):
		return goods.remove_buy_id(it_id)

	def buy(self, item):
		self.items.add_item(item)
		return item.price