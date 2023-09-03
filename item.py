import damage

class Item:
	def __init__(self, name = "Unnamed item"):
		self.name = name
		self.description = None
		self._slot = None
		self.effects = []
		self.isEquiped = False
		self.isEquippable = False
		self.isUsable = True
		self._isUsed = False
		self.isProtected = False # Can't remove item if it is protected
		self.usagesNumber = 1
		self.rarity = 0
		self.price = 0

	@property
	def isUsed(self):
		return self._isUsed

	def onUse(self):
		if self.isProtected:
			return
		if not self.isUsable:
			return
		if self._isUsed:
			return
		self.usagesNumber -= 1
		if self.usagesNumber <= 0:
			self._isUsed = True

	@property
	def slot(self):
		return self._slot

	@slot.setter
	def slot(self, s):
		self._slot = s
		self.isEquippable = s != None