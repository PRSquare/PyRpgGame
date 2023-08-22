import effect
import random

MAXIMUM_RESISTANCE = 0.9
MAXIMUM_DAMAGE_MOODIFICATOR = 5
# MAXIMUM_DAMAGE = 10000000

class DamageCalculator():
	def __init__(self, dealer, reciver):
		self.finaldamage = 0
		useddmgtypes = []
		dmgl = dealer.damageList
		modl = dealer.damageModificators
		resl = reciver.resistances
		if not dmgl:
			return

		i = 0
		dmgtype = dmgl[i].damage_type
		useddmgtypes.append(dmgtype)
		while i < len(dmgl):
			d = 0
			m = 1
			r = 0
			for dmel in dmgl: # calculate all damage of a type
				if dmel.damage_type == dmgtype:
					d += dmel.get_damage()

			for mdel in modl: #  calculate damage modificators of a type
				if mdel.damage_type == dmgtype:
					m += mdel.getInFloat()

			for rsel in resl: # calculate all resistance og a type
				if rsel.damage_type == dmgtype:
					r += rsel.getInFloat()
			
			self.finaldamage += d * min(m, MAXIMUM_DAMAGE_MOODIFICATOR) * (1-min(MAXIMUM_RESISTANCE, r))

			# geting next damage type
			j = i+1
			for i in range(j, len(dmgl)):
				if not dmgl[i].damage_type in useddmgtypes:
					dmgtype = dmgl[i].damage_type
					useddmgtypes.append(dmgtype)
					break
			
			i += 1



	# def deal_damage(self):
	# 	pass

class DamageModificator(): # DamageModificator / Resistance
	def __init__(self, percent = 0, damage_type = ""):
		self.damage_type = damage_type
		self.percent = percent

	def getInFloat(self):
		return self.percent/100.0

class Damage():
	def __init__(self, n = 1, d = 1, add = 0, damage_type = ""):
		self.damage_type = damage_type
		self.n = n
		self.d = d
		self.add = add

	def get_damage(self):
		retDmg = 0
		for i in range(0, self.n):
			retDmg += random.randrange(1, self.d)
		retDmg += self.add

		return retDmg