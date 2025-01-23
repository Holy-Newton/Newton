#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 19:52:35 2025

@author: francoisdeberdt
"""

### Tentative désespérée de faire Flappy-bird en python


import pygame
import os
import math as m
from pynput import keyboard




pygame.init()



WIDTH, HEIGHT = 1200,800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("------Flappy-Bird-------- by Holly_Newton")

#------------------------COLORS----------------------------------

WHITE = (240, 240, 240)
VENUS_YELLOW = (237, 201, 175)
YELLOW = (255, 255, 0)
BLUE = (34, 139, 230)
RED = (201, 52, 37)
DARK_GREY = (169, 169, 169)
SATURN_COLOR = (210, 180, 140)
JUPITER_COLOR = (200, 100, 50)
SPACE_GREY_BLUE = (10, 12, 40)


BLUE_SKY = (140, 190, 255)
GROUND = (222, 186, 136)
GRASS = (141, 228, 69)
TUBE = (98, 203, 60)
YELLOW_BIRD = (255, 254, 70)
ORANGE_BIRD = (255, 180, 45)
WHITE_WING = (255, 230, 200)


#------------------------MOVES----------------------------------

class move:
    def __init__(self, x, y, )
































def init():
    run = True
    clock = pygame.time.Clock()
    
    
    
    while run:
        clock.tick(60)
        WIN.fill(BLUE_SKY)
        
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        pygame.display.update()
    pygame.quit()


init()






















