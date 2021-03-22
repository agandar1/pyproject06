#!/usr/bin/env python3
from levels import dots

mid_x = [25, 75, 125, 175, 225, 275, 325, 375, 425, 475, 525, 575, 625, 675, 725, 775, 825, 875, 925, 975]
mid_y = [25, 75, 125, 175, 225, 275, 325, 375, 425, 475, 525, 575]
int_x = [0, 50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 800, 850, 900, 950, 1000]
int_y = [0, 50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550]
angles1 = [0, dots.d90, dots.d180, dots.d270]
angles2 = [0, dots.d120, dots.d240]


def level1(game):
    "load player and dots for level 1"
    # load the player
    game.spawn_points = [(mid_x[2], mid_y[6])]
    speed = 7

    # start the dots for level 1
    # dot = dottype(list of points, speed)
    dot = dots.PathDot([(mid_x[14], mid_y[7]), (mid_x[5], mid_y[7])], speed)
    # add the dot to the dot list
    game.blue_list.append(dot)
    dot = dots.PathDot([(mid_x[14], mid_y[5]), (mid_x[5], mid_y[5])], speed)
    game.blue_list.append(dot)
    dot = dots.PathDot([(mid_x[5], mid_y[6]), (mid_x[14], mid_y[6])], speed)
    game.blue_list.append(dot)
    dot = dots.PathDot([(mid_x[5], mid_y[4]), (mid_x[14], mid_y[4])], speed)
    game.blue_list.append(dot)


def level2(game):
    "load player and dots for level 2"
    game.spawn_points = [(mid_x[2], int_y[6])]
    speed = 5

    for i in range(4, 16):
        dot = dots.PathDot([(mid_x[i], mid_y[3]), (mid_x[i], mid_y[8])], speed)
        if i % 2 != 0:
            dot = dots.PathDot([(mid_x[i], mid_y[8]), (mid_x[i], mid_y[3])], speed)
        game.blue_list.append(dot)

    coin = dots.Coin((int_x[10], int_y[6]))
    game.level_coins.append(coin)
    game.coin_list.append(coin)


def level3(game):
    "load player and dots for level 3"
    game.spawn_points = [(int_x[10], int_y[6])]
    speed = 3

    dot = dots.PathDot([(mid_x[9], mid_y[7]), (mid_x[11], mid_y[7]), (mid_x[11], mid_y[4]), (mid_x[8], mid_y[4]), (mid_x[8], mid_y[7])], speed)
    game.blue_list.append(dot)
    dot = dots.PathDot([(mid_x[10], mid_y[7]), (mid_x[11], mid_y[7]), (mid_x[11], mid_y[4]), (mid_x[8], mid_y[4]), (mid_x[8], mid_y[7])], speed)
    game.blue_list.append(dot)
    dot = dots.PathDot([(mid_x[11], mid_y[7]), (mid_x[11], mid_y[4]), (mid_x[8], mid_y[4]), (mid_x[8], mid_y[7])], speed)
    game.blue_list.append(dot)
    dot = dots.PathDot([(mid_x[11], mid_y[6]), (mid_x[11], mid_y[4]), (mid_x[8], mid_y[4]), (mid_x[8], mid_y[7]), (mid_x[11], mid_y[7])], speed)
    game.blue_list.append(dot)
    dot = dots.PathDot([(mid_x[11], mid_y[5]), (mid_x[11], mid_y[4]), (mid_x[8], mid_y[4]), (mid_x[8], mid_y[7]), (mid_x[11], mid_y[7])], speed)
    game.blue_list.append(dot)
    dot = dots.PathDot([(mid_x[11], mid_y[4]), (mid_x[8], mid_y[4]), (mid_x[8], mid_y[7]), (mid_x[11], mid_y[7])], speed)
    game.blue_list.append(dot)
    dot = dots.PathDot([(mid_x[10], mid_y[4]), (mid_x[8], mid_y[4]), (mid_x[8], mid_y[7]), (mid_x[11], mid_y[7]), (mid_x[11], mid_y[4])], speed)
    game.blue_list.append(dot)
    dot = dots.PathDot([(mid_x[9], mid_y[4]), (mid_x[8], mid_y[4]), (mid_x[8], mid_y[7]), (mid_x[11], mid_y[7]), (mid_x[11], mid_y[4])], speed)
    game.blue_list.append(dot)
    dot = dots.PathDot([(mid_x[8], mid_y[4]), (mid_x[8], mid_y[7]), (mid_x[11], mid_y[7]), (mid_x[11], mid_y[4])], speed)
    game.blue_list.append(dot)
    dot = dots.PathDot([(mid_x[8], mid_y[5]), (mid_x[8], mid_y[7]), (mid_x[11], mid_y[7]), (mid_x[11], mid_y[4]), (mid_x[8], mid_y[4])], speed)
    game.blue_list.append(dot)
    dot = dots.PathDot([(mid_x[8], mid_y[6]), (mid_x[8], mid_y[7]), (mid_x[11], mid_y[7]), (mid_x[11], mid_y[4]), (mid_x[8], mid_y[4])], speed)
    game.blue_list.append(dot)

    coin = dots.Coin((mid_x[8], mid_y[8]))
    game.level_coins.append(coin)
    game.coin_list.append(coin)


