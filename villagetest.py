
from lib.worldcore import *
from lib.libentity import *
from lib.randomthings import *
import time

clearConsole()

print("simpleRPG. version: "+ game.version +' '+game.isStable() +" (Village Test)")

time.sleep(1.5)

def game():
    world(player)
    

game()
