
from lib.libsave import *
from lib.libbattle import *
from lib.libentity import dungeonEnemy
import time, sys

clearConsole()

def game():
    print(" loading default save file - s0.pkl")
    player = smanager.load("s0.pkl")
    return(battle(player, dungeonEnemy.stonemonster))
    
game()
