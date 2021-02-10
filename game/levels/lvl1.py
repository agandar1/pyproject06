#!/usr/bin/env python3
# Game Level 1
import pygame
from pygame.locals import *

tile_size = 50
tile_list = []
border_list = []

# define the map
# Columns    1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20    Rows
map_data = [[ 0, 0,  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 1
            [ 0, 0,  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 2
            [ 0, 0,  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 3
            [ 0, 2,  2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 2, 2, 2, 0],  # 4
            [ 0, 2,  2, 2, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 2, 2, 2, 0],  # 5
            [ 0, 2,  2, 2, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 2, 2, 2, 0],  # 6
            [ 0, 2,  2, 2, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 2, 2, 2, 0],  # 7
            [ 0, 2,  2, 2, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 2, 2, 2, 0],  # 8
            [ 0, 2,  2, 2, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 0],  # 9
            [ 0, 0,  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 10
            [ 0, 0,  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 11
            [ 0, 0,  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]  # 12

# load assets
empty = pygame.image.load('assets/EMPTY.png')
light_bg = pygame.image.load('assets/LIGHT.png')
dark_bg = pygame.image.load('assets/DARK.png')
goal = pygame.image.load('assets/GREEN.png')

# create tiles from the map
row_count = 0
for i, row in enumerate(map_data):
    col_count = 0
    for j, tilenum in enumerate(row):
        if tilenum == 0:
            img = pygame.transform.scale(empty, (tile_size, tile_size))
        if (tilenum == 1) and ((row_count + col_count) % 2 == 0):
            img = pygame.transform.scale(light_bg, (tile_size, tile_size))
        if (tilenum == 1) and ((row_count + col_count) % 2 != 0):
            img = pygame.transform.scale(dark_bg, (tile_size, tile_size))
        if tilenum == 2:
            img = pygame.transform.scale(goal, (tile_size, tile_size))
        if tilenum != 0:
            if row[j + 1] == 0:
                line_x = (col_count + 1) * tile_size
                line_y = row_count * tile_size
                line = ((line_x, line_y - 1), (line_x, line_y + tile_size + 1))
                border_list.append(line)
            if row[j - 1] == 0:
                line_x = (col_count) * tile_size
                line_y = row_count * tile_size
                line = ((line_x, line_y - 1), (line_x, line_y + tile_size + 1))
                border_list.append(line)
            if map_data[i + 1][j] == 0:
                line_x = col_count * tile_size
                line_y = (row_count + 1) * tile_size
                line = ((line_x - 1, line_y), (line_x + tile_size + 1, line_y))
                border_list.append(line)
            if map_data[i - 1][j] == 0:
                line_x = col_count * tile_size
                line_y = row_count * tile_size
                line = ((line_x - 1, line_y), (line_x + tile_size + 1, line_y))
                border_list.append(line)

        img_rect = img.get_rect()
        img_rect.x = col_count * tile_size
        img_rect.y = row_count * tile_size
        tile = (img, img_rect, tilenum)
        tile_list.append(tile)
        col_count += 1
    row_count += 1