def level4(game):
    "load player and dots for level 4"
    game.spawn_points = [(int_x[10], int_y[10])]
    speed = 0.035
    radiuses = [35, 70, 105, 140, 175]
    coins = [(int_x[10], int_y[8]),
             (int_x[13], int_y[5]),
             (int_x[10], int_y[2])]

    dot = dots.PathDot([(int_x[10], int_y[5]), (int_x[10], int_y[5])], speed)
    game.blue_list.append(dot)
    for radius in radiuses:
        for angle in angles1:
            dot = dots.CircleDot((int_x[10], int_y[5]), radius, angle, speed)
            game.blue_list.append(dot)

    for coinPoint in coins:
        coin = dots.Coin(coinPoint)
        game.level_coins.append(coin)
        game.coin_list.append(coin)


def level5(game):
    "load player and dots for level 5"
    game.spawn_points = [(int_x[2], mid_y[10]),
                         (mid_x[17], mid_y[10]),
                         (mid_x[1], mid_y[8])]
    speed = 0.025
    radiuses = [75, 175, 275, 375]

    for radius in radiuses:
        for angle in angles1:
            dot = dots.CircleDot((int_x[10], int_y[6]), radius, angle, speed)
            game.blue_list.append(dot)


def level6(game):
    "load player and dots for level 6"
    game.spawn_points = [(int_x[3], int_y[8]), (int_x[17], int_x[6])]
    speed = 0.035
    radiuses = [30, 60, 90]
    coins = [(mid_x[2], mid_y[5]),
             (mid_x[6], mid_y[5]),
             (mid_x[10], mid_y[5]),
             (mid_x[14], mid_y[5])]

    centers = [(int_x[8], int_y[9]),
               (int_x[12], int_y[9]),
               (int_x[16], int_y[9]),
               (int_x[4], int_y[3]),
               (int_x[8], int_y[3]),
               (int_x[12], int_y[3]),
               (int_x[16], int_y[3])]

    # Center dots
    for center in centers:
        dot = dots.PathDot([center, center], speed)
        game.blue_list.append(dot)

    # Rotating dots
    for radius in radiuses:
        for angle in angles2:
            for i, center in enumerate(centers):
                if i % 2 == 0:
                    dot = dots.CircleDot(center, radius, angle, speed)
                else:
                    dot = dots.CircleDot(center, radius, angle + dots.d60, speed, 0)
                game.blue_list.append(dot)

    for coinPoint in coins:
        coin = dots.Coin(coinPoint)
        game.level_coins.append(coin)
        game.coin_list.append(coin)
