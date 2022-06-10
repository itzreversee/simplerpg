
from lib.libmagic import *
from assets.items import *

from lib.console import out 
from lib.randomthings import notImplemented

def drawBasicWorldMenu(p, location):
    out("| " + p.name + " | " + location)
    bar(p.exp, p.nextlevel, ' EXP  |', '| LEVEL - ' + str(p.level) + ', EXP until next LEVEL '+ str(p.nextlevel) + ', GOLD - ' + str(p.gold)); out("")
    bar(p.hp, p.maxhp, ' HP   |', '/ ' + str(p.maxhp) + ' | REGEN - ' + str(p.hpregen) ); out("")
    bar(p.mana, p.maxmana, ' MANA |', '/ ' + str(p.maxmana) + ' | REGEN - ' + str(p.manaregen) ); out("")

    out("\nSpells:")
    for i in range(len(p.inventory)):
        out(" "+eval(p.inventory[i].hardid).name + ', cost: ' + str(eval(p.inventory[i].hardid).cost) + ' mana')
   
    out("\nItems:")
    for i in range(len(p.items)):
        out(" "+eval(p.items[i].hardid).inGameName + ', level: ' + str(eval(p.items[i].hardid).level))
   

def drawWorldMenu():
    out("\nWhat to do?")
    out(" q - shop ", 'yellow')
    out(" w - sleep", 'green')
    out(" e - exit village")
    
    return('village') # current menu

def drawInnMenu():
    out("\nWhat to do?")
    out(" q - sleep")
    out(" w - breakfast (cost : 35 gold) ")
    out(" e - back to village")

def drawSleepMenu():
    out("\nHow do you want to sleep?")
    out(" q - normal sleep (20 GOLD) ")
    out(" w - premium sleep (50 GOLD) ")
    out(" e - premium sleep + breakfast (75 gold) ")
    out(" r - back")

def drawShopMenu(p, s):
    out("\nWhat to buy? ")
    keys = ['q', 'w', 'e']
    for i in range(3):
       out(" "+ keys[i] + ' - ' + str(s[i].inGameName) + ', rarity: ' + str(s[i].level) + ', price: ' + str(s[i].cost))
    
    return('shop') # current menu

def drawBasicBattleMenu(player, enemy, rounds): 
    out('\n')
    out("| " + player.name + " | vs | " + enemy.name + " (" + str(enemy.hp) + " HP) | ROUND " + str(rounds))
    bar(player.hp, player.maxhp, ' HP   |', '| REGEN - ' + str(player.hpregen) ); out("")
    bar(player.mana, player.maxmana, ' MANA |', '| REGEN - ' + str(player.manaregen) ); out("")

def drawBattleMenu():
    out("\nWhat to do?")
    out(" q - flee ", 'yellow')
    out(" w - spells", 'yellow')
    out(" e - skip round", 'yellow')
    return('battle') # current menu
  

def drawSpellMenu(player):
    out("\nYour Spells: ")
    keys = ['q', 'w', 'e']
    for i in range(len(player.inventory)):
        out(keys[i] + ' - ' + eval(player.inventory[i].hardid).name + ', cost: ' + str(eval(player.inventory[i].hardid).cost) + ' mana, type: '+ str(eval(player.inventory[i].hardid).type) + ', value: ' + str(eval(player.inventory[i].hardid).value))
    return('spell') # current menu

def printItemInfo(stats):
    if stats[0] == 0: sprefix = [" + MAX MANA: ", " + MANA REGEN: "]
    if stats[0] == 1: sprefix = [" + MAX HP: ", " + HP REGEN: "]
    out(" Stats: ")
    out("  Description: " + stats[1])
    for i in range(len(sprefix)):
        a = i + 4; out(" {}{}".format(sprefix[i], stats[a]))
    out("  Rarity: " + str(stats[2]), 'yellow')
    out("  Level: " + str(stats[3]), 'cyan')
    out(" Do you want to buy this item? (q/*) ")

# copied from http://stackoverflow.com/questions/3173320/text-progress-bar-in-the-console

def bar(iteration, total, prefix = ' |', suffix = '| ', ):
    decimals = 1
    length = 20
    fill = '█'
    printEnd = "\r"
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    out(f'\r{prefix} |{bar}| {percent}% ({iteration}) {suffix}', alt_newline = printEnd)
