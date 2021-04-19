#!/usr/bin/env python3
# Main AI File
from random import randint


class AI():
    players = []

    def __init__(self, player_count, move_count):
        self.move_count = move_count
        self.player_count = player_count
        self.players = []
        self.randomMoves()

    def randomMoves(self):
        for i in range(self.player_count):
            player = []
            for j in range(self.move_count):
                player.append(randint(1, 8))
            self.players.append(player)
