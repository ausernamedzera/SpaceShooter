import arcade

class Bullet:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 5

    def on_update(self):
        self.y += self.speed