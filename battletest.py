
from lib.libsave import *
from lib.libbattle import *
from lib.libentity import *
from lib.randomthings import *
import time, sys

clearConsole()

print("simpleRPG. version: "+ game.version +' '+game.isStable() +" (runtime : " + sys.argv[0] + ") ")
time.sleep(0.5)

def game():
    player = smanager.load("s0.pkl")
    battle(player, villageEnemy.goldmonster)
    
game()
