import arcade #everynew window, we need to install again using "pip install arcade --no-deps"
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE
from objects.player import Player

class Game(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        self.player = Player()
        self.enemies = []
        arcade.set_background_color(arcade.color.GRAY_BLUE)

    def on_draw(self):
        self.clear()
        self.player.on_draw()

    def on_key_press(self, key, modifiers):
        self.player.on_key_press(key, modifiers)

    def on_key_release(self, key, modifiers):
        self.player.on_key_release(key, modifiers)

    def on_update(self, delta_time):
        self.player.on_update(delta_time)