import pygame


class Projectile(pygame.sprite.Sprite):

    def __init__(self, player):
        super().__init__()
        self.velocity = 5
        self.player = player
        self.image = pygame.image.load('assets/projectile.png')
        self.image = pygame.transform.scale(self.image, (32, 32))
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x + 80
        self.rect.y = player.rect.y + 70
        self.origin_image = self.image
        self.angle = 0

    def rotate(self):
        self.angle += 1
        self.image = pygame.transform.rotozoom(self.origin_image, self.angle, 1)
        self.rect = self.image.get_rect(center=self.rect.center)

    def remove(self):
        self.player.projectiles.remove(self)

    def move(self):
        self.rect.x += self.velocity
        self.rotate()

        for monster in self.player.game.check_collision(self, self.player.game.monsters):
            self.remove()
            monster.damage(self.player.attack)

        # ToDo: set value to screen width
        if self.rect.x > 1080:
            self.remove()
