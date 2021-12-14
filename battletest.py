
from lib.libsave import *
from lib.libbattle import *
from lib.libentity import silvermonster
from lib.randomthings import *
import time

clearConsole()

maciek = basePlayer('Maciek', 0, 100, 100, 100, 1, 1, 200, 200, 8, 200, 3, 3, [FireSpell, CurseSpell, HealSpell], [], 250, 0, 1, 100, False, 0, 6)
print("simpleRPG. version: "+ game.version +' '+game.isStable() +" (runtime : Battle Test)")
time.sleep(1.5)

def game():
    smanager.save("s_battletest.pkl", maciek)
    player = smanager.load("s_battletest.pkl")
    battle(player, silvermonster)
    print(player.hp)

game()
