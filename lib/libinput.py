# modified version of librps, original and remix made by reversee

import random

global userinput, cpuinput

def getUserInput():
    userinput = 3
    while (userinput) == 3:
        userinput = formatInput(getch())
    return(userinput)

def formatInput(input):
    z = str(input)

    if (z.startswith("q") or z.startswith("Q")): return 0
    elif (z.startswith("w") or z.startswith("W")): return 1
    elif (z.startswith("e") or z.startswith("E")): return 2
    elif (z.startswith("r") or z.startswith("R")): return 4
    elif (z.startswith("X") or z.startswith("Z")): exit()
    else: return(3)

# got code from https://code.activestate.com/recipes/134892/
class _Getch:
    def __init__(self):
        try:
            self.impl = _GetchWindows()
        except ImportError:
            self.impl = _GetchUnix()

    def __call__(self): return self.impl()


class _GetchUnix:
    def __init__(self):
        import tty, sys

    def __call__(self):
        import sys, tty, termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch


class _GetchWindows:
    def __init__(self):
        import msvcrt

    def __call__(self):
        import msvcrt
        return msvcrt.getch()


getch = _Getch()
