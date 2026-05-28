import arcade
class Bullet:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 5

    def update(self):
        self.y += self.speed

    def draw(self):
        arcade.draw_circle_filled(self.x, self.y, 5, arcade.color.YELLOW)