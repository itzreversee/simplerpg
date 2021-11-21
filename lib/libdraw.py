
from lib.librps import getUserInput
from lib.libmagic import *

from lib.randomthings import notimplemented

def drawBasicMenu(player, enemy): 
    print('\n')
    print("| " + player.name + " | vs | " + enemy.name + " (" + str(enemy.hp) + " HP) |")
    print("HP - " + str(player.hp))
    print("MANA - " + str(player.mana))

def drawBattleMenu():
    print("\nWhat to do?")
    print(" q - battle ( not implemented )")
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