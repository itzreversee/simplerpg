from ast import parse
from lib.libsave import *
from lib.libinput import *
from lib.randomthings import *
import time, sys, os

clearConsole()

print("simpleRPG. version: "+ game.version + game.isStable() +" (runtime : " + sys.argv[0] + ")")
time.sleep(1.5)

if not (os.path.isfile("s0.pkl")) or not os.path.isfile("s0_seed.pkl") or not os.path.isfile("s0_sstock.pkl"):
    from new_save import createDefaultSaveFile
    createDefaultSaveFile()

print("\nLoading default save file: \"s0.pkl\"")
player = smanager.load("s0.pkl")
time.sleep(0.2); 

if game.enforceModules == True:
    import importlib.util
    modules = ['climage'] # modules required 
    nomod = False 

    for m in modules:
        if (importlib.util.find_spec(m) == None):
            nomod = True

    if nomod: # install if not found
        print("Hey! In order to play srpg, you need these modules!")
        for m in modules:
            print(" - "+m)
        time.sleep(0.1); print("Do you want to install it now? (q/*)")
        a = getUserInput();
        if a == 0: 
            time.sleep(0.3)
            for m in modules:
                install(m)
            print("\nDone! Restart the game!")
            exit();
        else: 
            print("See ya!")
            input(); exit()

def settings():
    while True:
        print("\nSettings:")
        print(" - 1 - Delete save file")
        print(" - 2 - Launch test room")
        print(" - q - Exit")
        a = getch()
        if a == "q": break;
        if a == "1":
            os.remove('s0_seed.pkl')
            os.remove('s0_sstock.pkl')
            os.remove('s0.pkl')
            print("\nSave file deleted!")
            exit()
        if a == "2":
            from lib.worldcore import fate
            fate.helimantainosifarikanounpata()
        if a == "f" and os.path.exists("fate"):
            print("decide about your own life")

def scanGameScenarios():
    scenarios = []
    f = None
    path = 'scenarios/'
    dirs = os.listdir(path)
    for d in dirs:
        files = os.listdir("scenarios/"+d+"/")
        for f in files:
            if f.endswith('.json'):
                scenarios.append(f)
    return scenarios

def parseGameScenario(scenario):
    import json
    j = open("scenarios/"+scenario[:len(scenario) -4]+"/"+scenario)
    data = json.load(j)
    return data

def loadGameScenario(scenario):
    print(scenario)
    sys.path.insert(1, 'scenarios/'+scenario[:len(scenario) - 4]+'/')
    from scenario import a
    a.game()

while True: 
    #clearConsole()
    if "climage" in sys.modules: print(climage.convert('assets/srpgmini.png', is_unicode=True))  # logo 

    scenarios = scanGameScenarios()
    print("\nPress i for settings")
    print("Scenarios:")
    for i in range(len(scenarios)):
        name = parseGameScenario(scenarios[i])['name']
        print(f"  {i+1}. {name}")

    time.sleep(0.2);

    (menuinput) = getch() # getch, so dynamic type
    if (menuinput) == 4: continue
    if (menuinput) == 'q': break
    if (menuinput) == 'i': settings()
    maxPick = len(scenarios)
    #check if menuinput is int
    try: menuinput = int(menuinput)
    except ValueError: continue

    if menuinput > maxPick or menuinput < 1: continue
    else: 
        loadGameScenario(scenarios[menuinput-1])
        input("end")


