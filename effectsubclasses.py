import effect
import damage

class EAddDamage(effect.Effect):
	def __init__(self, target = None):
		super().__init__(target)
		self.name = "Physiscal damage increacement"
		self.duration = -1
		self._damage = damage.Damage(2, 8, 2)
		self.isResetable = True
		
	@property
	def damage(self):
		return self._damage
	@damage.setter
	def damage(self, val):
		if val != None:
			self._damage = val

	def on_apply(self):
		self.target.add_damage(self._damage)

	def on_tick(self):
		pass

	def on_end(self):
		self.target.remove_damage(self._damage)


class EDecreaceHealth(effect.Effect):
	def __init__(self, target = None):
		super().__init__(target)
		self.name = "HealthDecreacement"
		self.duration = 1
		self.strength = 1

	def on_apply(self):
		pass

	def on_tick(self):
		self.target.health -= self.strength

	def on_end(self):
		pass

class ERestoreHealth(effect.Effect):
	def __init__(self, target = None):
		super().__init__(target)
		self.name = ""
		self.duration = 1
		self.strength = 1

	def on_apply(self):
		pass

	def on_tick(self):
		self.target.health += self.strength

	def on_end(self):
		pass

class EAddDamageModificator(effect.Effect):
	def __init__(self, target = None):
		super().__init__(target)
		self.name = "Damage modificator"
		self.duration = 1
		self._dm = damage.DamageModificator(1)

	@property
	def dm(self):
		return self._dm
	@dm.setter
	def dm(self, val):
		if val != None:
			self._dm = val

	def on_apply(self):
		self.target.add_damage_modif(self._dm)

	def on_tick(self):
		pass

	def on_end(self):
		self.target.damageModificators.remove_damage_modif(self._dm)

class EAddResistance(effect.Effect):
	def __init__(self, target = None):
		super().__init__(target)
		self.name = "Incoming damage modificator"
		self.duration = 1
		self._dm = damage.DamageModificator(1)
		self.isResetable = True

	@property
	def dm(self):
		return self._dm
	@dm.setter
	def dm(self, val):
		if val != None:
			self._dm = val
			

	def on_apply(self):
		self.target.add_resistance(self._dm)

	def on_tick(self):
		pass

	def on_end(self):
		self.target.remove_resistance(self._dm)


class EVampirism(effect.Effect):
	def __init__(self, target = None, caster = None):
		super().__init__(target, caster)
		self.name = "Vampirism"
		self.duration = 1
		self.strength = 1

	def on_apply(self):
		pass

	def on_tick(self):
		self.target.health -= self.strength
		self.caster.health += self.strength

	def on_end(self):
		pass

class ETemporaryHeal(effect.Effect):
	def __init__(self, target = None):
		super().__init__(target)
		self.name = "Temporary heal"
		self.duration = 1
		self.strength = 1

	def on_apply(self):
		target.health += self.strength

	def on_tick(self):
		pass

	def on_end(self):
		target.health -= self.strength