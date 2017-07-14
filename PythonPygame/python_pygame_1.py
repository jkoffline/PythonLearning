#!/usr/bin/env python3
# -*- utf-8 -*-
#
# http://eyehere.net/2011/python-pygame-novice-professional-1/
#
# Karl.Lv@outlook.com, KarlLv@126.com
# 14 July, 2017
#

import pygame
from pygame.locals import *
from sys import exit

pygame.init()

screen = pygame.display.set_mode((640,480),0,32)

pygame.display.set_caption("Hello, World!")

background_image_filename = 'sushiplate.jpg'
mouse_image_filename = 'fugu.png'

background = pygame.image.load(background_image_filename).convert()
mouse_cursor = pygame.image.load(mouse_image_filename).convert_alpha()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()

    screen.blit(background, (0,0))

    x,y = pygame.mouse.get_pos()
    x-=mouse_cursor.get_width() / 2
    y-=mouse_cursor.get_height() / 2

    screen.blit(mouse_cursor, (x, y))

    pygame.display.update()

