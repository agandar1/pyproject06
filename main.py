#!/usr/bin/env python3

import copy
import math
import arcade
from levels import levels
from bot import Player, Genetic
from arcade.gui import UIManager

WIDTH = 1000
HEIGHT = 600


class TitleScreen(arcade.View):
    def __init__(self):
        super().__init__()
        self.texture = arcade.load_texture("assets/start.png")

    def on_draw(self):
        "Draw this view"
        arcade.start_render()
        self.texture.draw_sized(WIDTH / 2, HEIGHT / 2, WIDTH, HEIGHT)

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        "If the user presses the mouse button, start the game."
        modeSelect = ModeSelection()
        self.window.show_view(modeSelect)


class ModeButton(arcade.gui.UIGhostFlatButton):

    def __init__(self, innerText, center_x, center_y,ui_manager):
        self.innerText = innerText
        self.ui_manager = ui_manager
        super().__init__(
            innerText,
            center_x=center_x,
            center_y=center_y,
            width=250,
        )

    def on_click(self):
        """ Called when user lets off button """
        self.ui_manager.purge_ui_elements()
        mode = 1
        if self.innerText == "Train AI":
            mode = 0
        elif self.innerText == "Free Play":
            mode = 1
        elif self.innerText == "Watch AI":
            mode = 2
        levelView = levelSelection(mode)
        WIN.show_view(levelView)

class ModeSelection(arcade.View):
    
    def __init__(self):
        
        """ This is run once when we switch to this view """
        super().__init__()
        self.ui_manager = UIManager() 
        """ This is run once when we switch to this view """
    
    def on_draw(self):
        
        arcade.start_render()
        arcade.draw_text("Select a Mode", WIDTH / 2, HEIGHT / 1.25 , arcade.color.WHITE, font_size=50, anchor_x="center")
 
    def on_show_view(self):
        
        self.setup()
        arcade.set_background_color(arcade.csscolor.DARK_SLATE_BLUE)
        arcade.set_viewport(0, WIDTH - 1, 0, HEIGHT - 1)

    def setup(self):
        """ Draw this view """    

        button = ModeButton("Free Play", 475, 415,self.ui_manager)
        self.ui_manager.add_ui_element(button)

        button = ModeButton("Train AI", 475, 300,self.ui_manager)
        self.ui_manager.add_ui_element(button)

        button = ModeButton("Watch AI", 475, 175, self.ui_manager)
        self.ui_manager.add_ui_element(button)
       

class LevelButton(arcade.gui.UIGhostFlatButton):

    def __init__(self, innerText, center_x, center_y, mode, ui_manager, level):
        self.innerText = innerText
        self.mode = mode
        self.ui_manager = ui_manager
        self.level = level
        super().__init__(
            innerText,
            center_x=center_x,
            center_y=center_y,
            width=250,
        )

    def on_click(self):
        """ Called when user lets off button """ 
        self.ui_manager.purge_ui_elements()
        gameView = GameView(self.mode)
        gameView.level = self.level
        gameView.setup()
        WIN.show_view(gameView)


class levelSelection(arcade.View):

    def __init__(self, mode):
        self.mode = mode
        """ This is run once when we switch to this view """
        super().__init__()
        self.ui_manager = UIManager()
        
        """ This is run once when we switch to this view """
        arcade.set_background_color(arcade.csscolor.DARK_SLATE_BLUE)
        arcade.set_viewport(0, WIDTH - 1, 0, HEIGHT - 1)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("Select a Level", WIDTH / 2, HEIGHT / 1.25 , arcade.color.WHITE, font_size=50, anchor_x="center")
 
    def on_show_view(self):
        
        self.setup()
        arcade.set_background_color(arcade.csscolor.DARK_SLATE_BLUE)
        arcade.set_viewport(0, WIDTH - 1, 0, HEIGHT - 1)

    def setup(self):
        """ Draw this view """ 
        x_coords = [130, 475, 835]
        y_coords = [415, 300, 175]
        count = 1

        for i in range(3):
            for j in range(3):
                button = LevelButton("Level "+str(count), x_coords[j], y_coords[i], self.mode, self.ui_manager, count)
                self.ui_manager.add_ui_element(button)       
                count += 1
        button = LevelButton("Level 10", 475, 75, self.mode, self.ui_manager, 10)
        self.ui_manager.add_ui_element(button)
       

