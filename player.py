import pygame
from entity import Entity
from projectile import Projectile


class Player(Entity):

    def __init__(self, game):
        super().__init__(game,  # game
                         100,  # health
                         100,  # max_health
                         20,  # attack
                         4,  # velocity
                         'assets/player.png',  # image
                         500,  # rect x
                         500)  # rect y
        self.projectiles = pygame.sprite.Group()

    def update_health_bar(self, surface):
        bar_position = [self.rect.x + 50, self.rect.y, self.health, 5]
        background_bar_position = [self.rect.x + 50, self.rect.y, self.max_health, 5]
        pygame.draw.rect(surface, self.background_bar_color, background_bar_position)
        pygame.draw.rect(surface, self.bar_color, bar_position)

    def damage(self, amount):
        if self.health - amount > amount:
            self.health -= amount
        else:
            self.game.game_over()

    def launch_projectile(self):
        self.projectiles.add(Projectile(self))

    def move_right(self):
        if not self.game.check_collision(self, self.game.monsters):
            self.rect.x += self.velocity

    def move_left(self):
        self.rect.x -= self.velocity
