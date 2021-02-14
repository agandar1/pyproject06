#!/usr/bin/env python3
import math
import arcade

WIDTH = 1000
HEIGHT = 600
mid_x = [25, 75, 125, 175, 225, 275, 325, 375, 425, 475, 525, 575, 625, 675, 725, 775, 825, 875, 925, 975]
mid_y = [25, 75, 125, 175, 225, 275, 325, 375, 425, 475, 525, 575]
int_x = [0, 50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 800, 850, 900, 950, 1000]
int_y = [0, 50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550]


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


class MyGameWindow(arcade.Window):
    "control game window"
    # sprite lists
    empty_list = None
    goal_list = None
    wall_list = None
    checkpoint_list = None
    player_list = None
    blue_list = None
    coin_list = None
    level_coins = None

    # setup player
    spawn_points = None
    p_speed = 175
    deaths = 0
    player_sprite = None

    # movement
    right = False
    left = False
    up = False
    down = False

    # game variables
    game_over = False
    level = 1
    max_level = 30

    physics_engine = None

    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.set_location(400, 200)
        self.setup()

    def level1(self):
        "load player and dots for level 1"
        # load the player
        self.spawn_points = [(mid_x[2], mid_y[6])]
        speed = 7

        # start the dots for level 1
        # dot = dottype(list of points, speed)
        dot = PathDot([(mid_x[14], mid_y[7]), (mid_x[5], mid_y[7])], speed)
        # add the dot to the dot list
        self.blue_list.append(dot)
        dot = PathDot([(mid_x[14], mid_y[5]), (mid_x[5], mid_y[5])], speed)
        self.blue_list.append(dot)
        dot = PathDot([(mid_x[5], mid_y[6]), (mid_x[14], mid_y[6])], speed)
        self.blue_list.append(dot)
        dot = PathDot([(mid_x[5], mid_y[4]), (mid_x[14], mid_y[4])], speed)
        self.blue_list.append(dot)

    def level2(self):
        "load player and dots for level 2"
        self.spawn_points = [(mid_x[2], int_y[6])]
        speed = 5

        dot = PathDot([(mid_x[4], mid_y[3]), (mid_x[4], mid_y[8])], speed)
        self.blue_list.append(dot)
        dot = PathDot([(mid_x[6], mid_y[3]), (mid_x[6], mid_y[8])], speed)
        self.blue_list.append(dot)
        dot = PathDot([(mid_x[8], mid_y[3]), (mid_x[8], mid_y[8])], speed)
        self.blue_list.append(dot)
        dot = PathDot([(mid_x[10], mid_y[3]), (mid_x[10], mid_y[8])], speed)
        self.blue_list.append(dot)
        dot = PathDot([(mid_x[12], mid_y[3]), (mid_x[12], mid_y[8])], speed)
        self.blue_list.append(dot)
        dot = PathDot([(mid_x[14], mid_y[3]), (mid_x[14], mid_y[8])], speed)
        self.blue_list.append(dot)
        dot = PathDot([(mid_x[5], mid_y[8]), (mid_x[5], mid_y[3])], speed)
        self.blue_list.append(dot)
        dot = PathDot([(mid_x[7], mid_y[8]), (mid_x[7], mid_y[3])], speed)
        self.blue_list.append(dot)
        dot = PathDot([(mid_x[9], mid_y[8]), (mid_x[9], mid_y[3])], speed)
        self.blue_list.append(dot)
        dot = PathDot([(mid_x[11], mid_y[8]), (mid_x[11], mid_y[3])], speed)
        self.blue_list.append(dot)
        dot = PathDot([(mid_x[13], mid_y[8]), (mid_x[13], mid_y[3])], speed)
        self.blue_list.append(dot)
        dot = PathDot([(mid_x[15], mid_y[8]), (mid_x[15], mid_y[3])], speed)
        self.blue_list.append(dot)

        coin = Coin((int_x[10], int_y[6]))
        self.level_coins.append(coin)
        self.coin_list.append(coin)

    def level3(self):
        "load player and dots for level 3"
        self.spawn_points = [(int_x[10], int_y[6])]
        speed = 3

        dot = PathDot([(mid_x[9], mid_y[7]), (mid_x[11], mid_y[7]), (mid_x[11], mid_y[4]), (mid_x[8], mid_y[4]), (mid_x[8], mid_y[7])], speed)
        self.blue_list.append(dot)
        dot = PathDot([(mid_x[10], mid_y[7]), (mid_x[11], mid_y[7]), (mid_x[11], mid_y[4]), (mid_x[8], mid_y[4]), (mid_x[8], mid_y[7])], speed)
        self.blue_list.append(dot)
        dot = PathDot([(mid_x[11], mid_y[7]), (mid_x[11], mid_y[4]), (mid_x[8], mid_y[4]), (mid_x[8], mid_y[7])], speed)
        self.blue_list.append(dot)
        dot = PathDot([(mid_x[11], mid_y[6]), (mid_x[11], mid_y[4]), (mid_x[8], mid_y[4]), (mid_x[8], mid_y[7]), (mid_x[11], mid_y[7])], speed)
        self.blue_list.append(dot)
        dot = PathDot([(mid_x[11], mid_y[5]), (mid_x[11], mid_y[4]), (mid_x[8], mid_y[4]), (mid_x[8], mid_y[7]), (mid_x[11], mid_y[7])], speed)
        self.blue_list.append(dot)
        dot = PathDot([(mid_x[11], mid_y[4]), (mid_x[8], mid_y[4]), (mid_x[8], mid_y[7]), (mid_x[11], mid_y[7])], speed)
        self.blue_list.append(dot)
        dot = PathDot([(mid_x[10], mid_y[4]), (mid_x[8], mid_y[4]), (mid_x[8], mid_y[7]), (mid_x[11], mid_y[7]), (mid_x[11], mid_y[4])], speed)
        self.blue_list.append(dot)
        dot = PathDot([(mid_x[9], mid_y[4]), (mid_x[8], mid_y[4]), (mid_x[8], mid_y[7]), (mid_x[11], mid_y[7]), (mid_x[11], mid_y[4])], speed)
        self.blue_list.append(dot)
        dot = PathDot([(mid_x[8], mid_y[4]), (mid_x[8], mid_y[7]), (mid_x[11], mid_y[7]), (mid_x[11], mid_y[4])], speed)
        self.blue_list.append(dot)
        dot = PathDot([(mid_x[8], mid_y[5]), (mid_x[8], mid_y[7]), (mid_x[11], mid_y[7]), (mid_x[11], mid_y[4]), (mid_x[8], mid_y[4])], speed)
        self.blue_list.append(dot)
        dot = PathDot([(mid_x[8], mid_y[6]), (mid_x[8], mid_y[7]), (mid_x[11], mid_y[7]), (mid_x[11], mid_y[4]), (mid_x[8], mid_y[4])], speed)
        self.blue_list.append(dot)

        coin = Coin((mid_x[8], mid_y[8]))
        self.level_coins.append(coin)
        self.coin_list.append(coin)

    def level4(self):
        "load player and dots for level 4"
        self.spawn_points = [(int_x[10], int_y[10])]
        speed = 0.035
        d90 = math.pi / 2
        d180 = math.pi
        d270 = math.pi + (math.pi / 2)

        dot = PathDot([(int_x[10], int_y[5]), (int_x[10], int_y[5])], speed)
        self.blue_list.append(dot)
        dot = CircleDot((int_x[10], int_y[5]), 35, 0, speed)
        self.blue_list.append(dot)
        dot = CircleDot((int_x[10], int_y[5]), 35, d90, speed)
        self.blue_list.append(dot)
        dot = CircleDot((int_x[10], int_y[5]), 35, d180, speed)
        self.blue_list.append(dot)
        dot = CircleDot((int_x[10], int_y[5]), 35, d270, speed)
        self.blue_list.append(dot)
        dot = CircleDot((int_x[10], int_y[5]), 70, 0, speed)
        self.blue_list.append(dot)
        dot = CircleDot((int_x[10], int_y[5]), 70, d90, speed)
        self.blue_list.append(dot)
        dot = CircleDot((int_x[10], int_y[5]), 70, d180, speed)
        self.blue_list.append(dot)
        dot = CircleDot((int_x[10], int_y[5]), 70, d270, speed)
        self.blue_list.append(dot)
        dot = CircleDot((int_x[10], int_y[5]), 105, 0, speed)
        self.blue_list.append(dot)
        dot = CircleDot((int_x[10], int_y[5]), 105, d90, speed)
        self.blue_list.append(dot)
        dot = CircleDot((int_x[10], int_y[5]), 105, d180, speed)
        self.blue_list.append(dot)
        dot = CircleDot((int_x[10], int_y[5]), 105, d270, speed)
        self.blue_list.append(dot)
        dot = CircleDot((int_x[10], int_y[5]), 140, 0, speed)
        self.blue_list.append(dot)
        dot = CircleDot((int_x[10], int_y[5]), 140, d90, speed)
        self.blue_list.append(dot)
        dot = CircleDot((int_x[10], int_y[5]), 140, d180, speed)
        self.blue_list.append(dot)
        dot = CircleDot((int_x[10], int_y[5]), 140, d270, speed)
        self.blue_list.append(dot)
        dot = CircleDot((int_x[10], int_y[5]), 175, 0, speed)
        self.blue_list.append(dot)
        dot = CircleDot((int_x[10], int_y[5]), 175, d90, speed)
        self.blue_list.append(dot)
        dot = CircleDot((int_x[10], int_y[5]), 175, d180, speed)
        self.blue_list.append(dot)
        dot = CircleDot((int_x[10], int_y[5]), 175, d270, speed)
        self.blue_list.append(dot)

        coin = Coin((int_x[10], int_y[8]))
        self.level_coins.append(coin)
        self.coin_list.append(coin)
        coin = Coin((int_x[13], int_y[5]))
        self.level_coins.append(coin)
        self.coin_list.append(coin)
        coin = Coin((int_x[10], int_y[2]))
        self.level_coins.append(coin)
        self.coin_list.append(coin)

    def level5(self):
        "load player and dots for level 5"
        self.spawn_points = [(int_x[2], mid_y[10]), (mid_x[17], mid_y[10]), (mid_x[1], mid_y[8])]

        speed = 0.025
        d90 = math.pi / 2
        d180 = math.pi
        d270 = math.pi + (math.pi / 2)

        dot = CircleDot((int_x[10], int_y[6]), 75, 0, speed)
        self.blue_list.append(dot)
        dot = CircleDot((int_x[10], int_y[6]), 75, d90, speed)
        self.blue_list.append(dot)
        dot = CircleDot((int_x[10], int_y[6]), 75, d180, speed)
        self.blue_list.append(dot)
        dot = CircleDot((int_x[10], int_y[6]), 75, d270, speed)
        self.blue_list.append(dot)
        dot = CircleDot((int_x[10], int_y[6]), 175, 0, speed)
        self.blue_list.append(dot)
        dot = CircleDot((int_x[10], int_y[6]), 175, d90, speed)
        self.blue_list.append(dot)
        dot = CircleDot((int_x[10], int_y[6]), 175, d180, speed)
        self.blue_list.append(dot)
        dot = CircleDot((int_x[10], int_y[6]), 175, d270, speed)
        self.blue_list.append(dot)
        dot = CircleDot((int_x[10], int_y[6]), 275, 0, speed)
        self.blue_list.append(dot)
        dot = CircleDot((int_x[10], int_y[6]), 275, d90, speed)
        self.blue_list.append(dot)
        dot = CircleDot((int_x[10], int_y[6]), 275, d180, speed)
        self.blue_list.append(dot)
        dot = CircleDot((int_x[10], int_y[6]), 275, d270, speed)
        self.blue_list.append(dot)
        dot = CircleDot((int_x[10], int_y[6]), 375, 0, speed)
        self.blue_list.append(dot)
        dot = CircleDot((int_x[10], int_y[6]), 375, d90, speed)
        self.blue_list.append(dot)
        dot = CircleDot((int_x[10], int_y[6]), 375, d180, speed)
        self.blue_list.append(dot)
        dot = CircleDot((int_x[10], int_y[6]), 375, d270, speed)
        self.blue_list.append(dot)

    def setup(self):
        "set up the game"
        self.empty_list = arcade.SpriteList()
        self.goal_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()
        self.checkpoint_list = arcade.SpriteList()
        self.player_list = arcade.SpriteList()
        self.blue_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()
        self.level_coins = []
        self.load_level(self.level)

    def load_level(self, level):
        "load a specific level"
        levels = {
            "1": self.level1,
            "2": self.level2,
            "3": self.level3,
            "4": self.level4,
            "5": self.level5
        }
        my_map = arcade.tilemap.read_tmx(f"levels/lvl{level}.tmx")
        levels[str(level)]()

        # load the player
        self.player_sprite = arcade.Sprite("assets/PLAYER.png", 1.15)
        self.player_sprite.center_x = self.spawn_points[0][0]
        self.player_sprite.center_y = self.spawn_points[0][1]
        self.player_list.append(self.player_sprite)

        # load up the map
        self.empty_list = arcade.tilemap.process_layer(my_map, 'empty', 1)
        self.wall_list = arcade.tilemap.process_layer(my_map, 'walls', 1, use_spatial_hash=True)
        self.goal_list = arcade.tilemap.process_layer(my_map, 'goal', 1, use_spatial_hash=True)
        self.checkpoint_list = arcade.tilemap.process_layer(my_map, 'checkpoint', 1)

        self.physics_engine = arcade.PhysicsEnginePlatformer(self.player_sprite, self.wall_list, 0)

    def on_update(self, delta_time):
        self.move(delta_time)
        self.blue_hit()
        self.collect_coins()
        self.check_spawn()
        self.check_win()

        # update the physics engine
        self.physics_engine.update()

    def move(self, delta_time):
        "move the player"
        if self.right:
            self.player_sprite.change_x = self.p_speed * delta_time
        if self.left:
            self.player_sprite.change_x = - 1 * (self.p_speed * delta_time)
        if self.up:
            self.player_sprite.change_y = self.p_speed * delta_time
        if self.down:
            self.player_sprite.change_y = -1 * (self.p_speed * delta_time)

    def blue_hit(self):
        "update blue dots and check for collisions"
        self.blue_list.update()
        hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.blue_list)
        # return the coins if the player was hit
        if len(hit_list) > 0:
            self.coin_list = arcade.SpriteList()
            for coin in self.level_coins:
                self.coin_list.append(coin)
        # respawn the player
        for dot in hit_list:
            self.player_sprite.center_x = self.spawn_points[0][0]
            self.player_sprite.center_y = self.spawn_points[0][1]

    def collect_coins(self):
        "check if the player collected any coins"
        self.coin_list.update()
        hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.coin_list)
        # remove collected coins
        for coin in hit_list:
            coin.remove_from_sprite_lists()

    def check_win(self):
        "check if the player beat the level"
        self.goal_list.update()
        hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.goal_list)
        if len(hit_list) > 0 and len(self.coin_list) == 0:
            self.player_sprite.remove_from_sprite_lists()
            for dot in self.blue_list:
                self.blue_list = arcade.SpriteList()
                self.level_coins = []
            self.level += 1
            self.load_level(self.level)

    def check_spawn(self):
        "check if the player reached a checkpoint"
        self.checkpoint_list.update()
        hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.checkpoint_list)
        if len(hit_list) > 0:
            delete_to = 0
            x1 = self.player_sprite.center_x
            y1 = self.player_sprite.center_y
            x2 = self.spawn_points[0][0]
            y2 = self.spawn_points[0][1]
            closest = ((x2 - x1)**2 + (y2 - y1)**2) ** (0.5)
            for i, point in enumerate(self.spawn_points):
                x2 = point[0]
                y2 = point[1]
                distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
                if distance < closest:
                    closest = distance
                    delete_to = i
            for i in range(delete_to):
                self.spawn_points.pop(0)

    def on_draw(self):
        "draw the screen"
        arcade.start_render()
        self.empty_list.draw()
        self.goal_list.draw()
        self.wall_list.draw()
        self.checkpoint_list.draw()
        self.coin_list.draw()
        self.blue_list.draw()
        self.player_list.draw()

    def on_key_press(self, symbol, modifiers):
        if symbol in (arcade.key.D, arcade.key.RIGHT):
            self.right = True
        if symbol in (arcade.key.A, arcade.key.LEFT):
            self.left = True
        if symbol in (arcade.key.W, arcade.key.UP):
            self.up = True
        if symbol in (arcade.key.S, arcade.key.DOWN):
            self.down = True

    def on_key_release(self, symbol, modifiers):
        if symbol in (arcade.key.D, arcade.key.RIGHT):
            self.right = False
            self.player_sprite.change_x = 0
        if symbol in (arcade.key.A, arcade.key.LEFT):
            self.left = False
            self.player_sprite.change_x = 0
        if symbol in (arcade.key.W, arcade.key.UP):
            self.up = False
            self.player_sprite.change_y = 0
        if symbol in (arcade.key.S, arcade.key.DOWN):
            self.down = False
            self.player_sprite.change_y = 0


WIN = MyGameWindow(WIDTH, HEIGHT, "World's Hardest Game")
arcade.run()
