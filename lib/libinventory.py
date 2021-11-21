def itemname(invid):
    if invid == 0: return('Basic Sword')
    if invid == 1: return('Basic Armor')
    if invid == 2: return('Fire Spell')
    if invid == 3: return('Ice Spell')
    if invid == 4: return('Air Spell')
    if invid == 5: return('Heal Spell')
    if invid == 6: return('Curse Spell')

def manacost(invid):
    if invid == 2: return(20)
    if invid == 3: return(20)
    if invid == 4: return(15)
    if invid == 5: return(25)
    if invid == 6: return(40)

def translateToMagic(invid):
    if invid == 2: return('FireSpell')
    if invid == 3: return('IceSpell')
    if invid == 4: return('AirSpell')
    if invid == 5: return('HealSpell')
    if invid == 6: return('CurseSpell')