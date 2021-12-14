
from lib.libmagic import *
from assets.items import *

from lib.randomthings import notImplemented

def drawBasicWorldMenu(p, location):
    print('\n')
    print("| " + p.name + " | " + location)
    bar(p.exp, p.nextlevel, ' EXP  |', '| LEVEL - ' + str(p.level) + ', EXP until next LEVEL '+ str(p.nextlevel) + ', GOLD - ' + str(p.gold)); print("")
    bar(p.hp, p.maxhp, ' HP   |', '/ ' + str(p.maxhp) + ' | REGEN - ' + str(p.hpregen) ); print("")
    bar(p.mana, p.maxmana, ' MANA |', '/ ' + str(p.maxmana) + ' | REGEN - ' + str(p.manaregen) ); print("")

    print("\nSpells:")
    for i in range(len(p.inventory)):
        print(" "+eval(p.inventory[i].hardid).name + ', cost: ' + str(eval(p.inventory[i].hardid).cost) + ' mana')
   
    print("\nItems:")
    for i in range(len(p.items)):
        print(" "+eval(p.items[i].hardid).inGameName + ', level: ' + str(eval(p.items[i].hardid).level))
   

def drawWorldMenu():
    print("\nWhat to do?")
    print(" q - shop ")
    print(" w - sleep")
    print(" e - exit village")
    
    return('village') # current menu

def drawShopMenu(p, s):
    print("\nWhat to buy? ")
    for i in range(3):
       if (i) == 0: pkey = 'q - '
       if (i) == 1: pkey = 'w - '
       if (i) == 2: pkey = 'e - '
       print(" "+ pkey + str(s[i].inGameName) + ', rarity: ' + str(s[i].level) + ', price: ' + str(s[i].cost))
    
    return('shop') # current menu

def drawBasicBattleMenu(player, enemy, rounds): 
    print('\n')
    print("| " + player.name + " | vs | " + enemy.name + " (" + str(enemy.hp) + " HP) | ROUND " + str(rounds))
    bar(player.hp, player.maxhp, ' HP   |', '| REGEN - ' + str(player.hpregen) ); print("")
    bar(player.mana, player.maxmana, ' MANA |', '| REGEN - ' + str(player.manaregen) ); print("")

def drawBattleMenu():
    print("\nWhat to do?")
    print(" q - flee ")
    print(" w - spells")
    print(" e - skip round")
    
    return('battle') # current menu
  

def drawSpellMenu(player):
    print("\nYour Spells: ")
    for i in range(len(player.inventory)):
        if (i) == 0: pkey = 'q - '
        if (i) == 1: pkey = 'w - '
        if (i) == 2: pkey = 'e - '
        print(pkey + eval(player.inventory[i].hardid).name + ', cost: ' + str(eval(player.inventory[i].hardid).cost) + ' mana, type: '+ str(eval(player.inventory[i].hardid).type) + ', value: ' + str(eval(player.inventory[i].hardid).value))
   

    return('spell') # current menu

def printItemInfo(stats):
    if stats[0] == 0: sprefix = [" + MAX MANA: ", " + MANA REGEN: "]
    if stats[0] == 1: sprefix = [" + MAX HP: ", " + HP REGEN: "]
    print(" Stats: ")
    print("  Description: " + stats[1])
    for i in range(len(sprefix)):
        a = i + 4; print(" {}{}".format(sprefix[i], stats[a]))
    print("  Rarity: " + str(stats[2]))
    print("  Level: " + str(stats[3]))
    print(" Do you want to buy this item? (q/*) ")

# copied from http://stackoverflow.com/questions/3173320/text-progress-bar-in-the-console

def bar(iteration, total, prefix = ' |', suffix = '| ', ):
    decimals = 1
    length = 20
    fill = '█'
    printEnd = "\r"
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print(f'\r{prefix} |{bar}| {percent}% ({iteration}) {suffix}', end = printEnd)
