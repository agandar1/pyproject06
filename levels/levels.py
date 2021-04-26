#!/usr/bin/env python3
from levels import dots

mid_x = [25, 75, 125, 175, 225, 275, 325, 375, 425, 475, 525, 575, 625, 675, 725, 775, 825, 875, 925, 975]
mid_y = [25, 75, 125, 175, 225, 275, 325, 375, 425, 475, 525, 575]
int_x = [0, 50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 800, 850, 900, 950, 1000]
int_y = [0, 50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550]
float_x = [0, 25, 50, 75, 100, 125, 150, 175, 200, 225, 250, 275, 300, 325, 350, 375, 400, 425, 450, 475, 500, 525, 550,
           575, 600, 625, 650, 675, 700, 725, 750, 775, 800, 825, 850, 875, 900, 925, 950, 975, 1000]
float_y = [0, 25, 50, 75, 100, 125, 150, 175, 200, 225, 250, 275, 300, 325, 350, 375, 400, 425, 450, 475, 500, 525, 550,
           575, 600, 625, 650, 675, 700, 725, 750, 775, 800, 825, 850, 875, 900, 925, 950, 975, 1000]
angles1 = [0, dots.d90, dots.d180, dots.d270]
angles2 = [0, dots.d120, dots.d240]

goals = [
    (mid_x[16], mid_y[5]),  # 1
    (mid_x[16], int_y[6]),  # 2
    (mid_x[10], int_y[6]),  # 3
    (mid_x[5], int_y[5]),  # 4
    (mid_x[12], int_y[6]),  # 5
    (mid_x[16], int_y[6]),  # 6
    (mid_x[16], int_y[6]),  # 7
    (mid_x[14], int_y[6]),  # 8
    (int_x[18], int_y[6]),  # 9
    (mid_x[11], int_y[10]),  # 10
    (int_x[3], int_y[5]),  # 11
    (int_x[3], int_y[4]),  # 12
    (int_x[10], int_y[10]),  # 13
    (mid_x[16], mid_y[6]),  # 14
]

speeds = [
    (6, 0.21),
    (5, 0.15),
    (3, 0.08),
    (0.035, 0.0012),
    (0.025, 0.08),
    (0.035, 0.08),
    (7, 0.08),
    (4, 0.08),
    (5, 0.08),
    (1, 0.08),
    (3, 0.08),
    (2, 0.08),
    (5, 0.08),
    (2, 0.08),
]


