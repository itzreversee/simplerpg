from lib.libdraw import *
from lib.libinput import *
from lib.randomthings import clearConsole, notImplemented
from assets.items import *

import time, random

def world(p):
    if (p).location == 'village': village(p);

def village(p):
    inVillage = True
    cmenu = 'village'
    while inVillage:
        clearConsole()
        if (p.location != 'village'): inVillage = False; break

        updateStats(p)

        drawBasicWorldMenu(p)
        if (cmenu) == 'village':
                drawWorldMenu()
                (menuinput) = getUserInput()
                if (menuinput) == 0: shop(p)
                if (menuinput) == 1: notImplemented('sleep(p)')
                if (menuinput) == 2: print("you have exited the village."); exit()
        cmenu = 'village';  

def updateStats(p):
    print('placeholder')

def shop(p):
    inShop = True
    cmenu = 'shop'
    while inShop:
        clearConsole()
        if (p.location != 'village'): inVillage = False; break

        updateStats(p)

        drawBasicWorldMenu(p)
        if (cmenu) == 'shop':
                drawShopMenu(p, shopObject)
                (menuinput) = getUserInput()
                if (menuinput) == 0: shop(p)
                if (menuinput) == 1: notImplemented('sleep(p)')
                if (menuinput) == 2: print("you have exited the village."); exit()
                if (menuinput) == 4: inShop = False; cmenu = 'village'; break;
        cmenu = 'shop';  
    
class shopObject():
    
    itempool = [manaBag, healthNecklace]
    print(len(itempool))

    def getStock():
        for i in range(3):
            #return(shopObject.itempool[random.randint(0, shopObject.itempool.count-1)])
            print('a')