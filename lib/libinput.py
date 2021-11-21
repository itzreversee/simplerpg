# modified version of librps, original and remix made by reversee

import random

global userinput, cpuinput

def getUserInput():
    userinput = 3
    while (userinput) == 3:
        userinput = formatInput(input())
    return(userinput)

def formatInput(input):
    z = str(input)

    if (z.startswith("q") or z.startswith("Q")): return 0
    elif (z.startswith("w") or z.startswith("W")): return 1
    elif (z.startswith("e") or z.startswith("E")): return 2
    elif (z.startswith("r") or z.startswith("R")): return 4
    else: return(3)

