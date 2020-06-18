import pygame


class Entity(pygame.sprite.Sprite):
    bar_color = (110, 210, 50)
    background_bar_color = (60, 60, 60)

    def __init__(self, game, health, max_health, attack, velocity, image, rect_x, rect_y):
        super().__init__()
        self.game = game
        self.health = health
        self.max_health = max_health
        self.attack = attack
        self.velocity = velocity
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.x = rect_x
        self.rect.y = rect_y

    def update_health_bar(self, surface):
        bar_position = [self.rect.x + 12, self.rect.y - 20, self.health, 5]
        background_bar_position = [self.rect.x + 12, self.rect.y - 20, self.max_health, 5]
        pygame.draw.rect(surface, self.background_bar_color, background_bar_position)
        pygame.draw.rect(surface, self.bar_color, bar_position)

    def damage(self, amount):
        self.health -= amount
        if self.health <= 0:
            self.game.monsters.remove(self)
