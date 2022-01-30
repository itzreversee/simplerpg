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
    version = '2.2a'
    stable = True
    enforceModules = False

    def isStable():
        if (game.stable) == False: return('-unstable')
        if (game.stable) == True: return('-stable')
