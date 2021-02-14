#!/usr/bin/env python3
import math
import arcade

d90 = math.pi / 2
d180 = math.pi
d270 = math.pi + (math.pi / 2)


class CircleDot(arcade.Sprite):
    "blue dots that go in a circle"
    def __init__(self, centerPoint, radius, angle, speed):
        "constructor"
        super().__init__("assets/BLUE_DOT.png", 1)
        self.circle_angle = angle
        self.circle_radius = radius
        self.circle_speed = speed
        self.circle_center_x = centerPoint[0]
        self.circle_center_y = centerPoint[1]

    def update(self):
        "update the dot's position"
        self.center_x = self.circle_radius * math.sin(self.circle_angle) + self.circle_center_x
        self.center_y = self.circle_radius * math.cos(self.circle_angle) + self.circle_center_y

        self.circle_angle += self.circle_speed


class PathDot(arcade.Sprite):
    "blue dots that follow a path"
    def __init__(self, pointList, speed):
        super().__init__("assets/BLUE_DOT.png", 1)
        self.pointList = pointList
        self.centerPoint = [self.pointList[0][0], self.pointList[0][1]]
        self.counter = 1
        self.goal = pointList[1]
        self.speed = speed
        self.setCenter()

    def setCenter(self):
        "set the center coordinates for the dot"
        self.center_x = self.centerPoint[0]
        self.center_y = self.centerPoint[1]

    def update(self):
        "move the dot"
        for i in range(2):
            if self.centerPoint[i] > self.goal[i]:
                self.centerPoint[i] -= self.speed
            elif self.centerPoint[i] < self.goal[i]:
                self.centerPoint[i] += self.speed
            if 0 < abs(self.centerPoint[i] - self.goal[i]) < self.speed + 1:
                self.centerPoint[i] = self.goal[i]
                self.counter += 1
                self.goal = self.pointList[self.counter % len(self.pointList)]
        self.setCenter()


class Coin(arcade.Sprite):
    "yellow dots that dont move"
    def __init__(self, centerPoint):
        super().__init__("assets/YELLOW_DOT.png", 1)
        self.center_x = centerPoint[0]
        self.center_y = centerPoint[1]
