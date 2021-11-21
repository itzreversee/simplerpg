
from lib.libbattle import *
from lib.libentity import *
from lib.randomthings import *
import time

clearConsole()


print("simpleRPG. version: "+ game.version +' '+game.isStable() +" (Battle Test)")

time.sleep(1.5)

def game():
    isBattleGoing = True
    battle(player, silvermonster)

game()
