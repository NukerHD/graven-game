import pygame
from player import Player
from monster import Monster


class Game:

    def __init__(self):
        self.is_playing = False
        self.players = pygame.sprite.Group()
        self.monsters = pygame.sprite.Group()
        self.player = Player(self)
        self.players.add(self.player)
        self.pressed = {}

    def start(self):
        self.is_playing = True
        self.spawn_monster()

    def game_over(self):
        self.monsters = pygame.sprite.Group()
        self.player.health = self.player.max_health
        self.is_playing = False

    def update(self, display):
        display.blit(self.player.image, self.player.rect)

        self.player.update_health_bar(display)

        for projectile in self.player.projectiles:
            projectile.move()

        for monster in self.monsters:
            monster.forward()
            monster.update_health_bar(display)

        self.player.projectiles.draw(display)
        self.monsters.draw(display)

        if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x + self.player.rect.width < display.get_width():
            self.player.move_right()
        elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x > 0:
            self.player.move_left()

    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    def spawn_monster(self):
        self.monsters.add(Monster(self))
