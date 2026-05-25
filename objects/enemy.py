import arcade
import random

class Enemy:
    def __init__(self, x, y, spawn_timer):
        self.x = x
        self.y = y
        self.spawn_timer = spawn_timer

    def draw(self):
        arcade.draw_circle_filled(self.x, self.y, 15, arcade.color.RAW_UMBER)