def level1(game):
    "load player and dots for level 1"
    # load the player
    game.spawn_points = [(mid_x[2], mid_y[6])]
    if game.human or game.watching:
        speed = speeds[game.level - 1][0]
    else:
        speed = speeds[game.level - 1][1]

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
    if game.human or game.watching:
        speed = speeds[game.level - 1][0]
    else:
        speed = speeds[game.level - 1][1]
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
    if game.human or game.watching:
        speed = speeds[game.level - 1][0]
    else:
        speed = speeds[game.level - 1][1]

    dot = dots.PathDot([(mid_x[9], mid_y[7]), (mid_x[11], mid_y[7]), (mid_x[11], mid_y[4]), (mid_x[8], mid_y[4]),
                        (mid_x[8], mid_y[7])], speed)
    game.blue_list.append(dot)
    dot = dots.PathDot([(mid_x[10], mid_y[7]), (mid_x[11], mid_y[7]), (mid_x[11], mid_y[4]), (mid_x[8], mid_y[4]),
                        (mid_x[8], mid_y[7])], speed)
    game.blue_list.append(dot)
    dot = dots.PathDot([(mid_x[11], mid_y[7]), (mid_x[11], mid_y[4]), (mid_x[8], mid_y[4]), (mid_x[8], mid_y[7])],
                       speed)
    game.blue_list.append(dot)
    dot = dots.PathDot([(mid_x[11], mid_y[6]), (mid_x[11], mid_y[4]), (mid_x[8], mid_y[4]), (mid_x[8], mid_y[7]),
                        (mid_x[11], mid_y[7])], speed)
    game.blue_list.append(dot)
    dot = dots.PathDot([(mid_x[11], mid_y[5]), (mid_x[11], mid_y[4]), (mid_x[8], mid_y[4]), (mid_x[8], mid_y[7]),
                        (mid_x[11], mid_y[7])], speed)
    game.blue_list.append(dot)
    dot = dots.PathDot([(mid_x[11], mid_y[4]), (mid_x[8], mid_y[4]), (mid_x[8], mid_y[7]), (mid_x[11], mid_y[7])],
                       speed)
    game.blue_list.append(dot)
    dot = dots.PathDot([(mid_x[10], mid_y[4]), (mid_x[8], mid_y[4]), (mid_x[8], mid_y[7]), (mid_x[11], mid_y[7]),
                        (mid_x[11], mid_y[4])], speed)
    game.blue_list.append(dot)
    dot = dots.PathDot([(mid_x[9], mid_y[4]), (mid_x[8], mid_y[4]), (mid_x[8], mid_y[7]), (mid_x[11], mid_y[7]),
                        (mid_x[11], mid_y[4])], speed)
    game.blue_list.append(dot)
    dot = dots.PathDot([(mid_x[8], mid_y[4]), (mid_x[8], mid_y[7]), (mid_x[11], mid_y[7]), (mid_x[11], mid_y[4])],
                       speed)
    game.blue_list.append(dot)
    dot = dots.PathDot([(mid_x[8], mid_y[5]), (mid_x[8], mid_y[7]), (mid_x[11], mid_y[7]), (mid_x[11], mid_y[4]),
                        (mid_x[8], mid_y[4])], speed)
    game.blue_list.append(dot)
    dot = dots.PathDot([(mid_x[8], mid_y[6]), (mid_x[8], mid_y[7]), (mid_x[11], mid_y[7]), (mid_x[11], mid_y[4]),
                        (mid_x[8], mid_y[4])], speed)
    game.blue_list.append(dot)

    coin = dots.Coin((mid_x[8], mid_y[8]))
    game.level_coins.append(coin)
    game.coin_list.append(coin)


def level4(game):
    "load player and dots for level 4"

    if game.human or game.watching:
        speed = speeds[game.level - 1][0]
    else:
        speed = speeds[game.level - 1][1]

    game.spawn_points = [(int_x[10], int_y[10])]

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

    if game.human or game.watching:
        speed = speeds[game.level - 1][0]
    else:
        speed = speeds[game.level - 1][1]

    game.spawn_points = [(int_x[2], mid_y[10]),
                         (mid_x[17], mid_y[10]),
                         (mid_x[1], mid_y[8])]

    radiuses = [75, 175, 275, 375]

    for radius in radiuses:
        for angle in angles1:
            dot = dots.CircleDot((int_x[10], int_y[6]), radius, angle, speed)
            game.blue_list.append(dot)


def level6(game):
    "load player and dots for level 6"

    if game.human or game.watching:
        speed = speeds[game.level - 1][0]
    else:
        speed = speeds[game.level - 1][1]

    game.spawn_points = [(int_x[3], int_y[8]), (int_x[17], int_x[6])]

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


def level7(game):
    "load player and dots for level 7"

    if game.human or game.watching:
        speed = speeds[game.level - 1][0]
    else:
        speed = speeds[game.level - 1][1]

    game.spawn_points = [(mid_x[2], int_y[6])]

    for i in range(4, 16):
        dot = dots.PathDot([(mid_x[i], mid_y[2]), (mid_x[i], mid_y[9])], speed)
        if i % 2 != 0:
            dot = dots.PathDot([(mid_x[i], mid_y[9]), (mid_x[i], mid_y[2])], speed)
        game.blue_list.append(dot)

    coins = [(mid_x[4], mid_y[2]),
             (mid_x[4], mid_y[9]),
             (mid_x[15], mid_y[2]),
             (mid_x[15], mid_y[9])]

    for coinPoint in coins:
        coin = dots.Coin(coinPoint)
        game.level_coins.append(coin)
        game.coin_list.append(coin)


