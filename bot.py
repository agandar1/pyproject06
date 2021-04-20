#!/usr/bin/env python3
# Main AI File
from random import randint, uniform
import arcade
import copy


class playerBrain():
    def __init__(self, move_count):
        self.directions = []
        self.move_count = move_count
        self.randomMoves()

    def randomMoves(self):
        for i in range(self.move_count):
            self.directions.append(randint(1, 9))


class Genetic():
    parents_count = 20

    def __init__(self, player_list):
        self.parents = []
        self.directions = []
        self.players = player_list

        #for i in range(int(self.parents_count / 2)):
            #self.killWorst()

        for i in range(len(self.players)):
            self.directions.append(self.players[i].directions)

        self.total_fitness = self.totalFitness()

    def killWorst(self):
        least = 100
        for i in range(len(self.players)):
            if self.players[i].fitness < least:
                least = self.players[i].fitness
        for i in range(len(self.players)):
            if self.players[i].fitness == least:
                self.players[i].kill()
                break

    def newDirections(self):
        for i in range(self.parents_count):
            self.selection()
        # print(len(self.parents))

        return self.directions

    def totalFitness(self):
        total_fitness = 0
        for i in range(len(self.players)):
            total_fitness += self.players[i].fitness
        return total_fitness

    def selection(self):
        fitness_sum = 0
        rand_num = uniform(0, self.total_fitness)
        for i in range(len(self.players)):
            fitness_sum += self.players[i].fitness
            if fitness_sum > rand_num:
                self.parents.append(copy.deepcopy(self.players[i].directions))


class Player(arcade.Sprite):
    "class for the player/s"
    def __init__(self, spawn, move_count, human, speed, coinList, goal):
        super().__init__("assets/PLAYER.png", 1.15)
        self.reachedCoin = False
        self.alive = True
        self.fitness = 0

        if not human:
            self.brain = playerBrain(move_count)
            self.directions = copy.deepcopy(self.brain.directions)

        self.center_x = spawn[0]
        self.center_y = spawn[1]

        self.goal_x = goal[0]
        self.goal_y = goal[1]

        self.speed = speed
        self.coinList = coinList
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
        if not self.alive:
            if self.fitness == 0:
                self.calcFitness()
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
