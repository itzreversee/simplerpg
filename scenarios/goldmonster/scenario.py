
from lib.libsave import *
from lib.libbattle import *
from lib.libentity import villageEnemy
import sys

#clearConsole()

class a:
    def game():
        out(" loading default save file - s0.pkl")
        player = smanager.load("s0.pkl")
        del sys.modules['lib.libentity']
        from lib.libentity import villageEnemy
        return(battle(player, villageEnemy.goldmonster))
    
