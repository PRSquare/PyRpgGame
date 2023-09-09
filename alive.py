import container

class EquipementSlot():
	def __init__(self, name):
		self.name = name
		self._isBusy = False
		self._item = None
	
	@property
	def item(self):
		return self._item

	@property
	def isBusy(self):
		return self._isBusy

	def equip(self, item):
		if self.equals(item.slot):
			self._isBusy = True
			self._item = item

	def unequip(self):
		self._isBusy = False
		self._item = None

	def equals(self, slot):
		return self.name == slot.name

	def canWear(self, item):
		return self.equals(item.slot)

class Alive():
	_name = None
	_health = None
	maxHealth = 100
	_experience = None
	money = 0
	_isDead = False

	_equipment = []
	_eqSlots = []
	_effects = []
	
	_damageList = []
	_resistances = []
	_damageModificators = []
	inventory = None

	def __init__(self):
		self.inventory = container.Container(self)

#____________________ properties ____________________
	@property
	def name(self):
		return self._name
	@name.setter
	def name(self, newName):
		self._name = newName
		self.inventory.update()

	@property
	def health(self):
		return self._health
	@health.setter
	def health(self, newHealth):
		if newHealth <= 0:
			self.kill()
			return
		if newHealth > self.maxHealth:
			self._health = self.maxHealth
			return
		self._health = newHealth

	@property
	def experience(self):
		return self._experience
	@experience.setter
	def experience(self, val):
		if val < 0:
			return
		self._experience = val

	@property
	def equipment(self):
		return self._equipment
	@property
	def eqSlots(self):
		return self._eqSlots
	@property
	def effects(self):
		return self._effects

	@property
	def isDead(self):
		return self._isDead

	@property
	def damageList(self):
		return self._damageList

	@property
	def resistances(self):
		return self._resistances

	@property
	def damageModificators(self):
		return self._damageModificators



#____________________ public methods ____________________
	def kill(self):
		if self._isDead:
			return
		self._health = 0
		self._isDead = True
		self.name = self.name + "'s Corpse"	

	def add_experience(self, val):
		if val < 0:
			return
		self._experience += val

	def get_slot_to_wear(self, item):
		availBusySlot = None
		for slot in self._eqSlots:
			if slot.equals(item.slot):
				if not slot.isBusy:
					return slot
				availBusySlot = slot
		return availBusySlot

	def apply_item_effects(self, item):
		for effect in item.effects:
			self.add_effect(effect)

	def remove_effects(self, item):
		for effect in item.effects:
			self.remove_effect(effect)

	def equip(self, item):
		if item.isEquiped:
			return

		if not item.isEquippable:
			return

		slot = self.get_slot_to_wear(item)
		if slot == None:
			return

		if not self.inventory.contains(item):
			self.inventory.add_item(item)
		
		if slot.isBusy:
			self.unequip(slot.item)

		slot.equip(item)
		item.isEquiped = True
		self.apply_item_effects(item)

		self._equipment.append(item)

	
	def unequip(self, item):
		if not item.isEquiped:
			return
		if not self.inventory.contains(item):
			return
		# print(f"unequiping {item.name}")

		item.isEquiped = False
		
		self.remove_effects(item)
		for slot in self._eqSlots:
			if slot.item == item:
				slot.unequip()

		self._equipment.remove(item)

	def use(self, item):
		if not item.isUsable:
			return

		if item.isProtected:
			return

		self.apply_item_effects(item)
		item.onUse()

		if item.isEquiped:
			self.unequip(item)

		if self.inventory.contains(item):
			if item.isUsed:
				self.inventory.remove(item)

	def add_effect(self, effect):
		if not effect in self.effects:
			effect.target = self
			self._effects.append(effect)

	def remove_effect(self, effect):
		if effect in self._effects:
			effect.on_end()
			effect.reset()
			effect.target = None
			self._effects.remove(effect)

	def update_effects(self):
		activeEffects = [] # remove all unactive effects
		for e in self._effects:
			e.update() # apply effect
			if e.isActive:
				activeEffects.append(e)

		self._effects.clear()
		self._effects = activeEffects # only active effects in self._effects now


	def add_damage(self, damage):
		if not damage in self._damageList:
			self._damageList.append(damage)

	def remove_damage(self, damage):
		try:
			self._damageList.remove(damage)
		except Exception:
			raise

	def add_resistance(self, resistance):
		if not resistance in self._resistances:
			self._resistances.append(resistance)

	def remove_resistance(self, resistance):
		try:
			self._resistances.remove(resistance)
		except Exception:
			raise

	def add_damage_modif(self, damageModif):
		if not damageModif in self._damageModificators:
			self._damageModificators.append(damageModif)

	def remove_damage_modif(self, damageModif):
		try:
			self._damageModificators.remove(damageModif)
		except Exception:
			raise

	def add_item(self, item):
		return self.inventory.add_item(item)

	def drop(self, item):
		self.unequip(item)
		return self.inventory.remove(item)
