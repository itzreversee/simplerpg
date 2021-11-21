# modified version of librps, original and remix made by reversee

import random

global userinput, cpuinput

def getUserInput():
    userinput = 3
    while (userinput) == 3:
        userinput = formatInput(input())
    return(userinput)

def getCPUinput(): 
    return(random.randint(0, 2))


def formatInput(input):
    z = str(input)

    if (z.startswith("q") or z.startswith("Q")): return 0
    elif (z.startswith("w") or z.startswith("W")): return 1
    elif (z.startswith("e") or z.startswith("E")): return 2
    elif (z.startswith("r") or z.startswith("R")): return 4
    else: return(3)


def printcpu(cpu):
    if (cpu) == 0: return("CPU choose ")
    if (cpu) == 1: return("CPU choose ")
    if (cpu) == 2: return("CPU choose ")
    
def printplr(you):
    if (you) == 0: return("YOU choose ")
    if (you) == 1: return("YOU choose ")
    if (you) == 2: return("YOU choose ")
    
