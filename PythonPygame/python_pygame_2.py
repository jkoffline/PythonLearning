#!/usr/bin/env python3
# -*- utf-8 -*-
#
# http://eyehere.net/2011/python-pygame-novice-professional-2/
#
# Karl.Lv@outlook.com, KarlLv@126.com
# 14 July, 2017
#

import pygame
from pygame.locals import *
from sys import exit

import time

pygame.init()

SCREEN_SIZE = (640, 480)
screen = pygame.display.set_mode(SCREEN_SIZE, 0, 32)

font = pygame.font.SysFont("dejavu-serif", 16);
font_height = font.get_linesize()

print("font_height: ", font_height)
event_text = []

while True:
    event = pygame.event.wait()
    event_text.append(str(event))
    event_text = event_text[-SCREEN_SIZE[1]//font_height:]

    if event.type == QUIT:
        exit()

    screen.fill((255, 127, 0))

    y = SCREEN_SIZE[1]-font_height

    for text in reversed(event_text):
        screen.blit(font.render(text, True, (0, 0, 0)), (0, y))

        y-=font_height

    pygame.display.update()