def level8(game):
    "load player and dots for level 8"

    if game.human or game.watching:
        speed = speeds[game.level - 1][0]
    else:
        speed = speeds[game.level - 1][1]

    game.spawn_points = [(mid_x[5], mid_y[9])]

    dot = dots.PathDot([(mid_x[7], mid_y[9]), (mid_x[10], mid_y[9]), (mid_x[10], mid_y[2]), (mid_x[7], mid_y[2])],
                       speed)
    game.blue_list.append(dot)

    for i in range(1, 8, 3):
        dot = dots.PathDot(
            [(mid_x[4], mid_y[i + 3]), (mid_x[7], mid_y[i + 3]), (mid_x[7], mid_y[i]), (mid_x[4], mid_y[i])], speed)
        game.blue_list.append(dot)
        dot = dots.PathDot(
            [(mid_x[13], mid_y[i + 3]), (mid_x[10], mid_y[i + 3]), (mid_x[10], mid_y[i]), (mid_x[13], mid_y[i])], speed)
        game.blue_list.append(dot)

    coins = [(mid_x[4], mid_y[1]),
             (mid_x[13], mid_y[1]),
             (mid_x[13], mid_y[10])]

    for coinPoint in coins:
        coin = dots.Coin(coinPoint)
        game.level_coins.append(coin)
        game.coin_list.append(coin)


def level9(game):
    "load player and dots for level 9"

    if game.human or game.watching:
        speed = speeds[game.level - 1][0]
    else:
        speed = speeds[game.level - 1][1]

    game.spawn_points = [(int_x[2], int_y[10]), (int_x[10], int_y[4])]

    # Square rotation
    x_rotate = [5, 9, 1, 5, 17]
    y_rotate = [8, 10, 2, 2, 10]
    control = 0
    for i in x_rotate:
        y_cordinate = y_rotate[control]
        dot = dots.PathDot(
            [(mid_x[i], mid_y[y_cordinate]), (mid_x[i + 1], mid_y[y_cordinate]), (mid_x[i + 1], mid_y[y_cordinate - 1]),
             (mid_x[i], mid_y[y_cordinate - 1])],
            speed)
        game.blue_list.append(dot)
        control += 1

    # Square rotating different timing
    x_rotate = [1, 13, 13]
    y_rotate = [8, 10, 4]
    control = 0

    for i in x_rotate:
        y_cordinate = y_rotate[control]
        dot = dots.PathDot(
            [(mid_x[i + 1], mid_y[y_cordinate - 1]), (mid_x[i], mid_y[y_cordinate - 1]), (mid_x[i], mid_y[y_cordinate]),
             (mid_x[i + 1], mid_y[y_cordinate])],
            speed)
        game.blue_list.append(dot)
        control += 1

    # Non moving dots int_y
    x_static = [2, 13, 5, 5, 9, 1, 13, 14, 17]
    y_static = [6, 2, 4, 10, 8, 4, 6, 8, 8]
    control = 0

    for i in x_static:
        y_cordinate = y_static[control]
        dot = dots.PathDot([(mid_x[i], int_y[y_cordinate]), (mid_x[i], int_y[y_cordinate])], speed)
        game.blue_list.append(dot)
        control += 1

    # Non moving dots int_x

    x_static = [4, 7, 8, 4, 16]
    y_static = [8, 4, 9, 2, 9]
    control = 0

    for i in x_static:
        y_cordinate = y_static[control]
        dot = dots.PathDot([(int_x[i], mid_y[y_cordinate]), (int_x[i], mid_y[y_cordinate])], speed)
        game.blue_list.append(dot)
        control += 1

    # L movement
    dot = dots.PathDot(
        [(mid_x[10], int_y[8]), (mid_x[10], mid_y[5]), (mid_x[9], mid_y[5]), (mid_x[10], mid_y[5])], speed)
    game.blue_list.append(dot)

    dot = dots.PathDot(
        [(mid_x[14], mid_y[2]), (int_x[17], mid_y[2]), (int_x[17], mid_y[1]), (int_x[17], mid_y[2])], speed)
    game.blue_list.append(dot)

    coin = dots.Coin((int_x[18], int_y[2]))
    game.level_coins.append(coin)
    game.coin_list.append(coin)


