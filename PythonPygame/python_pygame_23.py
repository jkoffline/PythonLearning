#!/usr/bin/env python2
# -*- utf-8 -*-
#
# http://eyehere.net/2011/python-pygame-novice-professional-17/
#
# Karl.Lv@outlook.com, KarlLv@126.com
# 2 August, 2017
#

import time

import pygame
from pygame.locals import *
from random import randint

class Star(object):

    def __init__(self, x, y, speed):
        self.x = x
        self.y = y
        self.speed = speed

def run():
    pygame.init()
    screen = pygame.display.set_mode((640, 480), FULLSCREEN, 32)

    stars = []

    for n in xrange(300):
        x = float(randint(0, 639))
        y = float(randint(0, 479))
        speed = float(randint(10, 300))
        stars.append(Star(x, y, speed))

    clock = pygame.time.Clock()

    white = (255, 255, 255)

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                return
            if event.type == KEYDOWN:
                return

        y = float(randint(0, 479))
        speed = float(randint(10, 300))
        star = Star(640., y, speed)
        stars.append(star)

        time_passed = clock.tick()
        time_passed_seconds = time_passed / 1000.0

        screen.fill((0, 0, 0))

        for star in stars:
            src_x = star.x - time_passed_seconds * star.speed
            dst_x = star.x + 1
            src_y = star.y
            dst_y = star.y
            pygame.draw.aaline(screen, white, (src_x, src_y), (dst_x, dst_y))
            star.x = src_x

        def on_screen(star):
            return star.x > 0

        stars = filter(on_screen, stars)
        pygame.display.update()

if __name__ == "__main__":
    run()
