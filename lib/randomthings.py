import time
import os

def notImplemented(f = ''):
    if (f) == '': print("not implemented")
    else: print(f + ' is not implemented')
    time.sleep(1)

    return()

def install(pkg):
    import sys, subprocess
    print(f" Installing - {pkg}")
    subprocess.check_call([sys.executable, "-m", "pip", "install", pkg]); time.sleep(0.1);

def install_action(modules, norestart = False):
    import importlib.util # import module importlib.uil
    from lib.libinput import getUserInput
    import sys
    if modules == []:
        print("\nNo modules specified")
        return
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
            if not norestart:
                print("Restart")
                exit()
        else: 
            print("See ya!")
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
    version = '2.3'
    stable = True
    debugPrints = False
    enforceModules = True
    enforcedModulesList = ['climage']

    def isStable():
        if (game.stable) == False: return('-unstable')
        if (game.stable) == True: return('-stable')
