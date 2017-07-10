#!/usr/bin/env python3
# -*- utf-8 -*-

background_image_filename = 'sushiplate.jpg'
mouse_image_filename = 'fugu.png'

import pygame
from pygame.locals import *
from sys import exit

import time

pygame.init()


screen = pygame.display.set_mode((640,480),0,32)

pygame.display.set_caption("Hello, World!")

background = pygame.image.load(background_image_filename).convert()
mouse_cursor = pygame.image.load(mouse_image_filename).convert_alpha()

time.sleep(10)

