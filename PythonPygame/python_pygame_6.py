#!/usr/bin/env python3
# -*- utf-8 -*-
#
# http://eyehere.net/2011/python-pygame-novice-professional-5/
# http://eyehere.net/2011/how-many-image-in-one-paper/
#
# Karl.Lv@outlook.com, KarlLv@126.com
# 17 July, 2017
#

import pygame
pygame.init()

screen_size = pygame.display.list_modes()
screen = pygame.display.set_mode(screen_size[-1])

all_colors = pygame.Surface((4096, 4096), depth=24)

for r in range(256):
    print(r+1, "out of 256")
    x = (r&15)*256
    y = (r>>4)*256
    for g in range(256):
        for b in range(256):
            all_colors.set_at((x+g, y+b), (r, g, b))

pygame.image.save(all_colors, "allcolors.bmp")