class GameView(arcade.View):
    "control game window"
    # setup player
    spawn_points = []
    p_speed = 175
    deaths = 0

    # movement
    right = False
    left = False
    up = False
    down = False

    # game variables
    allDead = False
    level = 1
    max_level = 10

    def __init__(self, mode):
        super().__init__()
        self.mode = mode
        if self.mode == 1:
            self.human = True
            self.player_count = 1
            self.move_count = 0
        else:
            self.human = False
            self.player_count = 50
            self.move_count = 500

        self.watching = False
        if self.mode == 2:
            self.watching = True

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
            "9": levels.level9,
            "10": levels.level10
        }
        my_map = arcade.tilemap.read_tmx(f"levels/lvl{level}.tmx")
        level_list[str(level)](self)

        # load the player
        for i in range(self.player_count):
            player = Player(self.spawn_points[0], self.move_count, self.human, self.p_speed, self.level_coins[:], levels.goals[level - 1])
            self.player_list.append(player)

        # load up the map
        self.empty_list = arcade.tilemap.process_layer(my_map, 'empty', 1)
        self.wall_list = arcade.tilemap.process_layer(my_map, 'walls', 1, use_spatial_hash=True)
        self.goal_list = arcade.tilemap.process_layer(my_map, 'goal', 1, use_spatial_hash=True)
        self.checkpoint_list = arcade.tilemap.process_layer(my_map, 'checkpoint', 1)

        self.engine_list = []
        for sprite in self.player_list:
            physics_engine = arcade.PhysicsEnginePlatformer(sprite, self.wall_list, 0)
            self.engine_list.append(physics_engine)

    def on_update(self, delta_time):
        self.checkLife()
        if not self.allDead or self.human:
            for i, player in enumerate(self.player_list):
                self.player_sprite = player
                if self.human:
                    self.move(delta_time)
                else:
                    player.update(delta_time)
                self.blue_list.update()
                self.blue_hit()
                self.collect_coins()
                self.check_spawn()
                self.check_win()
        else:
            self.newplayers()
        # update the physics engine
        for engine in self.engine_list:
            engine.update()

    def newplayers(self):
        gen = Genetic(copy.deepcopy(self.player_list))
        new_directions = gen.newDirections()
        self.setup()

        for i in range(len(self.player_list)):
            self.player_list[i].brain.directions = copy.deepcopy(new_directions[i])
            self.player_list[i].directions = copy.deepcopy(new_directions[i])

    def checkLife(self):
        alive = False
        for i in range(len(self.player_list)):
            if self.player_list[i].alive:
                alive = True
        if alive:
            self.allDead = False
        else:
            self.allDead = True

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
        hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.blue_list)
        # return the coins if the player was hit
        if len(hit_list) > 0:
            self.coin_list = arcade.SpriteList()
            for coin in self.level_coins:
                self.coin_list.append(coin)
        # respawn the player
        for dot in hit_list:
            if self.human:
                self.player_sprite.center_x = self.spawn_points[0][0]
                self.player_sprite.center_y = self.spawn_points[0][1]
            else:
                self.player_sprite.alive = False

    def collect_coins(self):
        "check if the player collected any coins"
        self.coin_list.update()
        hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.coin_list)
        # remove collected coins
        for coin in hit_list:
            self.player_sprite.reachedCoin = True
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
        if self.human or not self.human:
            if symbol in (arcade.key.D, arcade.key.RIGHT):
                self.right = True
            if symbol in (arcade.key.A, arcade.key.LEFT):
                self.left = True
            if symbol in (arcade.key.W, arcade.key.UP):
                self.up = True
            if symbol in (arcade.key.S, arcade.key.DOWN):
                self.down = True

    def on_key_release(self, symbol, modifiers):
        if self.human or not self.human:
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


WIN = arcade.Window(WIDTH, HEIGHT, "World's Hardest Game")
start_view = TitleScreen()
WIN.show_view(start_view)
arcade.run()
