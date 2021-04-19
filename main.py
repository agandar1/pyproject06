#!/usr/bin/env python3

import math
import arcade
from levels import levels

WIDTH = 1000
HEIGHT = 600


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
    spawn_points = []
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
    max_level = 9

    physics_engine = None

    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.set_location(400, 200)
        self.setup()

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
        level_list = {
            "1": levels.level1,
            "2": levels.level2,
            "3": levels.level3,
            "4": levels.level4,
            "5": levels.level5,
            "6": levels.level6,
            "7": levels.level7,
            "8": levels.level8,
            "9": levels.level9
        }
        my_map = arcade.tilemap.read_tmx(f"levels/lvl{level}.tmx")
        level_list[str(level)](self)

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