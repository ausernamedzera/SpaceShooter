import arcade #everynew window, we need to install again using "pip install arcade --no-deps"

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Space Shooter"

class Game:
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        arcade.set.background_color(arcade.color.BLACK)