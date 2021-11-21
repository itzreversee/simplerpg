from lib.libmagic import * 
from assets.items import *

class player():
    name = "Maciek"
    location = "village"

    hp = 100
    maxhp = 100
    basemaxhp = 100
    basehpregen = 1
    hpregen = 1

    mana = 225
    maxmana = 225
    manaregen = 8
    basemana = 200
    basemanaregen = 3

    inventory = [FireSpell, CurseSpell, HealSpell]
    items = [manaBag]
    
    gold = 250
    exp = 75
    level = 1
    nextlevel = 100

    isEnemy = False
    curseLeft = 0
    curseId = 6


class silvermonster():
    name = "Silver Monster"
    id = 1

    hp = 80
    maxhp = 85
    hpregen = 2

    mana = 150
    maxmana = 250
    manaregen = 20

    inventory = [IceSpell, AirSpell, HealSpell]
    isEnemy = True
    curseLeft = 0
    curseId = 6