import pygame
from components.ball import Ball
from components.board import Board
from components.player import Player
from service.key_manager import KeyManager
import settings

pygame.init()

screen = pygame.display.set_mode([settings.WINDOW_WIDTH, settings.WINDOW_HEIGHT])

board = Board(settings.LEVEL)
player = Player(settings.PLAYER)
ball = Ball()
key_manager = KeyManager()

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            key_manager.register_down(event.key)
            player.on_key_down(event.key)
        if event.type == pygame.KEYUP:
            key_manager.register_up(event.key)
            player.on_key_up(event.key)
    
    for key in key_manager.get_pressed():
        player.on_key_pressed(key)

    screen.fill((255, 255, 255))

    player.update()

    pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)
    board.draw(screen)
    player.draw(screen)

    pygame.display.flip()

pygame.quit()