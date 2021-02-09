#!/usr/bin/env python3
# Main Game File
import pygame
from pygame.locals import *

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


def draw_window():
    "Update the Screen"
    WIN.fill(PURPLE)
    pygame.display.update()


def main():
    "Main Game Function"
    # some setup
    clock = pygame.time.Clock()
    run = True

    while run:
        clock.tick(FPS)
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        draw_window()
    pygame.quit()


if __name__ == "__main__":
    main()
