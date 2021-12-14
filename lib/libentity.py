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

class basePlayer(object):
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
    
    name = "Maciek"
    location = 0

    hp = 100
    maxhp = 100
    basemaxhp = 100
    basehpregen = 1
    hpregen = 1

    mana = 225
    maxmana = 2255
    manaregen = 8
    basemana = 200
    basemanaregen = 3

    maxitems = 3
    inventory = [FireSpell, CurseSpell, HealSpell]
    items = [manaBag, manaBag, healthNecklace]
    
    gold = 250
    exp = 2137
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