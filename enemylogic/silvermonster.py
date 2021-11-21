import random
from lib.libbattle import *

class entityLogic(): 
    location = 'all',
    rarity = 'common',
    rarityint = 15
    killexp = 25,
    enemylevel = 3

def enemyRound(player, me):
    while True:
        if (me.hp <= 20):
            if (me.mana) >= 25:
                x = random.randint(0,2)
                if (x) >= 1: return(me, player, 2)
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
        if (x.even()): return(me, player, 0); break
        if (x.odd()): return(me, player, 1); break
    