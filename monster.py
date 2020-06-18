import pygame
import random
from entity import Entity


class Monster(Entity):
    bar_color = (110, 210, 50)
    background_bar_color = (60, 60, 60)

    def __init__(self, game):
        super().__init__(game,  # game
                         100,  # health
                         100,  # max_health
                         random.randint(1, 5),  # attack
                         random.randint(1, 3),  # velocity
                         'assets/mummy.png',  # image
                         1080 + random.randint(0, 500),  # rect x
                         540)  # rect y

    def damage(self, amount):
        self.health -= amount
        if self.health <= 0:
            self.game.monsters.remove(self)

    def forward(self):
        if not self.game.check_collision(self, self.game.players):
            self.rect.x -= self.velocity
        else:
            self.game.player.damage(self.attack)