#!/usr/bin/env python3
import arcade

WIDTH = 1000
HEIGHT = 600


class LineDot(arcade.Sprite):
    "blue dots that go in a straight line"
    def __init__(self, filename, scale, point1, point2):
        super().__init__(filename, scale)
        self.p1x = point1[0]
        self.p1y = point1[1]
        self.p2x = point2[0]
        self.p2y = point2[1]
        self.goal = [self.p2x, self.p2y]
        self.speed = 7

        if self.p1y == self.p2y:
            self.direction = "horiz"
        else:
            self.direction = "vert"

    def update(self):
        "move the dot"
        if self.direction == "horiz":
            if self.center_x > self.goal[0]:
                self.center_x -= self.speed
            if self.center_x < self.goal[0]:
                self.center_x += self.speed
            if 0 < abs(self.center_x - self.goal[0]) < 7:
                self.center_x = self.goal[0]
                if self.goal[0] == self.p2x:
                    self.goal[0] = self.p1x
                elif self.goal[0] == self.p1x:
                    self.goal[0] = self.p2x
        if self.direction == "vert":
            if self.center_y > self.goal[1]:
                self.center_y -= self.speed
            if self.center_y < self.goal[1]:
                self.center_y += self.speed
            if 0 < abs(self.center_y - self.goal[1]) < 7:
                self.center_y = self.goal[1]
                if self.goal[1] == self.p2y:
                    self.goal[1] = self.p1y
                elif self.goal[1] == self.p1y:
                    self.goal[1] = self.p2y




class MyGameWindow(arcade.Window):
    "control game window"
    def __init__(self, width, height, title):
        super().__init__(width, height, title, resizable=True)
        self.set_location(400, 200)

        # sprite lists
        self.empty_list = None
        self.wall_list = None
        self.checkpoint_list = None
        self.player_list = None
        self.blue_list = None
        self.coin_list = None

        # setup player
        self.p_speed = 175
        self.p_sx = None
        self.p_sy = None
        self.deaths = 0
        self.player_sprite = None

        # movement
        self.right = False
        self.left = False
        self.up = False
        self.down = False

        # game variables
        self.game_over = False
        self.level = 1
        self.max_level = 1

        self.physics_engine = None
        self.setup()

    def level1(self):
        "load player and dots for level 1"
        # load the player
        self.p_sx = 110
        self.p_sy = 375

        # start the dots for level 1
        dot = LineDot("assets/BLUE_DOT.png", 1, [735, 375], [265, 375])
        dot.center_x = 735
        dot.center_y = 375
        self.blue_list.append(dot)

        dot = LineDot("assets/BLUE_DOT.png", 1, [735, 275], [265, 275])
        dot.center_x = 735
        dot.center_y = 275
        self.blue_list.append(dot)

        dot = LineDot("assets/BLUE_DOT.png", 1, [265, 325], [735, 325])
        dot.center_x = 265
        dot.center_y = 325
        self.blue_list.append(dot)

        dot = LineDot("assets/BLUE_DOT.png", 1, [265, 225], [735, 225])
        dot.center_x = 265
        dot.center_y = 225
        self.blue_list.append(dot)

    def setup(self):
        "set up the game"
        self.empty_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()
        self.checkpoint_list = arcade.SpriteList()
        self.player_list = arcade.SpriteList()
        self.blue_list = arcade.SpriteList()
        self.level1()
        self.load_level(self.level)

    def load_level(self, level):
        "load a specific level"
        my_map = arcade.tilemap.read_tmx(f"levels/lvl{level}.tmx")

        # load the player
        self.player_sprite = arcade.Sprite("assets/PLAYER.png", 1.15)
        self.player_sprite.center_x = self.p_sx
        self.player_sprite.center_y = self.p_sy
        self.player_list.append(self.player_sprite)

        # load up the map
        self.empty_list = arcade.tilemap.process_layer(my_map, 'empty', 1)
        self.wall_list = arcade.tilemap.process_layer(my_map, 'walls', 1, use_spatial_hash=True)

        # self.blue_list = arcade.tilemap.process_layer(my_map, 'bluedots', 1)
        self.checkpoint_list = arcade.tilemap.process_layer(my_map, 'checkpoint', 1)

        self.physics_engine = arcade.PhysicsEnginePlatformer(self.player_sprite, self.wall_list, 0)

    def on_update(self, delta_time):
        if self.right:
            self.player_sprite.change_x = self.p_speed * delta_time
        if self.left:
            self.player_sprite.change_x = - 1 * (self.p_speed * delta_time)
        if self.up:
            self.player_sprite.change_y = self.p_speed * delta_time
        if self.down:
            self.player_sprite.change_y = -1 * (self.p_speed * delta_time)

        self.blue_list.update()
        hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.blue_list)
        for dot in hit_list:
            self.player_sprite.center_x = self.p_sx
            self.player_sprite.center_y = self.p_sy

        self.physics_engine.update()

    def on_draw(self):
        "draw the screen"
        arcade.start_render()
        self.empty_list.draw()
        self.wall_list.draw()
        self.checkpoint_list.draw()
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
WIN.on_draw()
