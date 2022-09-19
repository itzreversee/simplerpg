
from lib.console import *

import time
import os

def notImplemented(f = ''):
    if (f) == '': out('not implemented yet', color_='red', decoration_='bold')
    else: print(f + ' is not implemented', color_='red', decoration_='bold')
    time.sleep(1)

    return()

def install(pkg):
    import sys, subprocess
    out(f" Installing - {pkg}", color_='green', decoration_='bold')
    subprocess.check_call([sys.executable, "-m", "pip", "install", pkg]); time.sleep(0.1);

def install_action(modules, norestart = False):
    import importlib.util # import module importlib.uil
    from lib.libinput import getUserInput
    import sys
    if modules == []:
        out("\nNo modules specified", color_='red', decoration_='bold')
        return
    nomod = False 

    for m in modules:   # iterate through modules
        if (importlib.util.find_spec(m) == None): # if module not found
            nomod = True # set nomod to true

    if nomod: # if nomod is true
        out("Hey! In order to play srpg, you need these modules!", color_='green')
        list(modules, color_='green')
        out("Do you want to install it now? (q/*)", color_='green')
        a = getUserInput(); # get user input
        if a == 0: 
            for m in modules: # iterate through modules
                install(m) # install module m
            if not norestart:
                out("Restart", decoration_='bold')
                exit()
        else: 
            out("See ya!")
            input(); exit()

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'): 
        command = 'cls'
    os.system(command)

def whatOS():
    if os.name in ('nt', 'dos'):
        return('win')
    else: return('unix')

class game():
    version = '2.2'
    stable = True
    debugPrints = False
    enforceModules = True
    enforcedModulesList = ['requests']

    def isStable():
        if (game.stable) == False: return('-unstable')
        if (game.stable) == True: return('-stable')
