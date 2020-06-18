import pygame

from game import Game

pygame.init()

pygame.display.set_caption("Comets")
display = pygame.display.set_mode((1280, 720))

background = pygame.image.load("assets/bg.jpg")

game = Game()

running = True

while running:
    display.blit(background, (0, 0))
    display.blit(game.player.image, game.player.rect)

    game.player.update_health_bar(display)

    for projectile in game.player.projectiles:
        projectile.move()

    for monster in game.monsters:
        monster.forward()
        monster.update_health_bar(display)

    game.player.projectiles.draw(display)
    game.monsters.draw(display)

    if game.pressed.get(pygame.K_RIGHT) and game.player.rect.x + game.player.rect.width < display.get_width():
        game.player.move_right()
    elif game.pressed.get(pygame.K_LEFT) and game.player.rect.x > 0:
        game.player.move_left()

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
