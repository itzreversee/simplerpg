import time
import os

def notImplemented(f = ''):
    if (f) == '': print("not implemented")
    else: print(f + ' is not implemented')
    time.sleep(1)

    return()


def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'): 
        command = 'cls'
    os.system(command)

class game():
    version = '2.2a'
    stable = False

    def isStable():
        if (game.stable) == False: return('-unstable')
        if (game.stable) == True: return('-stable')
