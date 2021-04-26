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
    parents_count = 10

    def __init__(self, player_list, move_count):
        self.parents = []
        self.babies = []
        self.directions = []
        self.players = player_list
        self.moves = move_count

        for i in range(int(self.parents_count + 1)):
            self.killWorst()
        self.saveBest()

        for i in range(len(self.players)):
            self.directions.append(self.players[i].directions)

        self.total_fitness = self.totalFitness()

    def saveBest(self):
        best = 0
        index = 0
        for i in range(len(self.players)):
            try:
                if self.players[i].fitness > best:
                    best = self.players[i].fitness
                    index = i
            except TypeError:
                continue

        self.directions.append(copy.deepcopy(self.players[index].directions))
        fileName = "saves/lvl" + str(self.players[index].level) + ".txt"
        with open(fileName, "w") as file:
            for directions in self.players[index].directions:
                file.write("%i " % directions)

    def killWorst(self):
        least = 100
        index = 0
        for i in range(len(self.players)):
            if (self.players[i].fitness).real < least:
                least = self.players[i].fitness
                index = i

        self.players[index].kill()

    def newDirections(self):
        for i in range(self.parents_count):
            self.selection()
        self.crossover()
        self.mutation()

        for baby in self.babies:
            self.directions.append(baby)
        return self.directions

    def totalFitness(self):
        total_fitness = 0
        for i in range(len(self.players)):
            total_fitness += self.players[i].fitness
        return total_fitness

    def selection(self):
        indexes = []
        for i in range(self.parents_count):
            best = 0
            index = 0
            for j in range(len(self.players)):
                try:
                    if (self.players[j].fitness > best) and (j not in indexes):
                        best = self.players[j].fitness
                        index = j
                except TypeError:
                    continue

            self.parents.append(copy.deepcopy(self.players[index].directions))
            indexes.append(index)

    def crossover(self):
        while len(self.parents) > 0:
            baby1 = self.parents.pop()
            baby2 = self.parents.pop()

            cross_point = randint(1, self.moves - 1)
            for i in range(cross_point):
                baby1[i] = baby1[i] + baby2[i]
                baby2[i] = baby1[i] - baby2[i]
                baby1[i] = baby1[i] - baby2[i]
            self.babies.append(baby1)
            self.babies.append(baby2)

    def mutation(self):
        mutate_rate = 0.15
        for i in range(len(self.babies)):
            for j in range(len(self.babies[i])):
                rand_num = uniform(0, 1)
                if rand_num < mutate_rate:
                    self.babies[i][j] = randint(1, 9)


class Player(arcade.Sprite):
    "class for the player/s"

    def __init__(self, spawn, move_count, human, speed, coinList, goal, level):
        super().__init__("assets/PLAYER.png", 1.15)
        self.reachedCoin = False
        self.alive = True
        self.fitness = 0
        self.timer = 0
        self.level = level
        self.reachedGoal = False
        self.DotDeath = False
        self.move_count = move_count
        self.steps = 0

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
        return ((((x_2 - x_1) ** 2) + (y_2 - y_1)) ** (1 / 2))

    def calcFitness(self):
        if self.reachedGoal:
            self.fitness = 1.0 / 16.0 + 10000.0 / (self.steps * self.steps)
        else:
            approxDistance = self.distance(self.goal_x, self.goal_y)
            if self.DotDeath:
                approxDistance *= 0.9
            self.fitness = 1.0 / (approxDistance * approxDistance)
        self.fitness *= self.fitness
        if self.reachedCoin:
            self.fitness *= 1.2

    def update(self, delta_time):
        if self.alive:
            if len(self.brain.directions) > 0:
                self.move(delta_time)
            else:
                self.alive = False
        if not self.alive:
            if self.fitness == 0:
                self.calcFitness()
            self.move(delta_time)
            self.change_x = 0
            self.change_y = 0

    def move(self, delta_time):
        "move the player"
        if len(self.brain.directions) > 0:
            direction = self.brain.directions.pop()
        else:
            direction = 9
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
        self.steps += 1
