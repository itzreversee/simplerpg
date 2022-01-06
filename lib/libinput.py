# modified version of librps, original and remix made by reversee

from sys import platform
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
    elif (z.startswith("t") or z.startswith("T")): return 5 
    elif (z.startswith("y") or z.startswith("Y")): return 6 
    elif (z.startswith("X") or z.startswith("Z")): exit()
    else: return(3)

def getch():
    if platform == "win32":
        import msvcrt
        try: 
            usi = msvcrt.getch().decode('ASCII')
            return(usi)
        except UnicodeDecodeError:
            return(4) 
    else: 
        
        # https://gist.github.com/sidequestboy/9205174

        import sys, tty, termios 
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch

