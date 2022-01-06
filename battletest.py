
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
    battleresult = battle(player, dungeonEnemy.stonemonster)
    if battleresult == 0:
        print("you lost")
    elif battleresult == 1:
        print("you won")
    elif battleresult == 2:
        print("you fleed")
    elif battleresult == 3:
        print("your enemy fleed")        

    
game()
