#!/usr/bin/env python3
import arcade

WIDTH = 1000
HEIGHT = 600


class MyGameWindow(arcade.Window):
    "control game window"
    def __init__(self, width, height, title):
        super().__init__(width, height, title, resizable=True)
        self.set_location(400, 200)
        self.background = arcade.load_texture("assets/BG.png")

        # sprite lists
        self.wall_list = None
        self.checkpoint_list = None
        self.player_list = None
        self.blue_list = None
        self.coin_list = None

        # setup player
        self.p_x = 110
        self.p_y = 375
        self.p_speed = 175
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

    def setup(self):
        self.game_over = False
        self.wall_list = arcade.SpriteList()
        self.checkpoint_list = arcade.SpriteList()
        self.player_list = arcade.SpriteList()
        self.blue_list = arcade.SpriteList()
        self.load_level(self.level)

    def load_level(self, level):
        my_map = arcade.tilemap.read_tmx(f"levels/lvl{level}.tmx")

        self.player_sprite = arcade.Sprite("assets/PLAYER.png", 1.15)
        self.player_sprite.center_x = 110
        self.player_sprite.center_y = 375
        self.player_list.append(self.player_sprite)

        self.blue_list = arcade.tilemap.process_layer(my_map, 'bluedots', 1)
        self.wall_list = arcade.tilemap.process_layer(my_map, 'walls', 1, use_spatial_hash=True)
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

        self.physics_engine.update()

    def on_draw(self):
        "draw the screen"
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0, 0, WIDTH, HEIGHT, self.background)
        self.wall_list.draw()
        self.checkpoint_list.draw()
        self.player_list.draw()
        self.blue_list.draw()

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
