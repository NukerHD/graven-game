import pygame
from player import Player
from monster import Monster


class Game:

    def __init__(self):
        self.players = pygame.sprite.Group()
        self.monsters = pygame.sprite.Group()
        self.player = Player(self)
        self.players.add(self.player)
        self.pressed = {}
        self.spawn_monster()

    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    def spawn_monster(self):
        self.monsters.add(Monster(self))
