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

x = 100
y = 100
speed_x = 130
speed_y = 170

'''
    ------------------------------------------
    |@                 @           @         |
    |   @           @     @     @     @      |
    |      @     @           @           @   |
    |         @           @     @           @|
    |      @     @     @           @     @   |
    |   @           @                 @      |
    |@           @     @           @     @   |
    |   @     @           @     @           @|
    |      @                 @           @   |
    ------------------------------------------
'''

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()

    screen.blit(background, (0, 0))
    screen.blit(sprite, (x, y))

    time_passed = clock.tick(30)
    time_passed_seconds = time_passed / 1000.0

    distance_x = time_passed_seconds * speed_x
    distance_y = time_passed_seconds * speed_y
    x += distance_x
    y += distance_y

    if x > 640 - sprite.get_width():
        speed_x = -speed_x
        x = 640 - sprite.get_width()
    elif x < 0:
        speed_x = -speed_x
        x = 0

    if y > 480 - sprite.get_height():
        speed_y = -speed_y
    elif y < 0:
        speed_y = -speed_y
        y = 0

    pygame.display.update()
