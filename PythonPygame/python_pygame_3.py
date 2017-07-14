#!/usr/bin/env python3
# -*- utf-8 -*-
#
# http://eyehere.net/2011/python-pygame-novice-professional-3/
#
# Karl.Lv@outlook.com, KarlLv@126.com
# 14 July, 2017
#

from sys import exit
import pygame
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((640, 480), 0, 32)
background = pygame.image.load('sushiplate.jpg').convert()

Fullscreen = False

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
    if event.type == KEYDOWN:
        if event.key == K_f:
            Fullscreen = not Fullscreen
            if Fullscreen:
                screen = pygame.display.set_mode((640, 480), FULLSCREEN, 32)
            else:
                screen = pygame.display.set_mode((640, 480), 0, 32)

    screen.blit(background, (0,0))
    pygame.display.update()
