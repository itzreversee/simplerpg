
from lib.libsave import *
from lib.libinput import getch
from lib.randomthings import *
from lib.console import *
import time, sys, os, json

clearConsole()

out(f"simpleRPG. version: "+ game.version + game.isStable() +"(runtime : " + sys.argv[0] + ")")
time.sleep(1.5)

# create default save file if not found
if not (os.path.isfile("s0.pkl")) or not os.path.isfile("s0_seed.pkl") or not os.path.isfile("s0_sstock.pkl"):
    from new_save import createDefaultSaveFile
    createDefaultSaveFile()

if game.debugPrints: print("\nLoading default save file: \"s0.pkl\"")
player = smanager.load("s0.pkl") # load player save data to local variable

if game.enforceModules == True: # if game modules are enforced in lib/randomthings.py
    install_action(game.enforcedModulesList)

def settings(): # settings menu
    while True:
        out("\nSettings:")
        out(" - 1 - Delete save file", 'green')
        out(" - q - Restart", 'green')
        a = getch()
        if a == "q": exit();
        if a == "1":
            os.remove('s0_seed.pkl')
            os.remove('s0_sstock.pkl')
            os.remove('s0.pkl')
            out("\nSave file deleted!", "red")
            exit()

def mega_reload():
    import sys
    import lib.console; import lib.libbattle; import lib.libdraw; import lib.libentity; import lib.libinput; import lib.libmagic; import lib.libsave; import lib.randomthings; import lib.worldcore
    del sys.modules['lib.console']; del sys.modules['lib.libbattle']; del sys.modules['lib.libdraw']
    del sys.modules['lib.libentity']; del sys.modules['lib.libinput']; del sys.modules['lib.libmagic']
    del sys.modules['lib.libsave']; del sys.modules['lib.randomthings']; del sys.modules['lib.worldcore']
    # import all the essential libraries
    from lib.console import out, list
    from lib.libinput import getch
    from lib.libsave import smanager
    from lib.randomthings import install_action, whatOS, clearConsole, whatOS, game
    return True

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
    if game.debugPrints: out("\nLoading scenario: "+scenario, 'green') # print debug info if specified in lib/randomthings.py
    sys.path.insert(1, 'scenarios/'+scenario[:len(scenario) - c]+'/') # inster path of scenario to sys.path
    from scenario import a # import scenario as if it was in same folder, because specified in sys.path
    status = a.game() # run scenario - class "a" function "game"
    return status

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

    out("\nPress i for settings", 'white') # print settings tip
    
    spp = pager.getPage(scenarios, page_id)  # get page of scenarios
    out("Scenarios:\n", 'white')
    
    for i in range(len(spp)): # iterate through scenarios
        name = parseGameScenario(spp[i])['name'] # get scenario name
        description = parseGameScenario(spp[i])['description'] # get scenario description
        name_color = parseGameScenario(spp[i])['name_color'] # get scenario name color
        description_color = parseGameScenario(spp[i])['description_color'] # get scenario description color
        out(f"  {i+1}. {name}", name_color) # print scenario name
        out(f"\t{description}", description_color) # print scenario name
    if enablePages: # IF ENABLED PAGES
        out(f"\nPage {page_id+1}/{page_ids+1}") # print page info
        out("Use w/e to change pages.", 'green') # print page info

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
        status = loadGameScenario(spp[menuinput-1]) # load scenario
        input('Scenario exited: ' + str(status)) # wait for enter if scenario does not exit already


