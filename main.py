from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from objects.player import Player
from objects.enemies import Enemies
from objects.game import Game
import arcade

def main():
    game_window = Game()
    arcade.run()

if __name__ == '__main__':
    main()