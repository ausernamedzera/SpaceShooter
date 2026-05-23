import arcade
from objects.bullet import Bullet
from constants import SCREEN_WIDTH, SCREEN_HEIGHT


class Player:
    def __init__(self):
        self.player_x = SCREEN_WIDTH / 2
        self.player_y = 50
        self.player_speed = 0

    def on_draw(self):
        arcade.draw_circle_filled(self.player_x, self.player_y, 20, arcade.color.PURPLE_HEART)

    def on_key_press(self, key, modifiers):
        if key == arcade.key.LEFT:
            self.player_speed = -5
        if key == arcade.key.RIGHT: #written with elif, I'll try this one first
            self.player_speed = 5

    def on_key_release(self, key, modifiers):
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player_speed = 0

    def on_update(self, delta_time):
        self.player_x += self.player_speed

        if self.player_x < 20:
            self.player_x = 20
        if self.player_x > SCREEN_WIDTH - 20:
            self.player_x = SCREEN_WIDTH - 20