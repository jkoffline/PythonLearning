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

SCREEN_SIZE = (640, 480)
screen = pygame.display.set_mode(SCREEN_SIZE, RESIZABLE, 32)
background = pygame.image.load('sushiplate.jpg').convert()

Fullscreen = False

while True:
    event = pygame.event.wait()
    if event.type == QUIT:
        exit()
    if event.type == VIDEORESIZE:
        SCREEN_SIZE = event.size
        screen = pygame.display.set_mode(SCREEN_SIZE, RESIZABLE, 32)
        pygame.display.set_caption("Window resized to "+str(event.size))

    screen_width, screen_height = SCREEN_SIZE
    for y in range(0, screen_height, background.get_height()):
        for x in range(0, screen_width, background.get_width()):
            screen.blit(background, (x, y))

    pygame.display.update()
