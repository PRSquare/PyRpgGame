import json

import damage
import item
import monster
import random
import builder
import itembuilder
import dmbuilder
import damagebuilder
import effectsubclasses

class GameData():
	def __init__(self, data):
		self._data = data

	def get(self, element):
		try:
			ret = self._data[element]
			if isinstance(ret, dict):
				return GameData(ret)
			return ret
		except Exception:
			return None


def get_data(filename):
	txt = open(filename).read()
	data = json.loads(txt)
	return GameData(data)

def create_damage_builder(data):
	dmg = damagebuilder.DamageBuilder()
	tp = data.get("type")
	if isinstance(tp, str):
		dmg.damage_type.append(tp)
	else:
		dmg.damage_type = tp

	n = data.get("n")
	d = data.get("d")
	add = data.get("add")
	dmg.n = [n, n] if isinstance(n, int) else n
	dmg.d = [d, d] if isinstance(d, int) else d
	dmg.add = [add, add] if isinstance(add, int) else add

	return dmg


	return dm

def create_dm_builder(data):
	dm = dmbuilder.DMBuilder()
	tp = data.get("type")
	dm.damage_type = [tp] if isinstance(tp, str) else tp

	prc = data.get("value")
	dm.percent = [prc, prc] if isinstance(prc, int) else prc

	return dm

def effect_inic_general_fields(ef, data):
	ef.name = data.get("name")
	ef.description = data.get("description")
	
	dl = data.get("delay")
	
	ef.delay = dl if isinstance(dl, int) or not dl else random.randrange(dl[0], dl[1])
	
	dur = data.get("duration")	
	
	ef.duration = dur if isinstance(dur, int) or not dur else random.randrange(dur[0], dur[1])

	ef.isResetable = data.get("isResetable")



def create_add_dmg_eff(data):
	ef = effectsubclasses.EAddDamage()
	effect_inic_general_fields(ef, data)
	ef.damage = create_damage_builder(data.get("options")).build()
	return ef

def create_decreace_health_ef(data):
	ef = effectsubclasses.EDecreaceHealth()
	effect_inic_general_fields(ef, data)
	strength = data.get("options").get("strength")
	ef.strength = strength if isinstance(strength, int) else random.randrange(strength[0], strength[1])
	return ef

def create_restore_helth_effect(data):
	ef = effectsubclasses.ERestoreHealth()
	effect_inic_general_fields(ef, data)
	strength = data.get("options").get("strength")
	ef.strength = strength if isinstance(strength, int) else random.randrange(strength[0], strength[1])
	return ef

def create_add_dmg_mod_eff(data):
	ef = effectsubclasses.EAddDamageModificator()
	effect_inic_general_fields(ef, data)
	ef.dm = create_dm_builder(data.get("options")).build()
	return ef

def create_add_res_eff(data):
	ef = effectsubclasses.EAddResistance()
	effect_inic_general_fields(ef, data)
	ef.dm = create_dm_builder(data.get("options")).build()
	return ef

def create_vampirism_ef(data):
	ef = effectsubclasses.EVampirism()
	effect_inic_general_fields(ef, data)
	strength = data.get("options").get("strength")
	ef.strength = strength if isinstance(strength, int) else random.randrange(strength[0], strength[1])
	return ef

def create_temp_heal_ef(data):
	ef = effectsubclasses.ETemporaryHeal()
	effect_inic_general_fields(ef, data)
	strength = data.get("options").get("strength")
	ef.strength = strength if isinstance(strength, int) else random.randrange(strength[0], strength[1])
	return ef
	

def create_effect(data):
	t = data.get("type")
	if t == "add_damage":
		return create_add_dmg_eff(data)
	if t == "dec_health":
		return create_decreace_health_ef(data)
	if t == "res_health":
		return create_restore_helth_effect(data)
	if t == "damage_modif":
		return create_add_dmg_mod_eff(data)
	if t == "resist":
		return create_add_res_eff(data)
	if t == "vampirism":
		return create_vampirism_ef(data)
	if t == "temp_heal":
		return create_temp_heal_ef(data)


