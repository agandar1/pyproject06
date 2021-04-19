#!/usr/bin/env python3
# Main AI File
from random import randint
import arcade


class playerBrain():
    directions = []

    def __init__(self, move_count):
        self.move_count = move_count
        self.randomMoves()

    def randomMoves(self):
        for i in range(self.move_count):
            self.directions.append(randint(1, 9))


class Player(arcade.Sprite):
    "class for the player/s"
    def __init__(self, spawn, move_count, human, speed):
        super().__init__("assets/PLAYER.png", 1.15)
        if not human:
            self.brain = playerBrain(move_count)
            self.directions = self.brain.directions
        self.center_x = spawn[0]
        self.center_y = spawn[1]
        self.speed = speed

    def update(self, delta_time):
        "move the player"
        direction = self.directions.pop()
        if direction == 1:
            self.change_x = self.speed * delta_time
            self.change_y = 0
        if direction == 2:
            self.change_x = - 1 * (self.speed * delta_time)
            self.change_y = 0
        if direction == 3:
            self.change_y = self.speed * delta_time
            self.change_x = 0
        if direction == 4:
            self.change_y = - 1 * (self.speed * delta_time)
            self.change_x = 0
        if direction == 5:
            self.change_x = self.speed * delta_time
            self.change_y = self.speed * delta_time
        if direction == 6:
            self.change_x = self.speed * delta_time
            self.change_y = - 1 * (self.speed * delta_time)
        if direction == 7:
            self.change_x = - 1 * (self.speed * delta_time)
            self.change_y = self.speed * delta_time
        if direction == 8:
            self.change_x = - 1 * (self.speed * delta_time)
            self.change_y = - 1 * (self.speed * delta_time)
        if direction == 9:
            self.change_x = 0
            self.change_y = 0
