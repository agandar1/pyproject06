#!/usr/bin/env python3
# Game Level 1
import pygame
from pygame.locals import *

tile_size = 50
tile_list = []

# Columns    1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20    Rows
map_data = [[ 0,   0,   0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],   # 1
            [ 0,   0,   0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],   # 2
            [ 14,  3,   3,  3, 15,  0,  0,  0,  0,  0,  0,  0,  0, 14,  3,  3,  3,  3,  3, 15],   # 3
            [ 6,   2,   2,  2, 17,  3,  3,  3,  3,  3,  3,  3,  3,  8,  1,  1,  2,  2,  2,  4],   # 4
            [ 6,   2,   2,  2, 11,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  9,  2,  2,  2,  4],   # 5
            [ 6,   2,   2,  2, 11,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1, 11,  2,  2,  2,  4],   # 6
            [ 6,   2,   2,  2, 11,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1, 11,  2,  2,  2,  4],   # 7
            [ 6,   2,   2,  2, 10,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1, 11,  2,  2,  2,  4],   # 8
            [ 6,   2,   2,  2,  1,  1,  7,  5,  5,  5,  5,  5,  5,  5,  5, 16,  2,  2,  2,  4],   # 9
            [ 12,  5,   5,  5,  5,  5, 13,  0,  0,  0,  0,  0,  0,  0,  0, 12,  5,  5,  5, 13],   # 10
            [ 0,   0,   0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],   # 11
            [ 0,   0,   0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0]]  # 12


# load assets
empty = pygame.image.load('assets/EMPTY.png')
light_bg = pygame.image.load('assets/LIGHT.png')
dark_bg = pygame.image.load('assets/DARK.png')
goal = pygame.image.load('assets/GREEN.png')
tw = pygame.image.load('assets/B.png')
rw = pygame.image.load('assets/L.png')
bw = pygame.image.load('assets/T.png')
lw = pygame.image.load('assets/R.png')
tlw = pygame.image.load('assets/TL.png')
brw = pygame.image.load('assets/BR.png')
trlw = pygame.image.load('assets/TLR.png')
brlw = pygame.image.load('assets/BLR.png')
rlw = pygame.image.load('assets/RL.png')
trc = pygame.image.load('assets/TRC.png')
tlc = pygame.image.load('assets/TLC.png')
brc = pygame.image.load('assets/BRC.png')
blc = pygame.image.load('assets/BLC.png')
rwtc = pygame.image.load('assets/RwTC.png')
lwbc = pygame.image.load('assets/LwBC.png')

row_count = 0
for row in map_data:
    col_count = 0
    for tile in row:
        if tile == 0:
            img = pygame.transform.scale(empty, (tile_size, tile_size))
        if (tile == 1) and ((row_count + col_count) % 2 == 0):
            img = pygame.transform.scale(light_bg, (tile_size, tile_size))
        if (tile == 1) and ((row_count + col_count) % 2 != 0):
            img = pygame.transform.scale(dark_bg, (tile_size, tile_size))
        if tile == 2:
            img = pygame.transform.scale(goal, (tile_size, tile_size))
        if tile == 3:
            img = pygame.transform.scale(tw, (tile_size, tile_size))
        if tile == 4:
            img = pygame.transform.scale(rw, (tile_size, tile_size))
        if tile == 5:
            img = pygame.transform.scale(bw, (tile_size, tile_size))
        if tile == 6:
            img = pygame.transform.scale(lw, (tile_size, tile_size))
        if tile == 7:
            img = pygame.transform.scale(tlw, (tile_size, tile_size))
        if tile == 8:
            img = pygame.transform.scale(brw, (tile_size, tile_size))
        if tile == 9:
            img = pygame.transform.scale(trlw, (tile_size, tile_size))
        if tile == 10:
            img = pygame.transform.scale(brlw, (tile_size, tile_size))
        if tile == 11:
            img = pygame.transform.scale(rlw, (tile_size, tile_size))
        if tile == 12:
            img = pygame.transform.scale(trc, (tile_size, tile_size))
        if tile == 13:
            img = pygame.transform.scale(tlc, (tile_size, tile_size))
        if tile == 14:
            img = pygame.transform.scale(brc, (tile_size, tile_size))
        if tile == 15:
            img = pygame.transform.scale(blc, (tile_size, tile_size))
        if tile == 16:
            img = pygame.transform.scale(rwtc, (tile_size, tile_size))
        if tile == 17:
            img = pygame.transform.scale(lwbc, (tile_size, tile_size))

        img_rect = img.get_rect()
        img_rect.x = col_count * tile_size
        img_rect.y = row_count * tile_size
        tile = (img, img_rect)
        tile_list.append(tile)
        col_count += 1
    row_count += 1
