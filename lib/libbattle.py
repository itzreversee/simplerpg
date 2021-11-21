from lib.libdraw import *
from lib.libmagic import *
from lib.randomthings import *
from lib.librps import getUserInput, getCPUinput
from enemylogic.silvermonster import entityLogic, enemyRound

import random

global isBattleGoing
global battletype

battletype = 0 # normal battle

def battle(p, e):
    cmenu = 'battle'
    menuinput = 3
    isBattleGoing = True
    while isBattleGoing:
        clearConsole()

        ambient(p)
        ambient(e)

        quickCheck(p, e)
        drawBasicMenu(p, e)
        
        if (cmenu) == 'battle':
            drawBattleMenu()
            (menuinput) = getUserInput()
            if (menuinput) == 0: notimplemented()
            if (menuinput) == 1: cmenu = drawSpellMenu(p)
            if (menuinput) == 2: cmenu = 'battle'
        if (cmenu) == 'spell':
            (menuinput) = getUserInput()
            if (menuinput) != 4: 

                cmenu = castspell(p, e, menuinput)
            cmenu = 'battle';   

        getEnemyRound(p ,e)

        time.sleep(3)

def ambient(p): 
    p.mana = p.mana + p.manaregen
    if p.mana > p.maxmana:
        p.mana = p.maxmana

    if (p.curseLeft) >= 1: 
        if (p.curseId) == 6: p.hp = p.hp - CurseSpell.value
        p.curseLeft = p.curseLeft - 1

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
            enemy.hp = enemy.hp - spell.value
            player.mana = player.mana - spell.cost

            print(" " + player.name + " casted " + eval(player.inventory[selection].hardid).name + "!")

        if (eval(player.inventory[selection].hardid).type) == 'curse':
            enemy.hp = enemy.hp - (spell.value - 5) 
            enemy.curseLeft = spell.duration
            enemy.curse = selection
            player.mana = player.mana - spell.cost

            print(" " + player.name + " casted " + eval(player.inventory[selection].hardid).name + "!")


        if (eval(player.inventory[selection].hardid).type) == 'heal':
            player.hp = player.hp + spell.value
            player.mana = player.mana - spell.cost

            print(" " + player.name + " used " + eval(player.inventory[selection].hardid).name + "!")
            

        return('battle');

def quickCheck(p, e):
    if (p.hp) <= 0:
        print("You Died!")
        exit()
    if (e.hp) <= 0:
        print("You Won!")
        exit()