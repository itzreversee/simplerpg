# from lib.libentity import player

from lib.libsave import *
from lib.libentity import *
from lib.randomthings import *

import time, sys

clearConsole()

print("simpleRPG. version: "+ game.version +' '+game.isStable() +" (runtime : "+sys.argv[0]+" )")
time.sleep(1.5)

maciek = basePlayer(
    'Maciek', 0, # name, location
    100, 100, 100, 1, 1, # hp, maxhp, basemaxhp, basehpregen, hpregen
    200, 200, 8, 200, 3, # mana, maxmana, manaregen, basemana, basemanaregen
    3, [FireSpell, CurseSpell, HealSpell], [], # maxitems, inventory, items
    250, 0, 1, 100, # gold, exp, level, nextlevel
    False, 0, 6) # isEnemy, curseLeft, curseId

smanager.save("s0.pkl", maciek)
print("")