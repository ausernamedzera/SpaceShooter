import arcade #everynew window, we need to install again using "pip install arcade --no-deps"
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE
from objects.bullet import Bullet
from objects.enemy import Enemy
from objects.player import Player
import random

class Game(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        self.player = Player()
        self.enemies = []
        self.enemy_spawn_timer = 0
        self.game_over = False
        arcade.set_background_color(arcade.color.GRAY_BLUE)

    def on_draw(self):
        self.clear()
        self.player.on_draw()
        arcade.draw_text(f"Score: {self.player.score}", 10, SCREEN_HEIGHT - 30, arcade.color.BLACK_OLIVE, 16)
        arcade.draw_text(f"Lives: {self.player.lives}", 10, SCREEN_HEIGHT - 50, arcade.color.RED_BROWN, 16)
        for enemy in self.enemies:
            enemy.draw()
        if self.game_over:
            arcade.draw_text("GAME OVER", SCREEN_WIDTH/2, SCREEN_HEIGHT/2, arcade.color.BLACK, 50)


    def on_key_press(self, key, modifiers):
        self.player.on_key_press(key, modifiers)

    def on_key_release(self, key, modifiers):
        self.player.on_key_release(key, modifiers)

    def on_update(self, delta_time):
        if self.game_over:
            return
        self.player.on_update(delta_time)
        self.enemy_spawn_timer += delta_time

        if self.enemy_spawn_timer > 1.5:
            x = random.randint(20, SCREEN_WIDTH - 20)
            self.enemies.append(Enemy(x, SCREEN_HEIGHT))
            self.enemy_spawn_timer = 0

        for enemy in self.enemies:
            enemy.update()

        for enemy in self.enemies:
            if enemy.y <= 0:
                self.player.lives -= 1
        self.enemies = [e for e in self.enemies if e.y > 0]

        for bullet in self.player.bullets[:]: #[:] creates copy of a list
            bullet.update()

        self.player.bullets = [b for b in self.player.bullets if b.y < SCREEN_HEIGHT]

        #collision mechanics
        for bullet in self.player.bullets[:]:
            for enemy in self.enemies[:]:
                if abs(bullet.x - enemy.x) < 20 and abs(bullet.y - enemy.y) < 20:
                    self.player.bullets.remove(bullet)
                    self.enemies.remove(enemy)
                    self.player.score += 1
                    break

        if self.player.lives <= 0:
            self.game_over = True