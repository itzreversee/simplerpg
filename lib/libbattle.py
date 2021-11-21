import math, random
from os import pathsep
from lib.libdraw import *
from lib.libmagic import *
from assets.items import *
from lib.randomthings import *
from lib.libinput import getUserInput
from entitylogic.silvermonster import entityLogic, enemyRound

global isBattleGoing
global battletype
global rounds

battletype = 0 # normal battle

def battle(p, e):
    cmenu = 'battle'
    menuinput = 3
    rounds = 0
    isBattleGoing = True
    while isBattleGoing:
        rounds = rounds + 1 

        time.sleep(0.5)

        quickCheck(p, e)

        ambient(p)
        ambient(e)

        while True: #menu loop
            clearConsole()
            drawBasicBattleMenu(p, e, rounds)
            if (cmenu) == 'battle':
                drawBattleMenu()
                (menuinput) = getUserInput()
                if (menuinput) == 0: isBattleGoing = flee(p, rounds); break;
                if (menuinput) == 1: cmenu = drawSpellMenu(p)
                if (menuinput) == 2: cmenu = 'battle'; break;
            if (cmenu) == 'spell':
                time.sleep(0.5)
                (menuinput) = getUserInput()
                if (menuinput) != 4: 
                    cmenu = castspell(p, e, menuinput); break;
            cmenu = 'battle';   

        if (isBattleGoing) == False: break;

        getEnemyRound(p ,e)

        
def getEnemyRound(p, e):
    pb, eb, sb = enemyRound(p, e)
    castspell(pb, eb, sb)

def castspell(player, enemy, selection):
    print('\n')
    
    class spell():
        type = eval(player.inventory[selection].hardid).type
        value = eval(player.inventory[selection].hardid).value
        cost = eval(player.inventory[selection].hardid).cost
        duration = eval(player.inventory[selection].hardid).duration

    if (eval(player.inventory[selection].hardid).cost) > player.mana: 
        if (player.isEnemy) == False: print(" You don't have enough mana!"); 
        return('battle');

    else:

        if (eval(player.inventory[selection].hardid).type) == 'damage':
            enemy.hp = round(enemy.hp - spell.value, 2) 
            player.mana = player.mana - spell.cost

            print(" " + player.name + " casted " + eval(player.inventory[selection].hardid).name + "!")
            time.sleep(1.5)

        if (eval(player.inventory[selection].hardid).type) == 'curse':
            enemy.hp = round(enemy.hp - (spell.value - 5) ,2) 
            enemy.curseLeft = spell.duration
            enemy.curse = selection
            player.mana = player.mana - spell.cost

            print(" " + player.name + " casted " + eval(player.inventory[selection].hardid).name + "!")
            time.sleep(1.5)


        if (eval(player.inventory[selection].hardid).type) == 'heal':
            player.hp = player.hp + spell.value
            player.mana = player.mana - spell.cost

            print(" " + player.name + " used " + eval(player.inventory[selection].hardid).name + "!")
            time.sleep(1.5)

        return('battle');

def ambient(p): 
    p.mana = p.mana + p.manaregen
    if p.mana > p.maxmana:
        p.mana = p.maxmana

    if (p.curseLeft) >= 1: 
        if (p.curseId) == 6: p.hp = p.hp - CurseSpell.value
        p.curseLeft = p.curseLeft - 1

def flee(p, rounds):
    chance = random.randint(0, (20 - rounds))
    print("\n " + p.name+ " is trying to flee!")
    if (chance) == 0:
        time.sleep(3)
        print(" ... ")
        time.sleep(1)
        print(" " + p.name + " fleed!")
        return False;
    time.sleep(1.5)
    return True

def quickCheck(p, e):
    if (p.hp) <= 0:
        print("You Died!")
        exit()
    if (e.hp) <= 0:
        print("You Won!")
        exit()