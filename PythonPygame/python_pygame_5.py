#!/usr/bin/env python3
# -*- utf-8 -*-
#
# http://eyehere.net/2011/python-pygame-novice-professional-4/
#
# Karl.Lv@outlook.com, KarlLv@126.com
# 14 July, 2017
#

from sys import exit
import time
import pygame
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((640, 480), 0, 32)

print(pygame.font.get_fonts())

#font = pygame.font.SysFont("方正兰亭超细黑简体", 80)

font = pygame.font.Font("FZLTCXHJW.TTF", 60)

str_chs = "北冥有鱼，其名为鲲。鲲之大，不知其几千里也；"\
          "化而为鸟，其名为鹏。鹏之背，不知其几千里也；"\
          "怒而飞，其翼若垂天之云。是鸟也，海运则将徙于南冥。"

text_surface = font.render(str_chs, True, (0, 0, 255))

x = 0
y = (480 - text_surface.get_height())/2

background = pygame.image.load("sushiplate.jpg").convert()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()

    screen.blit(background, (0, 0))

    x -= 0.2
    #time.sleep(1)
    if x < -text_surface.get_width():
        x = 640 - text_surface.get_width()

    screen.blit(text_surface, (x, y))

    pygame.display.update()
