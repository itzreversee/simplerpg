
from lib.libbattle import *
from lib.libentity import *
from lib.randomthings import *
import time

clearConsole()
print("Super Basic RPG. version: 1.3_alpha (Battle Test)")
time.sleep(3)

def game():
    isBattleGoing = True
    battle(player, silvermonster)

game()
