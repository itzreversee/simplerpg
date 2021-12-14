
# from lib.libentity import player

from lib.libsave import *
from lib.worldcore import *
from lib.libentity import *
from lib.randomthings import *
import time

clearConsole()

maciek = basePlayer('Maciek', 0, 100, 100, 100, 1, 1, 225, 2255, 8, 200, 3, 3, [FireSpell, CurseSpell, HealSpell], [manaBag, manaBag, healthNecklace], 250, 120, 1, 100, False, 0, 6)
print("simpleRPG. version: "+ game.version +' '+game.isStable() +" (Village Test)")
time.sleep(1.5)

def game():
    smanager.save("s0.pkl", maciek)
    world("s0.pkl")

game()
