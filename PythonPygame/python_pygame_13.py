#!/usr/bin/env python3
# -*- utf-8 -*-
#
# http://eyehere.net/2011/python-pygame-novice-professional-8/
#
# Karl.Lv@outlook.com, KarlLv@126.com
# 19 July, 2017
#

from sys import exit
from random import randint
from math import pi

import pygame
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((640, 480), 0, 32)

background_image = 'sushiplate.jpg'
sprite_image = 'fugu.png'

background = pygame.image.load(background_image).convert()
sprite = pygame.image.load(sprite_image)

clock = pygame.time.Clock()

x = 0

speed = 250

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()

    screen.blit(background, (0, 0))
    screen.blit(sprite, (x, 100))

    time_passed = clock.tick()
    time_passed_seconds = time_passed / 1000.0

    distance_moved = time_passed_seconds * speed
    x += distance_moved

    if x > 640:
        speed = -250

    if x < 0:
        speed = 250

    pygame.display.update()
