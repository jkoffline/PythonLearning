#!/usr/bin/env python2
# -*- utf-8 -*-
#
# http://eyehere.net/2011/python-pygame-novice-professional-10/
#
# Karl.Lv@outlook.com, KarlLv@126.com
# 26 July, 2017
#

from sys import exit

import pygame
from pygame.locals import *
from gameobjects.vector2 import Vector2

pygame.init() 

screen = pygame.display.set_mode((640, 480), 0, 32)

background_image = 'sushiplate.jpg'
sprite_image = 'fugu.png'

background = pygame.image.load(background_image).convert()
sprite = pygame.image.load(sprite_image).convert_alpha()

clock = pygame.time.Clock()

sprite_pos = Vector2(200, 150)
sprite_speed = 30.

while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            exit()

    pressed_keys = pygame.key.get_pressed()

    key_direction = Vector2(2, 0)
    if pressed_keys[K_LEFT]:
        key_direction.x = -1
    elif pressed_keys[K_RIGHT]:
        key_direction.x = +1
    if pressed_keys[K_UP]:
        key_direction.y = -1
    elif pressed_keys[K_DOWN]:
        key_direction.y = +1

    key_direction.normalize()

    screen.blit(background, (0, 0))
    screen.blit(sprite, sprite_pos)

    time_passed = clock.tick(30)
    time_passed_seconds = time_passed / 1000.0

    sprite_pos += key_direction * sprite_speed * time_passed_seconds

    if sprite_pos.get_x() > 640:
        sprite_pos.set_x(200)
    elif sprite_pos.get_x() < 0:
        sprite_pos.set_x(200)
    else:
        pass

    print "position: ", sprite_pos

    pygame.display.update()
