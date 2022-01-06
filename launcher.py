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

if game.enforceModules == True:

    modules = ['climage'] # modules required 
    nomod = False 

    try: # check for modules
        import climage
        # from playsound import playsound 
    except ModuleNotFoundError:
        nomod = True

    if nomod: # install if not found
        print("Hey! In order to play srpg, you need these things!")
        print(f" - {modules[0]}")
        # print(f" - {modules[1]}")
        time.sleep(0.1); print("Do you want to install it now? (q/*)")
        a = getUserInput();
        if a == 0: 
            time.sleep(0.3)
            install(modules[0])
            install(modules[1])
            getUserInput()
        else: 
            print("See ya!")
            input(); exit()

while True: 
    clearConsole()

    if "climage" in sys.modules: print(climage.convert('assets/srpgmini.png', is_unicode=True))  # logo 

    time.sleep(0.2);
    print("\nSelect game preset: ") # presets
    print(" q - Village ")
    print(" w - Battle Scenarios (progress is not saved for now) ")
    (menuinput) = getUserInput()
    if (menuinput) == 0: 
        from village import *
        game()
    if (menuinput) == 1: 
        while True: 
            clearConsole()
            print("\nSelect battle scenario: ")
            print(" q - Silver Monster ")
            print(" w - Golden Monster ")
            print(" e - Stone Monster ")
            (menuinput) = getUserInput()
            if (menuinput) == 0: 
                from scenarios.silvermonster import *
                game()
            if (menuinput) == 1: 
                from scenarios.goldmonster import *
                game()
            if (menuinput) == 2: 
                from scenarios.stonemonster import *
                game()

