from lib.libentity import checkStats
from lib.libdraw import *
from lib.libinput import *
from lib.randomthings import clearConsole, notImplemented
from assets.items import *

from lib.libsave import *

import time

def world(save):
    while True:
        p = smanager.load(save)
        smanager.save(save, checkStats(p)); p = smanager.load(save)
        if (p).location == 0: smallVillage(p);

def smallVillage(p):
    cmenu = 'village'
    clearConsole()
    drawBasicWorldMenu(p)
    if (cmenu) == 'village':
        drawWorldMenu()
        (menuinput) = getUserInput()
        if (menuinput) == 0: shop(p, getShopStock())
        if (menuinput) == 1: notImplemented('sleep(p)')
        if (menuinput) == 2: print("you have exited the village."); time.sleep(2); exit()
    cmenu = 'village';  

def updateStats(p, save):
    a = checkStats(p)
    smanager.save(save, a)

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
        break;
    
class shopObject():
    
    itempool = [manaBag, healthNecklace]
    print(len(itempool))

    def getStock():
        for i in range(3):
            #return(shopObject.itempool[random.randint(0, shopObject.itempool.count-1)])
            print('a')