import arcade
import random

class Enemy:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 0

    def draw(self):
        arcade.draw_circle_filled(self.x, self.y, 15, arcade.color.RAW_UMBER)

    def update(self, delta_time):
        self.speed += delta_time

