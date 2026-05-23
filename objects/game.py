import arcade #everynew window, we need to install again using "pip install arcade --no-deps"
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE
from objects.player import Player

class Game(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        self.player = Player()
        arcade.set_background_color(arcade.color.GRAY_BLUE)

    def on_draw(self):
        self.clear()
        self.player.on_draw()