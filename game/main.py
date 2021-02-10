#!/usr/bin/env python3
# Main Game File
import pygame
from pygame.locals import *
import levels.lvl1

# Colors
BLACK = (0, 0, 0)
WHITE = (247, 247, 255)
GRAY = (230, 230, 255)
PURPLE = (180, 181, 254)
GREEN = (181, 254, 180)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)

# Window Setup
FPS = 60
WIDTH, HEIGHT = 1000, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("World's Hardest Game")

# Game Variables
tile_size = 50


class World:
    "Class to draw the map"
    def __init__(self, data):
        self.tile_list = data

    def draw(self):
        "Draw all the tiles"
        for tile in self.tile_list:
            WIN.blit(tile[0], tile[1])


def draw_window(world):
    "Update the Screen"
    world.draw()
    pygame.display.update()


def main():
    "Main Game Function"
    # some setup
    level = 1
    lvl1 = levels.lvl1.tile_list
    world = World(lvl1)
    clock = pygame.time.Clock()
    run = True

    while run:
        clock.tick(FPS)
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        draw_window(world)
    pygame.quit()


if __name__ == "__main__":
    main()