import alive # slot

def create_item_builder(data):
	ib = itembuilder.ItemBuilder()
	ib.name = data.get("name")
	ib.description = data.get("description")
	ib.slot = alive.EquipementSlot(data.get("slot"))
	ib.isUsable = data.get("isUsable")
	ib.isProtected = data.get("isProtected")
	ib.rarity = data.get("rarity")
	ib.price = data.get("price")
	ib.usagesNumber = data.get("usages_number")


	efsData = data.get("effects")
	if efsData:
		for e in efsData:
			ef_list = []
			for inner_ef in e:
				ef_list.append(create_effect(GameData(inner_ef)))

			ib.effectsVariants.append(ef_list)
	return ib

def create_monster_builder(data):
	mb = MonsterBuilder()
	mb.name = data.get("name")
	hp = data.get("health")
	mb.health = [hp, hp] if isinstance(hp, int) else hp
	mb.eqSlots = data.get("eqSlots")
	mb.equipementOptions = data.get("equipement")
	mb.effectsOptions = data.get("effects")
	mb.damages = data.get("damage")
	mb.resistances = data.get("resistances")
	mb.damageModifs = data.get("dm_mods")

	dropVars = data.get("drop")
	if dropVars:
		for dv in dropVars:
			drop_list = []
			for drop in dv:
				drop_list.append(drop) # get item builder from global table

			mb.dropVariants.append(drop_list)
	
	return mb


class MonsterBuilder(builder.Builder):
	def __init__(self):
		self.name = ""
		self.health = [100, 100]
		self.eqSlots = []
		self.equipementOptions = []
		self.effectsOptions = []
		self.damages = []
		self.resistances = []
		self.damageModifs = []
		self.dropVariants = []

	def build(self):
		m = monster.Monster()
		m.name = name
		m.health = random.randrange(self.health[0], self.health[1])

		for es in self.eqSlots:
			m.eqSlots.append(es)

		eqOpt = builder.get_random_element(self.equipementOptions)
		if eqOpt:
			for opt in eqOpt:
				m.equip(opt.build())

		for d in self.damages:
			m.damageList.append(d.build())
		for dm in self.damageModifs:
			m.damageModificators.append(dm.build())
		for r in self.resistances:
			m.resistances.append(r.build())

		for dv in get_random_element(self.dropVariants):
			m.drop.append(dv.build())

		return m



def load_monsters(monsters_list):
	pass

def load_monster(file):
	pass

import location

def get_monster_builder(BName):
	return None

import globaldata

def create_location(data):
	loc = location.Location()
	loc.name = data.get("name")
	loc.size = data.get("size")
	sv_list = data.get("monsters")
	spawn_vars = []
	for sv in sv_list:
		spawn_var = []
		for MSParams in sv:
			ms = location.MonsterSpawn()
			ms.amont = MSParams["amount"]
			ms.monsterB = globaldata.MONSTERS.get(MSParams["name"])
			spawn_var.append(ms)
		spawn_vars.append(spawn_var)
	# loc.spawn_vars = 

def load_all_items(data):
	for i in data.get("to_load"):
		filename = i
		d = get_data(f"data/items/{filename}.json")
		ib = create_item_builder(d)
		globaldata.ITEMS.add(filename, ib)

def load_all_monsters(data):
	for i in data.get("to_load"):
		filename = i
		d = get_data(f"data/monsters/{filename}.json")
		ib = create_monster_builder(d)
		globaldata.MONSTERS.add(filename, ib)

def load_all_locations(data):
	for i in data.get("to_load"):
		filename = i
		d = get_data(f"data/locations/{filename}.json")
		l = create_location(d)
		globaldata.LOCATIONS.add(filename, l)