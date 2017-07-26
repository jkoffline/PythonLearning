#!/usr/bin/env python2
# -*- utf-8 -*-
#
# http://eyehere.net/2011/python-pygame-novice-professional-10/
#
# Karl.Lv@outlook.com, KarlLv@126.com
# 26 July, 2017
#

from sys import exit
from math import *

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
sprite_speed = 300
sprite_rotation = 0
sprite_rotation_speed = 360

while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            exit()

    pressed_keys = pygame.key.get_pressed()

    rotation_direction = 0
    movement_direction = 0

    if pressed_keys[K_LEFT]:
        rotation_direction = +1
    elif pressed_keys[K_RIGHT]:
        rotation_direction = -1

    if pressed_keys[K_UP]:
        movement_direction = +1
    elif pressed_keys[K_DOWN]:
        movement_direction = -1

    screen.blit(background, (0, 0))

    rotated_sprite = pygame.transform.rotate(sprite, sprite_rotation)

    w, h = rotated_sprite.get_size()

    sprite_draw_pos = Vector2(sprite_pos.x - w / 2, sprite_pos.y - h / 2)
    screen.blit(rotated_sprite, sprite_draw_pos)

    time_passed = clock.tick(30)
    time_passed_seconds = time_passed / 1000.0

    sprite_rotation += (rotation_direction * sprite_rotation_speed * 
                        time_passed_seconds)
    print "sprite_rotation: ", sprite_rotation

    heading_x = sin(sprite_rotation * pi / 180)
    heading_y = cos(sprite_rotation * pi / 180)

    heading = Vector2(heading_x, heading_y)

    print 'heading: ', heading
    heading *= movement_direction

    sprite_pos += heading * sprite_speed * time_passed_seconds

    if sprite_pos.get_x() > 640:
        sprite_pos.set_x(200)
    elif sprite_pos.get_x() < 0:
        sprite_pos.set_x(200)
    else:
        pass

    if sprite_pos.get_y() > 480:
        sprite_pos.set_y(150)
    elif sprite_pos.get_y() < 0:
        sprite_pos.set_y(150)
    else:
        pass

    print "position: ", sprite_pos

    pygame.display.update()
