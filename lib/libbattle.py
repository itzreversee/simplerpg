import math, random
from os import pathsep
from lib.libdraw import *
from lib.libmagic import *
from assets.items import *
from lib.randomthings import *
from lib.libinput import getUserInput
from entitylogic.ai import  getEasyAi, getNormalAi

global isBattleGoing
global battletype
global rounds

battletype = 0 # normal battle, 1 = bossfight

def battle(p, e):
    cmenu = 'battle'
    menuinput = 3
    rounds = 0
    isBattleGoing = True
    while isBattleGoing:
        rounds = rounds + 1 

        time.sleep(0.5)

        if p.hp <= 0: return 0;
        if e.hp <= 0: return 1;

        ambient(p)
        ambient(e)
        
        while True: #menu loop
            clearConsole()
            drawBasicBattleMenu(p, e, rounds)
            if (cmenu) == 'battle':
                drawBattleMenu()
                (menuinput) = getUserInput()
                if (menuinput) == 0: 
                    z = flee(p, rounds);
                    if z == 0:
                        break;
                    elif z == 1:
                        return 2;
                    elif z == 2:
                        return 3;
                if (menuinput) == 1: cmenu = drawSpellMenu(p)
                if (menuinput) == 2: cmenu = 'battle'; break;
            if (cmenu) == 'spell':
                time.sleep(0.5)
                (menuinput) = getUserInput()
                if (menuinput) != 4 and (menuinput) != 5 and (menuinput) != 6: 
                    cmenu = castspell(p, e, p.inventory[menuinput]); break;
            cmenu = 'battle';   

        if (isBattleGoing) == False: break;

        ger = getEnemyRound(p ,e)
        if ger == 3: return 3;

    return;
        
def getEnemyRound(p, e):
    if e.location == 0: 
        a = getEasyAi(p, e)
    if e.location == 1: 
        a = getNormalAi(p, e)
    print(" [debug] getEnemyRound, a = " + str(a)); input()
    if a == 8: 
        z = flee(e, 69); 
        if z == 2: return 3
    elif a == 9: return;
    else: 
        castspell(e, p, e.inventory[a])
        e.mana -= e.inventory[a].cost

def castspell(player, enemy, spell): 
    print('\n')

    if (spell.cost) > player.mana: 
        if (player.isEnemy) == False: print(" You don't have enough mana!"); 
        return('battle');

    else:

        if (spell.type) == 'damage':
            enemy.hp = round(enemy.hp - spell.value, 2) 
            player.mana = player.mana - spell.cost

            print(" " + player.name + " casted " + spell.name + "!")
            time.sleep(1)

        if (spell.type) == 'curse':
            enemy.hp = round(enemy.hp - (spell.value - 5) ,2) 
            enemy.curseLeft = spell.duration
            player.mana = player.mana - spell.cost
            

            print(" " + player.name + " casted " + spell.name + "!")
            time.sleep(1)


        if (spell.type) == 'heal':
            player.hp = player.hp + spell.value
            player.mana = player.mana - spell.cost

            print(" " + player.name + " used " + spell.name + "!")
            time.sleep(1)

        return('battle');

def ambient(p): 
    p.mana = p.mana + p.manaregen
    if p.mana > p.maxmana:
        p.mana = p.maxmana
    
    p.hp = p.hp + p.hpregen
    if p.hp > p.maxhp:
        p.hp = p.maxhp

    if (p.curseLeft) >= 1: 
        if (p.curseId) == 6: p.hp = p.hp - CurseSpell.value
        p.curseLeft = p.curseLeft - 1

def flee(p, rounds):
    if not rounds >= 20:
         chance = random.randint(0, (35 - rounds))
    else: chance = random.randint(0, 10)
    print("\n " + p.name+ " is trying to flee!")
    if (chance) == 0:
        time.sleep(3)
        print(" ... ")
        time.sleep(1)
        print(" " + p.name + " fleed!")
        if p.isEnemy == True:
            return 3;
        else: return 1;
    time.sleep(1.5)
    return 0;
