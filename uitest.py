import pygame
import pygame_gui
import sys

from tools import *

displaySize = width, heigth = 1280, 720
displayGrid = [[],[]] # init grid 
displayGridX = 16
displayGridY = 9


# pygame stuff
pygame.init() # INIT PYGAME
displayFlags = pygame.OPENGL | pygame.SHOWN
screen = pygame.display.set_mode(displaySize) # 1280x720 - 128x72 grid 
screen.fill(pygame.Color(colors.indigo))
pygame.display.set_allow_screensaver(True) # ALLOW SCREEN SAVER
pygame.display.set_caption("Simple RPG - PyGame Test")
clock = pygame.time.Clock()

manager = pygame_gui.UIManager(displaySize)

# EXAMPLE VALUES

class player:
    name = "Maciek"
    hp = 80
    maxhp = 100
    mana = 200
    maxmana = 250
    level = 1
    exp = 20

class enemy:
    name = "Silver Monster"
    hp = 50
    maxhp = 100

# RENDER UI HERE | LAYOUT: x = 20; y += 70 | LABEL SIZE: 100;50 | BUTTON SIZE : 200;50
class playerui(): 
        name = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((20, 20),(150, 50)), text = player.name, manager=manager)

        hp = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((20, 110),(100, 50)), text = "HP ", manager=manager) 
        hpbar = pygame_gui.elements.UIProgressBar(relative_rect=pygame.Rect((140, 110),(250, 50)), manager=manager) 

        mana = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((20, 180),(100, 50)), text = "MANA " , manager=manager) 
        manabar = pygame_gui.elements.UIProgressBar(relative_rect=pygame.Rect((140, 180),(250, 50)), manager=manager) 

        level = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((20, 250),(100, 50)), text = "LEVEL " + str(player.level), manager=manager) 
        exp = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((140, 250),(100, 50)), text = "EXP " + str(player.exp), manager=manager) 

class enemyUILayout():
    name = pygame.Rect(-170,20,150,50)
    hp = pygame.Rect(-120,110, 100,50)
    hpbar = pygame.Rect(-390,110,250,50)

class enemyui(): 
        name = pygame_gui.elements.UILabel(relative_rect=enemyUILayout.name, text = enemy.name, manager=manager, anchors = {"left":"right", "right":"right", "top":"top", "bottom":"top"})
        hp = pygame_gui.elements.UILabel(relative_rect=enemyUILayout.hp, text = "HP ", manager=manager, anchors = {"left":"right", "right":"right", "top":"top", "bottom":"top"}) 
        hpbar = pygame_gui.elements.UIProgressBar(relative_rect=enemyUILayout.hpbar, manager=manager, anchors = {"left":"right", "right":"right", "top":"top", "bottom":"top"}) 


class battlemenu():
    spells_btn = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((20, 650), (200, 50)), text='SPELLS', manager=manager)
    skipround_btn = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((20, 580), (200, 50)), text='SKIP ROUND', manager=manager)
class spellsmenu():
    back_btn = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((20, 650), (200, 50)), text='BACK', manager=manager)
    spell1 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((20, 580), (200, 50)), text='FIRE SPELl', manager=manager)
    spell2 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((20, 510), (200, 50)), text='CURSE SPELL', manager=manager)
    spell3 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((20, 440), (200, 50)),text='HEAL SPELL', manager=manager)

def reloadui():
    battlemenu.spells_btn.hide()
    battlemenu.skipround_btn.hide()

    spellsmenu.back_btn.hide()
    spellsmenu.spell1.hide()
    spellsmenu.spell2.hide()
    spellsmenu.spell3.hide()

reloadui()
cmenu = 'battle'
while True: # GAME LOOP
    
    delta_time = clock.tick(60)/1000.0 # TICK THE CLOCK
    screen.fill(pygame.Color(colors.indigo)) # CLEAR FRAME
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.KEYDOWN: # KEYBOARD CONTROLS
            if event.key == pygame.K_ESCAPE: sys.exit()

        # UI EVENTS
        manager.process_events(event)
        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == battlemenu.spells_btn:
                cmenu = 'spells'; reloadui()
            if event.ui_element == battlemenu.skipround_btn:
                print('skip round logic')

            if event.ui_element == spellsmenu.back_btn: 
                cmenu = 'battle'; reloadui()
            if event.ui_element == spellsmenu.spell1: print('spell1 logic')
            if event.ui_element == spellsmenu.spell2: print('spell2 logic')
            if event.ui_element == spellsmenu.spell3: print('spell3 logic')

    # UI UPDATES
    manager.update(delta_time)
    manager.draw_ui(screen)

    # UI LOGIC
    playerui.hpbar.set_current_progress((player.hp * 100) / player.maxhp)
    playerui.manabar.set_current_progress((player.mana * 100) / player.maxmana)

    enemyui.hpbar.set_current_progress((enemy.hp * 100) / enemy.maxhp)

    if (cmenu) == 'battle': 
        battlemenu.spells_btn.show()
        battlemenu.skipround_btn.show()

    if (cmenu) == 'spells': 
        spellsmenu.back_btn.show()
        spellsmenu.spell1.show()
        spellsmenu.spell2.show()
        spellsmenu.spell3.show()

    
    # RENDER HERE

    # DRAW FPS
    DrawText(str(round(clock.get_fps())), pygame.Color(colors.red), (32, 32), screen)
    pygame.display.flip() # UPDATE DISPLAY EVERY FRAME 
