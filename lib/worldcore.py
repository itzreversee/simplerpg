from lib.libentity import checkStats
from lib.libdraw import *
from lib.libinput import *
from lib.randomthings import clearConsole, notImplemented
from assets.items import *

from lib.libsave import *

import time, random

def world(save, s):
    global seed;
    global ssave;
    ssave = save;
    seed = s
    p = smanager.load(save)
    while True:
        reload(save, p)
        if (p).location == 0: smallVillage(p);
def reload(save, p):
    smanager.save(save, checkStats(p)); p = smanager.load(save)

def smallVillage(p):
    cmenu = 'village'
    clearConsole()
    drawBasicWorldMenu(p, 'Small Village')
    if (cmenu) == 'village':
        drawWorldMenu()
        # for i in range(len(p.items)): print(p.items[i]) # debug
        (menuinput) = getUserInput()
        if (menuinput) == 0: shop(p)
        if (menuinput) == 1: notImplemented('sleep(p)'); global seed; seed += 200
        if (menuinput) == 2: print("you have exited the village."); time.sleep(2); exit()
    cmenu = 'village';  

def shop(p):
    inShop = True
    cmenu = 'shop'
    while inShop:
        clearConsole()
        stock = getShopStock(3)

        drawBasicWorldMenu(p, 'SHOP')
        if (cmenu) == 'shop':
                drawShopMenu(p, stock)
                (menuinput) = getUserInput()
                if (menuinput) == 0: buy(p, stock[0])
                if (menuinput) == 1: buy(p, stock[1])
                if (menuinput) == 2: buy(p, stock[2])
                if (menuinput) == 4: inShop = False; cmenu = 'village'; break;
        cmenu = 'shop';  

def buy(p, item):
    print("\nYou are about to buy: "+item.inGameName)
    print("\n Price: "+str(item.cost))
    itemstats = getItemInfo(item); printItemInfo(itemstats)
    (menuinput) = getUserInput()
    if (menuinput) == 0:
        if len(p.items) >= p.maxitems: print("You can't buy more than " + str(p.maxitems) + " items"); time.sleep(3); return;
        if (item.cost > p.gold): print("You don't have enough gold"); time.sleep(3); return;
        p.gold -= item.cost; p.items.append(item);
        print("You bought " + item.inGameName + "!"); reload(ssave, p);
        print("You bought " + item.inGameName + "!"); reload(ssave, p);
        

def getShopStock(count):
    global seed;
    
    tseed = seed
    itempool = [manaBag, healthNecklace]
    items = []
    for _ in range(count):
        tseed *= 16
        random.seed(tseed); 
        items.append(itempool[random.randint(0,len(itempool) -1)])
    return(items)