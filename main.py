import pygame
from entity.ball import Ball
from entity.board import Board
from entity.player import Player
from entity.test_entity import TestRectangleEntity
from service.key_manager import KeyManager
from service.timer import Timer
from service.collision_manager.collision_manager import check_circle_rectangle_collision
from service.collision_manager.collision_manager import check_circle_rectangle_group_collision
import settings

pygame.init()

screen = pygame.display.set_mode([settings.WINDOW_WIDTH, settings.WINDOW_HEIGHT])

board = Board(settings.LEVEL)
player = Player(settings.PLAYER)
ball = Ball(radious=10.0, spawn_position=player.get_position_center())
test_rect = TestRectangleEntity(200, 100, 200, 250)
key_manager = KeyManager()
timer = Timer()
# collisionManager = CollisionManager()

collidables = [
    player,
    ball,
    board
]

# collisionManager.register(board)
# collisionManager.register(ball)
# collisionManager.register(player)


running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            key_manager.register_down(event.key)
            player.on_key_down(event.key)
            ball.on_key_down(event.key)
        if event.type == pygame.KEYUP:
            key_manager.register_up(event.key)
            player.on_key_up(event.key)
            ball.on_key_up(event.key)
    
    for key in key_manager.get_pressed():
        player.on_key_pressed(key)

    screen.fill((255, 255, 255))

    delta_time = timer.reset()
    player.update(delta_time)
    ball.update(delta_time)
    # collisionManager.checkCollisions(collidables)

    if check_circle_rectangle_group_collision(ball.collider, board.get_colliders()):
        ball.set_color_collision_triggered()
    else:
        ball.set_color_default()

    pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)
    board.draw(screen)
    player.draw(screen)
    test_rect.draw(screen)
    ball.draw(screen)

    pygame.display.flip()

pygame.quit()