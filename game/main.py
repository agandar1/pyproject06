#!/usr/bin/env python3
# Main Game File
import pygame
from pygame.locals import *
# import levels here
import levels.lvl1

# Colors
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)

# Window Setup
FPS = 60
WIDTH, HEIGHT = 1000, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("World's Hardest Game")


class Game:
    "Class to draw the map"
    # setup levels
    # lvln = tile_list, border_list
    lvl1 = [levels.lvl1.tile_list, levels.lvl1.border_list]
    lvls = [lvl1]

    def __init__(self, starting):
        self.level = starting - 1
        self.tile_list = self.lvls[self.level][0]
        self.border_list = self.lvls[self.level][1]

    def draw(self):
        "Draw all the tiles"
        for tile in self.tile_list:
            WIN.blit(tile[0], tile[1])
        for line in self.border_list:
            pygame.draw.line(WIN, BLACK, line[0], line[1], 4)
        pygame.display.update()


def main():
    "Main Game Function"
    # some setup
    start_lvl = 1
    game = Game(start_lvl)
    clock = pygame.time.Clock()
    run = True

    while run:
        clock.tick(FPS)
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        game.draw()
    pygame.quit()


if __name__ == "__main__":
    main()
