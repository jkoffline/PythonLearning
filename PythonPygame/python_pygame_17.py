#!/usr/bin/env python3
# -*- utf-8 -*-
#
# Karl.Lv@outlook.com, KarlLv@126.com
# 21 July, 2017
#

from sys import exit

import pygame
from pygame.locals import *

from vector2 import Vec2d

pygame.init()

screen = pygame.display.set_mode((640, 480), 0, 32)

background_image = 'sushiplate.jpg'
sprite_image = 'fugu.png'

background = pygame.image.load(background_image).convert()
sprite = pygame.image.load(sprite_image).convert_alpha()

clock = pygame.time.Clock()

position = Vec2d(100.0, 100.0)
heading = Vec2d(0, 0)

while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            exit()

    screen.blit(background, (0, 0))
    screen.blit(sprite, position)

    time_passed = clock.tick()
    time_passed_seconds = time_passed / 1000.0
    print("time_passed_seconds: ", time_passed_seconds)

    destination = (Vec2d(*pygame.mouse.get_pos()) - 
                    Vec2d(*sprite.get_size()) / 2)
    print("pygame.mouse.get_pos(): ", pygame.mouse.get_pos())
    print("destination: ", destination)

    vector_to_mouse = Vec2d(destination) - Vec2d(position)
    vector_to_mouse = vector_to_mouse.normalized()
    print("vector_to_mouse: ", vector_to_mouse)

    heading = heading + (vector_to_mouse * 0.6)
    position += heading * time_passed_seconds
    print("heading: ", heading)
    print("postion: ", position)

    pygame.display.update()
