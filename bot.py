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
    reachedCoin = False
    alive = True
    fitness = 0

    def __init__(self, spawn, move_count, human, speed, coinList, goal):
        super().__init__("assets/PLAYER.png", 1.15)
        if not human:
            self.brain = playerBrain(move_count)
            self.directions = self.brain.directions
        self.center_x = spawn[0]
        self.center_y = spawn[1]
        self.speed = speed
        self.coinList = coinList
        self.goal_x = goal[0]
        self.goal_y = goal[1]
        if len(coinList) == 0:
            self.reachedCoin = True
        else:
            self.currentCoin = self.coinList.pop(0)

    def distance(self, x_2, y_2):
        x_1 = self.center_x
        y_1 = self.center_y
        return ((((x_2 - x_1)**2) + (y_2 - y_1))**(1 / 2))

    def calcFitness(self):
        if not self.reachedCoin:
            self.fitness = 1.0 / (self.distance(self.currentCoin.center_x, self.currentCoin.center_y)**2)
            if len(self.coinList) > 0:
                self.coinList.pop(0)
                self.currentCoin = self.coinList[len(self.coinList) - 1]
                self.reachedCoin = False
            else:
                self.reachedCoin = True
        else:
            self.fitness = 1.0 / (self.distance(self.goal_x, self.goal_y)**2)

    def update(self, delta_time):
        if self.alive:
            if len(self.brain.directions) > 0:
                self.move(delta_time)
            else:
                self.alive = False
        else:
            if self.fitness == 0:
                self.calcFitness()
                print(self.fitness)
            self.change_x = 0
            self.change_y = 0

    def move(self, delta_time):
        "move the player"
        direction = self.brain.directions.pop()
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
