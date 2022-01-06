from lib.libmagic import * 
from assets.items import *

import pickle, time

def checkStats(p):
    
    temp = p.basemana; temp2 = p.basemanaregen
    for i in (p.items):
        if i.type == 0:
            temp += i.value1
            temp2 += i.value2
    p.maxmana = temp; p.manaregen = temp2; 

    temp3 = p.basemaxhp; temp4 = p.basehpregen
    for i in (p.items):
        if i.type == 1:
            temp3 += i.value1
            temp4 += i.value2
    p.maxhp = temp3; p.hpregen = temp4; 
    while p.exp > p.nextlevel:
        p.level += 1;
        p.exp = p.exp - p.nextlevel;
        p.nextlevel *= 2
        print(" LEVEL UP! | LEVEL " + str(p.level) + ", UNTIL NEXT LEVEL: " + str(p.nextlevel - p.exp) + "EXP ")
        time.sleep(2)
    a = p; return a;

class player():
    name = None
    location = None
    hp = None
    maxhp = None
    basemaxhp = None
    basehpregen = None
    hpregen = None
    mana = None
    maxmana = None
    manaregen = None
    basemana = None
    basemanaregen = None
    maxitems = None
    inventory = None
    items = None
    gold = None
    exp = None
    level = None
    nextlevel = None
    isEnemy = None
    curseLeft = None
    curseId = None

class baseEntity(object):
    def __init__(self,name,location,hp,maxhp,basemaxhp,basehpregen,hpregen,mana,maxmana,manaregen,basemana,basemanaregen,maxitems,inventory,items,gold,exp,level,nextlevel,isEnemy,curseLeft,curseId):
        self.name = name
        self.location = location
        self.hp = hp
        self.maxhp = maxhp
        self.basemaxhp = basemaxhp
        self.basehpregen = basehpregen
        self.hpregen = hpregen
        self.mana = mana
        self.maxmana = maxmana
        self.manaregen = manaregen
        self.basemana = basemana
        self.basemanaregen = basemanaregen
        self.maxitems = maxitems
        self.inventory = inventory
        self.items = items
        self.gold = gold
        self.exp = exp
        self.level = level
        self.nextlevel = nextlevel
        self.isEnemy = isEnemy
        self.curseLeft = curseLeft
        self.curseId = curseId

class villageEnemy():
    silvermonster = baseEntity(
    'Silver Monster', 0, # name, location
    80, 80, 80, 2, 2, # hp, maxhp, basemaxhp, basehpregen, hpregen
    150, 250, 20, 250, 20, # mana, maxmana, manaregen, basemana, basemanaregen
    3, [IceSpell, AirSpell], [], # maxitems, inventory, items
    0, 0, 1, 100, # gold, exp, level, nextlevel
    True, 0, 6) # isEnemy, curseLeft, curseId
    
    goldmonster = baseEntity(
    'Golden Monster', 0, # name, location
    120, 120, 120, 1, 1, # hp, maxhp, basemaxhp, basehpregen, hpregen
    120, 120, 4, 120, 4, # mana, maxmana, manaregen, basemana, basemanaregen
    3, [FireSpell, AirSpell, HealSpell], [], # maxitems, inventory, items
    0, 0, 1, 100, # gold, exp, level, nextlevel
    True, 0, 6) # isEnemy, curseLeft, curseId

class dungeonEnemy():
    stonemonster = baseEntity(
    'Stone Monster', 1, # name, location
    60, 60, 60, 0, 0, # hp, maxhp, basemaxhp, basehpregen, hpregen
    80, 80, 10, 80, 10, # mana, maxmana, manaregen, basemana, basemanaregen
    3, [StoneSpell, DirtSpell], [], # maxitems, inventory, items
    0, 0, 1, 100, # gold, exp, level, nextlevel
    True, 0, 6) # isEnemy, curseLeft, curseId