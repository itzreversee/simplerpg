import random
from lib.libbattle import *

def getEasyAi(p, m):
    # get entity spells
    spells = []
    for i in range(len(m.inventory)): 
        spells.append(m.inventory[i])

    for i in range(len(spells)):
        if spells[i].cost > m.mana : return 9 # skip round 
        else: 
            if spells[i].type == 'damage' or 'curse':
                if spells[i].value >= p.hp: return i
            elif spells[i].type == 'heal': 
                if p.hp >= p.hp/3: return 9  # skip round
                if p.hp <= p.hp/4: return i
            else: 
                if m.hp <= m.hp/5: return 8
                return random.randint(0, len(spells)-1)


def getNormalAi(p, m):
    # get entity spells
    spells = []
    for i in range(len(m.inventory)): 
        spells.append(m.inventory[i])
    
    for i in range(len(spells)):
        if spells[i].cost > m.mana : return 9 # skip round 
        else: 
            if spells[i].type == 'damage' or 'curse':
                if spells[i].value >= p.hp: return i
                if spells[i].value >= p.hp/2 : return i 
                if spells[i].value < p.hp/2: return i 
            elif spells[i].type == 'heal': 
                if p.hp >= p.hp/3: return 9  # skip round
                if p.hp <= p.hp/4: return i
            else: 
                return random.randint(0, len(spells)-1)




def enemyRound(player, me): # PREBUILD "AI" FOR SILVER MONSTER, DEPRECATED
    while True:
        if (me.hp <= 20):
            if (me.mana) >= 25:
                x = random.randint(0,6)
                if (x) >= 2: return(me, player, 2)
                else: return(me, player, 1)
                break
            break
        if (player.hp > me.hp): 
            if (me.mana) >= 70:
                x = random.randint(0,2)
                if (x) >= 1: return(me, player, 0)
                else: return(me, player, 1)
                break
            break
        if (player.hp < me.hp): 
            if (me.mana) >= 25:
                x = random.randint(0,6)
                if (x) >= 2: return(me, player, 0)
                else: return(me, player, 1)
                break
            break
        x = random.randint(0,9)
        if (x) == 6: return(me, player, 2)
        if (x % 2 == 0): return(me, player, 0); break
        else: return(me, player, 1); break
    