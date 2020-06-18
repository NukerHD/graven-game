import pygame


class Monster(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 5
        self.velocity = 1
        self.image = pygame.image.load('assets/mummy.png')
        self.rect = self.image.get_rect()
        # ToDo: set value to screen width
        self.rect.x = 1080
        self.rect.y = 550

    def forward(self):
        if not self.game.check_collision(self, self.game.players):
            self.rect.x -= self.velocity
