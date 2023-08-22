import alive
import damage
import item
import effect


def create_poison():
	i = item.Item()
	i.name = "Poison"
	i.description = "Light-green substance. Smells owfull, probably made by some crazy witch!"
	i.isUsable = True
	i.effects.append(EPoison(None))
	return i

def create_quest_item():
	i = item.Item()
	i.name = "Old talisman"
	i.description = "Old wooden talisman covered with cracks and scratches. Looks quite evil!"
	i.slot = alive.EquipementSlot("head")
	i.isProtected = True
	i.isUsable = False
	return i

def create_axe():
	i = item.Item()
	i.name = "Axe"
	i.slot = alive.EquipementSlot("hand")
	i.isUsable = False

	i.effects.append(ECAddPhysDamage(None))

	return i

def create_sword():
	i = item.Item()
	i.name = "Sword"
	i.slot = alive.EquipementSlot("hand")
	i.isUsable = False
	i.effects.append(ECAddPhysDamage(None))

	return i

def create_armor_plate():
	i = item.Item()
	i.name = "Armor Plate"
	i.slot = alive.EquipementSlot("torso")
	i.isUsable = False

	i.effects.append(ECResistance(None))

	return i

def create_ring():
	i = item.Item()
	i.name = "Ring of fire"
	i.slot = alive.EquipementSlot("finger")
	i.effects.append(EAddFireDamage(None))
	i.isUsable = False

	return i



def create_player():
	a = alive.Alive()
	a.name = "Player"
	a.health = 100
	a.experience = 100

	a.eqSlots.append(alive.EquipementSlot("hand"))
	a.eqSlots.append(alive.EquipementSlot("hand"))

	a.eqSlots.append(alive.EquipementSlot("finger"))
	a.eqSlots.append(alive.EquipementSlot("finger"))
	a.eqSlots.append(alive.EquipementSlot("finger"))
	a.eqSlots.append(alive.EquipementSlot("finger"))

	a.eqSlots.append(alive.EquipementSlot("head"))
	a.eqSlots.append(alive.EquipementSlot("torso"))
	a.eqSlots.append(alive.EquipementSlot("legs"))
	
	return a

def create_goblin():
	a = alive.Alive()
	a.name = "Goblin"
	a.maxHealth = 50
	a.health = 50
	a.experience = 100

	a.eqSlots.append(alive.EquipementSlot("hand"))
	a.eqSlots.append(alive.EquipementSlot("hand"))

	a.eqSlots.append(alive.EquipementSlot("finger"))

	a.eqSlots.append(alive.EquipementSlot("head"))
	a.eqSlots.append(alive.EquipementSlot("torso"))
	a.eqSlots.append(alive.EquipementSlot("legs"))

	return a


def print_equipment(e):
	for eq in e.equipment:
		print(eq.name)
	print("-----------------")
	for es in e.eqSlots:
		if es.item == None:
			print(es.name + ": " + "---")
		else:
			print(es.name + ": " + es.item.name)
             
def print_effects(e):
	for ef in e.effects:
		s = "not active"
		if ef.isActive:
			s = "active"
		print(f"{ef.name}({s}): {ef.duration}")



if __name__ == "__main__":
	pl = create_player()
	gb = create_goblin()
	sword_for_player = create_sword()
	pl.equip(sword_for_player)
	pl.equip(create_ring())
	pl.update_effects()
	gb.update_effects()