import time
import os

def notimplemented():
    print("not implemented")
    time.sleep(1)

    return()


def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'): 
        command = 'cls'
    os.system(command)