def level10(game):
    "load player and dots for level 10"
    if game.human or game.watching:
        speed = speeds[game.level - 1][0]
    else:
        speed = speeds[game.level - 1][1]

    game.spawn_points = [(int_x[9], int_y[10]), (int_x[10], int_y[4])]

    x_rotate = [7, 7, 5, 5, 10, 10, 12]
    y_rotate = [7, 5, 4, 2, 7, 5, 3]
    control = 0

    # Lef to right
    for i in x_rotate:
        y_cordinate = y_rotate[control]
        dot = dots.PathDot(
            [(mid_x[i], mid_y[y_cordinate]), (mid_x[i + 1], mid_y[y_cordinate]), (mid_x[i], mid_y[y_cordinate]),
             (mid_x[i + 1], mid_y[y_cordinate])],
            speed)
        game.blue_list.append(dot)
        control += 1

    # Right to left

    x_rotate = [5, 7, 7, 12, 12, 10, 10]
    y_rotate = [3, 4, 6, 4, 2, 4, 6]
    control = 0

    for i in x_rotate:
        y_cordinate = y_rotate[control]
        dot = dots.PathDot(
            [(mid_x[i + 1], mid_y[y_cordinate]), (mid_x[i], mid_y[y_cordinate]), (mid_x[i + 1], mid_y[y_cordinate]),
             (mid_x[i], mid_y[y_cordinate])],
            speed)
        game.blue_list.append(dot)
        control += 1

    # Up and Down

    x_rotate = [7, 9, 11]
    y_rotate = [1, 1, 1]
    control = 0

    for i in x_rotate:
        y_cordinate = y_rotate[control]
        dot = dots.PathDot(
            [(mid_x[i], mid_y[y_cordinate + 1]), (mid_x[i], mid_y[y_cordinate]), (mid_x[i], mid_y[y_cordinate + 1]),
             (mid_x[i], mid_y[y_cordinate])],
            speed)
        game.blue_list.append(dot)
        control += 1

    # Down and Up

    x_rotate = [8, 10]
    y_rotate = [1, 1]
    control = 0

    for i in x_rotate:
        y_cordinate = y_rotate[control]
        dot = dots.PathDot(
            [(mid_x[i], mid_y[y_cordinate]), (mid_x[i], mid_y[y_cordinate + 1]), (mid_x[i], mid_y[y_cordinate]),
             (mid_x[i], mid_y[y_cordinate + 1])],
            speed)
        game.blue_list.append(dot)
        control += 1


def level11(game):
    "load player and dots for level 11"
    if game.human or game.watching:
        speed = speeds[game.level - 1][0]
    else:
        speed = speeds[game.level - 1][1]

    game.spawn_points = [(int_x[17], int_y[7])]

    x_rotate = [6, 8, 10, 12]
    y_rotate = [3, 3, 3, 3]
    control = 0

    # down up

    for i in x_rotate:
        y_cordinate = y_rotate[control]
        dot = dots.PathDot(
            [(mid_x[i], int_y[y_cordinate]), (mid_x[i], int_y[y_cordinate + 7]), (mid_x[i], int_y[y_cordinate]),
             (mid_x[i], int_y[y_cordinate + 7])],
            speed)
        game.blue_list.append(dot)
        control += 1

    # up down
    x_rotate = [7, 9, 11, 13]
    y_rotate = [10, 10, 10, 10]
    control = 0

    for i in x_rotate:
        y_cordinate = y_rotate[control]
        dot = dots.PathDot(
            [(mid_x[i], int_y[y_cordinate]), (mid_x[i], int_y[y_cordinate - 7]), (mid_x[i], int_y[y_cordinate]),
             (mid_x[i], int_y[y_cordinate - 7])],
            speed)
        game.blue_list.append(dot)
        control += 1

    # Left right

    x_rotate = [6, 6, 6, 6]
    y_rotate = [9, 7, 5, 3]
    control = 0

    for i in x_rotate:
        y_cordinate = y_rotate[control]
        dot = dots.PathDot(
            [(mid_x[i], mid_y[y_cordinate]), (mid_x[i + 7], mid_y[y_cordinate]), (mid_x[i], mid_y[y_cordinate]),
             (mid_x[i + 7], mid_y[y_cordinate])],
            speed)
        game.blue_list.append(dot)
        control += 1

    # right to left

    x_rotate = [13, 13, 13]
    y_rotate = [8, 6, 4]
    control = 0

    for i in x_rotate:
        y_cordinate = y_rotate[control]
        dot = dots.PathDot(
            [(mid_x[i], mid_y[y_cordinate]), (mid_x[i - 7], mid_y[y_cordinate]), (mid_x[i], mid_y[y_cordinate]),
             (mid_x[i - 7], mid_y[y_cordinate])],
            speed)
        game.blue_list.append(dot)
        control += 1

    coins = [(mid_x[6], int_y[6]),
             (int_x[10], mid_y[9]),
             (mid_x[13], int_y[6]),
             (int_x[10], mid_y[2])]

    for coinPoint in coins:
        coin = dots.Coin(coinPoint)
        game.level_coins.append(coin)
        game.coin_list.append(coin)


