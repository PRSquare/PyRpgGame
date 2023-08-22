import builder
import item
import random

class ItemBuilder(builder.Builder):
	def __init__(self):
		self._name = ""
		self._description = ""
		self.slot = None
		self._effectsVariants = []
		self._isUsable = False
		self._isProtected = False
		self._usagesNumber = []
		self._rarity = 1
		self._price = 10


	@property
	def usagesNumber(self):
		return self._usagesNumber
	@usagesNumber.setter
	def usagesNumber(self, val):
		if val != None:
			self._usagesNumber = val

	@property
	def rarity(self):
		return self._rarity
	@rarity.setter
	def rarity(self, val):
		if val != None:
			self._rarity = val

	@property
	def price(self):
		return self._price
	@price.setter
	def price(self, val):
		if val != None:
			self._price = val

	@property
	def name(self):
		return self._name
	@name.setter
	def name(self, val):
		if val != None:
			self._name = val


	@property
	def description(self):
		return self._description
	@description.setter
	def description(self, val):
		if val != None:
			self._description = val


	@property
	def effectsVariants(self):
		return self._effectsVariants
	@effectsVariants.setter
	def effectsVariants(self, val):
		if val != None:
			self._effectsVariants = val

	@property
	def isUsable(self):
		return self._isUsable
	@isUsable.setter
	def isUsable(self, val):
		if val != None:
			self._isUsable = val

	@property
	def isProtected(self):
		return self._isProtected
	@isProtected.setter
	def isProtected(self, val):
		if val != None:
			self._isProtected = val

	def build(self):
		i = item.Item()
		i.name = self.name
		i.description = self.description
		i.slot = self.slot
		i.isUsable = self.isUsable
		i.isProtected = self.isProtected
		i.usagesNumber = builder.get_random_element(self.usagesNumber)
		i.rarity = self.rarity
		
		efOption = builder.get_random_element(self.effectsVariants)
		if efOption:
			for ef in efOption:
				if ef:
					i.effects.append(ef)
					
		return i
