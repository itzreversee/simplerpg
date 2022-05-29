
from lib.libsave import *
from lib.libinput import *
from lib.randomthings import *
import time, sys, os

clearConsole()

print("simpleRPG. version: "+ game.version + game.isStable() +" (runtime : " + sys.argv[0] + ")")
time.sleep(1.5)

# create default save file if not found
if not (os.path.isfile("s0.pkl")) or not os.path.isfile("s0_seed.pkl") or not os.path.isfile("s0_sstock.pkl"):
    from new_save import createDefaultSaveFile
    createDefaultSaveFile()

if game.debugPrints: print("\nLoading default save file: \"s0.pkl\"")
player = smanager.load("s0.pkl") # load player save data to local variable

if game.enforceModules == True: # if game modules are enforced in lib/randomthings.py
    import importlib.util # import module importlib.uil
    modules = ['climage'] # modules required 
    nomod = False 

    for m in modules:   # iterate through modules
        if (importlib.util.find_spec(m) == None): # if module not found
            nomod = True # set nomod to true

    if nomod: # if nomod is true
        print("Hey! In order to play srpg, you need these modules!")
        for m in modules: # iterate through modules
            print(" - "+m)
        print("Do you want to install it now? (q/*)")
        a = getUserInput(); # get user input
        if a == 0: 
            for m in modules: # iterate through modules
                install(m) # install module m
            print("\nDone! Restart the game!")
            exit();
        else: 
            print("See ya!")
            input(); exit()

def settings(): # settings menu
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
        if a == "2": # ???
            from lib.worldcore import fate
            fate.helimantainosifarikanounpata()
        if a == "f" and os.path.exists("fate"):
            print("decide about your own life")

def scanGameScenarios(): # scan game scenarios
    scenarios = [] 
    f = None
    path = 'scenarios/' # path to scenarios
    dirs = os.listdir(path) # list of directories in path
    for d in dirs: # iterate through directories
        files = os.listdir("scenarios/"+d+"/") # list of files in directory
        for f in files: # iterate through files
            if f.endswith('.json'): # if file is json
                scenarios.append(f) # add file to list
    return scenarios # return list of scenarios

def parseGameScenario(scenario): # parse game scenario
    import json # import json 
    c = 4
    if whatOS() == "unix": c = 5
    j = open("scenarios/"+scenario[:len(scenario) - c]+"/"+scenario) # open scenario
    data = json.load(j) # load json
    return data # return data

def loadGameScenario(scenario): # load game scenario
    c = 4
    if whatOS() == "unix": c = 5
    if game.debugPrints: print("\nLoading scenario: "+scenario) # print debug info if specified in lib/randomthings.py
    sys.path.insert(1, 'scenarios/'+scenario[:len(scenario) - c]+'/') # inster path of scenario to sys.path
    from scenario import a # import scenario as if it was in same folder, because specified in sys.path
    a.game() # run scenario - class "a" function "game"

class pager: # pager class
    def getPage(scenarios, page): # get page
        # put 9 scenarios per page 
        # and return list of scenarios in page
        page +=1 # page starts at 1
        if page == 1: # if page is 1
            spp = scenarios[:9] # get first 9 scenarios
        else: # if page is not 1
            spp = scenarios[(page-1)*9:page*9] # get page scenarios
        return spp # return page


# pages variable
enablePages = None # disable pages
page_id = 0 # page id
page_ids = 0 # page ids

while True: # menu loop
    clearConsole() # clear console
    if "climage" in sys.modules: print(climage.convert('assets/srpgmini.png', is_unicode=True))  # logo  if module climage is installed

    scenarios = scanGameScenarios() # scan scenarios
    if len(scenarios) > 9: # if more than 9 scenarios
        enablePages = True # enable pages
        # get total pages
        page_ids = len(scenarios) // 9 # get total pages

    print("\nPress i for settings") # print settings tip
    
    spp = pager.getPage(scenarios, page_id)  # get page of scenarios
    print("Scenarios:")
    
    for i in range(len(spp)): # iterate through scenarios
        name = parseGameScenario(spp[i])['name'] # get scenario name
        description = parseGameScenario(spp[i])['description']
        print(f"  {i+1}. {name}") # print scenario name
        print(f"\t{description}") # print scenario name
    if enablePages: # IF ENABLED PAGES
        print(f"\nPage {page_id+1}/{page_ids+1}") # print page info
        print("Use w/e to change pages.") # print page info

    (menuinput) = getch() # getch, so dynamic type
    if (menuinput) == 4: continue # if enter is pressed, continue
    if (menuinput) == 'q': break # if q is pressed, break loop
    if (menuinput) == 'i': settings() # if i is pressed, settings menu
    if enablePages: # IF ENABLED PAGES
        if (menuinput) == 'w':  # if w is pressed
                if not page_ids > page_id:  # if page id is not greater than total pages
                    page_id -= 1 # decrease page id
        if (menuinput) == 'e': # if e is pressed
                if not page_ids <= page_id:     # if page id is not greater than total pages
                    page_id += 1 # increase page id

    maxPick = len(scenarios) # max pick
    #check if menuinput is int
    try: menuinput = int(menuinput) # try to convert to int
    except ValueError: continue # if not int, continue

    if menuinput > maxPick or menuinput < 1: continue # if menuinput is not in range, continue
    else: # if menuinput is in range
        loadGameScenario(spp[menuinput-1]) # load scenario
        input() # wait for enter if scenario does not exit already


