from lib.libsave import *
from lib.libinput import *
from lib.randomthings import *
import time, sys

clearConsole()

print("simpleRPG. version: "+ game.version + game.isStable() +" (runtime : " + sys.argv[0] + ")")
time.sleep(1.5)

if not (os.path.isfile("s0.pkl")):
    from new_save import createDefaultSaveFile
    createDefaultSaveFile()

print("\nLoading default save file: \"s0.pkl\"")
player = smanager.load("s0.pkl")
time.sleep(0.2); 

while True:
    clearConsole()
    print("\nSelect game preset: ")
    print(" q - Village ")
    print(" w - Battle (progress is not saved) ")
    (menuinput) = getUserInput()

    if (menuinput) == 0: 
        from village import *
        game()
    if (menuinput) == 1: 
        from battletest import *
        game()
    
    
