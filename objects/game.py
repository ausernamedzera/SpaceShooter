import arcade #everynew window, we need to install again using "pip install arcade --no-deps"

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Space Shooter"

class Game(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        arcade.set_background_color(arcade.color.GRAY_BLUE)

    def on_draw(self):
        self.clear()