import pygame
import settings
import utils

pygame.init()

screen = pygame.display.set_mode([settings.WINDOW_WIDTH, settings.WINDOW_HEIGHT])

board = utils.clone_list(settings.LEVEL)

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))

    pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)

    pygame.display.flip()

pygame.quit()