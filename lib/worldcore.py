from lib.libentity import checkStats
from lib.libdraw import *
from lib.libinput import *
from lib.randomthings import clearConsole, notImplemented
from lib.console import out
from assets.items import *

from lib.libsave import *

import time, random

def world(save, s):
    global seed;
    global ssave;
    global shopstock;
    ssave = save;
    p = smanager.load(save)
    seed = smanager.load("s0_seed.pkl")
    shopstock = smanager.load("s0_sstock.pkl")
    while True:
        reload(save, p)
        if (p).location == 0: smallVillage(p);

def reload(save, p): smanager.save(save, checkStats(p)); p = smanager.load(save); worldReload();

def worldReload():
    global seed; global shopstock;
    smanager.world.save(seed, shopstock)
    seed = smanager.load("s0_seed.pkl")
    shopstock = smanager.load("s0_sstock.pkl")

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
        if (menuinput) == 2: out("you have exited the village."); time.sleep(2); exit()
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
    if (p.hp >= p.maxhp) and (p.mana >= p.maxmana): out("\nYou are already at max stats!"); getch(); return;

    if type == 0: # NORMAL SLEEP ( FOR SMALL VILLAGE ) ( 20 GOLD )
        if (p.gold < 20): out("\nYou don't have enough gold!"); return;
        out("\nYou took a nap!")
        out(" +3EXP")
        out(" +MAX HP")
        out(" +MAX MANA")
        p.gold -= 20; p.exp += 3; p.hp = p.maxhp; p.mana = p.maxmana;

    if type == 1: # PREMIUM SLEEP ( 50 GOLD )
        if (p.gold < 50): out("\nYou don't have enough gold!"); return;
        out("\nYou spent night in this inn!")
        out(" +5EXP")
        out(" +MAX HP  +20 temporary")
        out(" +MAX MANA")
        p.gold -= 50; p.exp += 5; p.hp = p.maxhp + 20; p.mana = p.maxmana;

    if type == 3: # PREMIUM SLEEP + NORMAL BREAKFAST ( 75 GOLD )
        if (p.gold < 75): out("\nYou don't have enough gold!"); return;
        out("\nYou spent night in this inn, with breakfast!")
        out(" +10EXP")
        out(" +MAX HP  +20 temporary")
        out(" +MAX MANA  +30 temporary")
        p.gold -= 75; p.exp += 10; p.hp = p.maxhp + 20; p.mana = p.maxmana + 30;
    
    if type == 4: # NORMAL BREAKFAST ( 35 GOLD )
        if (p.gold) < 35: out("\nYou don't have enough gold!"); return;
        out("\nYou have eaten breakfast!")
        out(" +5EXP")
        out(" +MAX HP")
        out(" +MAX MANA  +30 temporary")
        p.gold -= 35; p.exp += 5; p.hp = p.maxhp; p.mana = p.maxmana + 30;

    # WAIT FOR PLAYER
    out("\nPress any key to continue...");  time.sleep(0.75); getch()  

    global ssave; reload(ssave, p) # reload
    global seed; seed += 200 # FOR EVERY SLEEP CHANGE SEED!
    getShopStock(3, True); # FORCE REGEN SHOP STOCK
    worldReload() # SAVE WORLD DATA
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
    out("\nYou are about to buy: "+item.inGameName)
    out("\n Price: "+str(item.cost))
    itemstats = getItemInfo(item); printItemInfo(itemstats)
    (menuinput) = getUserInput()
    if (menuinput) == 0:
        if len(p.items) >= p.maxitems: out("You can't buy more than " + str(p.maxitems) + " items"); time.sleep(3); return;
        if (item.cost > p.gold): out("You don't have enough gold"); time.sleep(3); return;
        p.gold -= item.cost; p.items.append(item);
        out("You bought " + item.inGameName + "!"); reload(ssave, p); 
    
    # WAIT FOR PLAYER
    out("\nPress any key to continue...");  time.sleep(0.75); getch()  


def getShopStock(count, force = False): # GET SHOP STOCK
    global seed;
    global shopstock;
    
    tseed = seed
    itempool = [manaBag, healthNecklace] 
    if shopstock == [] or force == True:
        shopstock = []
        for _ in range(count):
            tseed *= 16
            random.seed(tseed); 
            shopstock.append(itempool[random.randint(0,len(itempool) -1)])
    worldReload()
    return(shopstock)