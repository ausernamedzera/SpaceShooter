import arcade
from constants import SCREEN_WIDTH, SCREEN_HEIGHT


class Player:
    def __init__(self):
        self.player_x = SCREEN_WIDTH / 2
        self.player_y = 50

    def on_draw(self):
        arcade.draw_circle_filled(self.player_x, self.player_y, 20, arcade.color.PURPLE_HEART)