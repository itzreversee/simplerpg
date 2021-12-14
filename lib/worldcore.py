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
        if (menuinput) == 1: sleep(p) 
        if (menuinput) == 2: print("you have exited the village."); time.sleep(2); exit()
    cmenu = 'village';  

def sleep(p):
    inInn = True
    cmenu = 'inn'
    while inInn:
        clearConsole()
        drawBasicWorldMenu(p, 'Inn')
        if (cmenu) == 'inn': 
            drawInnMenu(); (menuinput) = getUserInput()
            if (menuinput) == 0: cmenu = 'inn_sleep'; continue;
            if (menuinput) == 1: innEvent(p, 4); continue;
            if (menuinput) == 2: cmenu = 'village'; break;
            if (menuinput) == 4: cmenu = 'village'; break;
            cmenu = 'inn'
        
        if (cmenu) == "inn_sleep":
            drawSleepMenu()
            (menuinput) = getUserInput()
            if (menuinput) == 0: innEvent(p, 0)
            if (menuinput) == 1: innEvent(p, 1)
            if (menuinput) == 2: innEvent(p, 3)
            if (menuinput) == 4: cmenu = 'inn'; continue;
            cmenu = 'inn_sleep'
        
        else: break;

def innEvent(p, type):
    if (p.hp >= p.maxhp) or (p.mana >= p.maxmana): print("\nYou are already at max stats!"); getch(); return;

    if type == 0: # NORMAL SLEEP ( FOR SMALL VILLAGE ) ( 20 GOLD )
        if (p.gold < 20): print("\nYou don't have enough gold!"); return;
        print("\nYou took a nap!")
        print(" +3EXP")
        print(" +MAX HP")
        print(" +MAX MANA")
        p.gold -= 20; p.exp += 3; p.hp = p.maxhp; p.mana = p.maxmana;

    if type == 1: # PREMIUM SLEEP ( 50 GOLD )
        if (p.gold < 50): print("\nYou don't have enough gold!"); return;
        print("\nYou spent night in this inn!")
        print(" +5EXP")
        print(" +MAX HP  +20 temporary")
        print(" +MAX MANA")
        p.gold -= 50; p.exp += 5; p.hp = p.maxhp + 20; p.mana = p.maxmana;

    if type == 3: # PREMIUM SLEEP + NORMAL BREAKFAST ( 75 GOLD )
        if (p.gold < 75): print("\nYou don't have enough gold!"); return;
        print("\nYou spent night in this inn, with breakfast!")
        print(" +10EXP")
        print(" +MAX HP  +20 temporary")
        print(" +MAX MANA  +30 temporary")
        p.gold -= 75; p.exp += 10; p.hp = p.maxhp + 20; p.mana = p.maxmana + 30;
    
    if type == 4: # NORMAL BREAKFAST ( 35 GOLD )
        if (p.gold) < 35: print("\nYou don't have enough gold!"); return;
        print("\nYou have eaten breakfast!")
        print(" +5EXP")
        print(" +MAX HP")
        print(" +MAX MANA  +30 temporary")
        p.gold -= 35; p.exp += 5; p.hp = p.maxhp; p.mana = p.maxmana + 30;

    # WAIT FOR PLAYER
    print("\nPress any key to continue...");  time.sleep(0.75); getch()  

    global ssave; reload(ssave, p)
    global seed; seed += 200 # FOR EVERY SLEEP CHANGE SEED!
    cmenu = 'village'; return;

def shop(p): # SHOP DISPLAY FUNCTION
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
        else: break;
        cmenu = 'shop';  

def buy(p, item): # BUY MENU
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
    
    # WAIT FOR PLAYER
    print("\nPress any key to continue...");  time.sleep(0.75); getch()  


def getShopStock(count): # GET SHOP STOCK
    global seed;
    
    tseed = seed
    itempool = [manaBag, healthNecklace]
    items = []
    for _ in range(count):
        tseed *= 16
        random.seed(tseed); 
        items.append(itempool[random.randint(0,len(itempool) -1)])
    return(items)