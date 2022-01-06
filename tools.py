import pygame
import random

class colors():
    black = 0, 0, 0
    white = 255, 255, 255
    red = 220, 20, 60 # CRIMSON
    gold = 255, 215, 0
    grass_1 = 124, 252, 0
    grass_2 = 173, 255, 47
    forest_green = 34, 139, 34
    sky_1 = 0, 191, 255
    sky_2 = 135, 206, 235
    water = 65, 105, 225
    indigo = 75, 0, 130
    fence = 255, 228, 196
    silver = 192, 192, 192

def DrawText(s, color, pos, screen):
    font = pygame.font.SysFont('Roboto', 30)
    text = font.render(s, 1, pygame.Color(color))
    screen.blit(text, pos)

def RandomRotate(image):
    r = random.randint(0,3)
    if r == 0: angle = 0
    if r == 1: angle = 90
    if r == 2: angle = 180
    if r == 3: angle = 270
    return(pygame.transform.rotate(image, angle))