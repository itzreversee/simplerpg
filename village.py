
# from lib.libentity import player

from lib.libsave import *
from lib.worldcore import *
from lib.libentity import *
from lib.randomthings import *
import time

clearConsole()

print("simpleRPG. version: "+ game.version + game.isStable() +" (runtime : village.py)")
time.sleep(1.5)

def game():
    world("s0.pkl", random.randint(0,99999999))

game()