def level12(game):
    "load player and dots for level 12"
    if game.human or game.watching:
        speed = speeds[game.level - 1][0]
    else:
        speed = speeds[game.level - 1][1]

    game.spawn_points = [(int_x[17], int_y[4]), (int_x[3], int_y[8])]

    # Non moving dots float_x

    x_static = [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
                31, 32, 33, 34, 35,

                4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
                31, 32, 33, 34, 35,
                ]

    y_static = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3,
                9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9]

    control = 0

    for i in x_static:
        y_cordinate = y_static[control]
        dot = dots.PathDot([(float_x[i], int_y[y_cordinate]), (float_x[i], int_y[y_cordinate])], speed)
        game.blue_list.append(dot)
        control += 1

    # Non moving dots int_x float_y

    x_static = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
                18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18
                ]

    y_static = [7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18,
                6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18
                ]

    control = 0

    for i in x_static:
        y_cordinate = y_static[control]
        dot = dots.PathDot([(int_x[i], float_y[y_cordinate]), (int_x[i], float_y[y_cordinate])], speed)
        game.blue_list.append(dot)
        control += 1

    # Trying weird stuff

    x_static = [4, 5, 6, 7, 8, 9, 10, 11, 12,
                13, 14, 15, 16, 17, 18,

                9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21,
                15, 16, 17, 18, 19, 20, 21,
                19, 20, 21,
                19, 20, 21,
                5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21,

                24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35,
                24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35,
                24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35,
                24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35,
                24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35,
                24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35,
                24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35,
                26, 27, 28, 29, 30, 31, 32,
                29, 30,

                15, 16,
                9, 10, 11,
                9,
                22, 23,
                19, 20, 21, 22, 23, 24, 25, 26
                ]

    y_static = [
        12, 12, 12, 12, 12, 12, 12, 12, 12,
        10, 10, 10, 10, 10, 10,

        15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15,
        14, 14, 14, 14, 14, 14, 14,
        13, 13, 13,
        12, 12, 12,
        11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11,

        17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17,
        16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16,
        15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15,
        14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14,
        13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13,
        12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12,
        11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11,
        10, 10, 10, 10, 10, 10, 10,
        9, 9,

        9, 9,
        7, 7, 7,
        8,
        8, 8,
        7, 7, 7, 7, 7, 7, 7, 7

    ]

    control = 0

    for i in x_static:
        y_cordinate = y_static[control]
        dot = dots.PathDot([(float_x[i], float_y[y_cordinate]), (float_x[i], float_y[y_cordinate])], speed)
        game.blue_list.append(dot)
        control += 1

    # up down
    x_rotate = [22, 23, 11, 12]
    y_rotate = [6, 6, 6, 6]
    control = 0

    for i in x_rotate:
        y_cordinate = y_rotate[control]
        dot = dots.PathDot(
            [(float_x[i], float_y[y_cordinate]), (float_x[i], float_y[y_cordinate + 12]),
             (float_x[i], float_y[y_cordinate]),
             (float_x[i], float_y[y_cordinate + 12])],
            speed)
        game.blue_list.append(dot)
        control += 1

    # down up
    x_rotate = [17, 18, 29, 30]
    y_rotate = [18, 18, 18, 18]
    control = 0

    for i in x_rotate:
        y_cordinate = y_rotate[control]
        dot = dots.PathDot(
            [(float_x[i], float_y[y_cordinate]), (float_x[i], float_y[y_cordinate - 12]),
             (float_x[i], float_y[y_cordinate]),
             (float_x[i], float_y[y_cordinate - 12])],
            speed)
        game.blue_list.append(dot)
        control += 1

    coin = dots.Coin((float_x[17], mid_y[6]))
    game.level_coins.append(coin)
    game.coin_list.append(coin)


