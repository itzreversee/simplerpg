import random
from lib.libbattle import *

def getEasyAi(p, m):
    # get entity spells
    spells = []
    rt = -1
    for i in range(len(m.inventory)): 
        spells.append(m.inventory[i])
    i = -1

    while True:
        i += 1
        if i >= len(spells): break; 
        
        if spells[i].cost > m.mana : rt = 9; break; # skip round 
        elif m.hp < m.hp/8:
            x = random.randint(0, 2)
            if x == 1: return 8; break;
        else: 
            if spells[i].type == 'damage' or 'curse':
                if spells[i].value >= p.hp: rt = i; break
            elif spells[i].type == 'heal': 
                if p.hp >= p.hp/3: rt = 9; break  # skip round
                if p.hp <= p.hp/4: rt = i; break;
    if rt == -1: rt = random.randint(0, len(spells)-1)
    return rt;

def getNormalAi(p, m):
    # get entity spells
    spells = []
    rt = -1
    for i in range(len(m.inventory)): 
        spells.append(m.inventory[i])

    i = -1
    while True:
        i += 1
        if i >= len(spells): break; 
        if spells[i].cost > m.mana : rt = 9; break; # skip round 
        else: 
            if spells[i].type == 'damage' or 'curse':
                if spells[i].value >= p.hp : rt = i; break
                elif spells[i].value >= p.hp/2 : rt = i; break
                elif spells[i].value >= p.hp/6 : rt = i; break
            elif spells[i].type == 'heal': 
                if p.hp >= p.hp/3 : rt = 9; break;  # skip round
                if p.hp <= p.hp/4 : rt = i; break;

    if rt == -1: rt = random.randint(0, len(spells)-1)
    return rt;

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
    