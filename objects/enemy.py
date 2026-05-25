import arcade

class Enemy:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 3

    def draw(self):
        arcade.draw_circle_filled(self.x, self.y, 15, arcade.color.RAW_UMBER)

    def update(self):
        self.y -= self.speed
