import item

class Container():
	def __init__(self, holder):
		self.name = ""
		if holder != None:
			self.name = f"{holder.name}'s inventory"
		self._itemsList = []
		self._holder = holder

	def update(self):
		if self._holder != None:
			self.name = f"{self._holder.name}'s inventory"
	@property
	def itemsList(self):
		return self._itemsList;


	def at(self, id):
		try:
			return self._itemsList[id]
		except Exception:
			raise

	def contains(self, item):
		return item in self._itemsList

	def add_item(self, item):
		if not item in self._itemsList:
			item.holder = self._holder
			self._itemsList.append(item)

	def remove(self, item, ignoreProtection = False):
		if not ignoreProtection:
			if item.isProtected:
				return	
		try:
			self._itemsList.remove(item)
			item.holder = None
		except ValueError:
			raise

	def remove_by_id(self, id, ignoreProtection = False):
		if not ignoreProtection:
			if item.isProtected:
				return
		if i in range(0, len(self._itemsList)):
			raise IndexError
		item = self._itemsList.pop(id)
		item.holder = None
		return item

	def count_items(self):
		return len(self._itemsList)