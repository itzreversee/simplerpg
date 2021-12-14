
# from lib.libentity import player

from lib.libsave import *
from lib.worldcore import *
from lib.libentity import *
from lib.randomthings import *
import time

clearConsole()

maciek = basePlayer('Maciek', 0, 100, 100, 100, 1, 1, 200, 200, 8, 200, 3, 3, [FireSpell, CurseSpell, HealSpell], [], 250, 0, 1, 100, False, 0, 6)
print("simpleRPG. version: "+ game.version +' '+game.isStable() +" (Village Test)")
time.sleep(1.5)

def game():
    smanager.save("s0.pkl", maciek)
    world("s0.pkl", random.randint(0,99999999))

game()
