import arcade
import random

class Enemy:
    def __init__(self, x, y, spawn_timer):
        self.x = x
        self.y = y
        self.spawn_timer = spawn_timer