def level13(game):
    "load player and dots for level 13"
    if game.human or game.watching:
        speed = speeds[game.level - 1][0]
    else:
        speed = speeds[game.level - 1][1]

    game.spawn_points = [(int_x[10], int_y[2])]

    x_rotate = [5, 7, 9, 11, 13]
    y_rotate = [8, 8, 8, 8, 8]
    control = 0

    for i in x_rotate:
        y_cordinate = y_rotate[control]
        dot = dots.PathDot(
            [(mid_x[i], mid_y[y_cordinate]), (mid_x[i], mid_y[y_cordinate - 5]), (mid_x[i], mid_y[y_cordinate]),
             (mid_x[i], mid_y[y_cordinate - 5])],
            speed)
        game.blue_list.append(dot)
        control += 1

    x_rotate = [6, 8, 10, 12, 14]
    y_rotate = [3, 3, 3, 3, 3]
    control = 0

    for i in x_rotate:
        y_cordinate = y_rotate[control]
        dot = dots.PathDot(
            [(mid_x[i], mid_y[y_cordinate]), (mid_x[i], mid_y[y_cordinate + 5]), (mid_x[i], mid_y[y_cordinate]),
             (mid_x[i], mid_y[y_cordinate + 5])],
            speed)
        game.blue_list.append(dot)
        control += 1

    dot = dots.PathDot(
        [(mid_x[5], mid_y[6]), (mid_x[14], mid_y[6]), (mid_x[5], mid_y[6]),
         (mid_x[14], mid_y[6])],
        speed)
    game.blue_list.append(dot)

    dot = dots.PathDot(
        [(mid_x[14], mid_y[5]), (mid_x[5], mid_y[5]), (mid_x[14], mid_y[5]),
         (mid_x[5], mid_y[5])],
        speed)
    game.blue_list.append(dot)


def level14(game):
    "load player and dots for level 14"
    if game.human or game.watching:
        speed = speeds[game.level - 1][0]
    else:
        speed = speeds[game.level - 1][1]

    game.spawn_points = [(mid_x[2], mid_y[4])]

    x_rotate = [7, 7, 15 ,15]
    y_rotate = [12, 11, 12, 11]
    control = 0

    for i in x_rotate:
        y_cordinate = y_rotate[control]
        dot = dots.PathDot(
            [(mid_x[i], float_y[y_cordinate]), (mid_x[i], float_y[y_cordinate - 5]), (mid_x[i], float_y[y_cordinate]),
             (mid_x[i], float_y[y_cordinate - 5])],
            speed)
        game.blue_list.append(dot)
        control += 1


    x_rotate = [11, 11]
    y_rotate = [7, 6]
    control = 0
    for i in x_rotate:
        y_cordinate = y_rotate[control]
        dot = dots.PathDot(
            [(mid_x[i], float_y[y_cordinate]), (mid_x[i], float_y[y_cordinate + 5]), (mid_x[i], float_y[y_cordinate]),
             (mid_x[i], float_y[y_cordinate + 5])],
            speed)
        game.blue_list.append(dot)
        control += 1


    x_static = [5, 9, 13, 17]
    y_static = [4, 4, 4, 4]
    control = 0

    for i in x_static:
        y_cordinate = y_static[control]
        dot = dots.PathDot([(mid_x[i], mid_y[y_cordinate]), (mid_x[i], mid_y[y_cordinate])], speed)
        game.blue_list.append(dot)
        control += 1

    speed = 0.05
    radiuses = [60, 30]

    centers = [(mid_x[5], mid_y[4]),
               (mid_x[9], mid_y[4]),
               (mid_x[13], mid_y[4]),
               (mid_x[17], mid_y[4])
               ]

    for radius in radiuses:
        for angle in angles2:
            for i, center in enumerate(centers):
                dot = dots.CircleDot(center, radius, angle, speed)
                game.blue_list.append(dot)
