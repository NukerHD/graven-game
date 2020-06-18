import pygame
import math

from game import Game

pygame.init()

pygame.display.set_caption("Comets")
display = pygame.display.set_mode((1280, 720))

background = pygame.image.load('assets/bg.jpg')

banner = pygame.image.load('assets/banner.png')
banner = pygame.transform.scale(banner, (500, 500))
banner_rect = banner.get_rect()
banner_rect.x = math.ceil(display.get_width() / 4)

play_button = pygame.image.load('assets/button.png')
play_button = pygame.transform.scale(play_button, (400, 150))
play_button_rect = play_button.get_rect()
play_button_rect.x = math.ceil(display.get_width() / 3.33)
play_button_rect.y = math.ceil(display.get_height() / 1.6)

game = Game()

running = True

while running:
    display.blit(background, (0, 0))

    if game.is_playing:
        game.update(display)
    else:
        display.blit(banner, banner_rect)
        display.blit(play_button, play_button_rect)

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True
            if event.key == pygame.K_SPACE:
                game.player.launch_projectile()
        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if play_button_rect.collidepoint(event.pos):
                game.start()
