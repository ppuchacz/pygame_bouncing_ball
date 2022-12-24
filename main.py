import pygame
from core.scene import Scene
from entity.ball import Ball
from entity.player import Player
from entity.test_entity import TestRectangleEntity
from service.key_manager import KeyManager
from service.timer import Timer
import settings
from system.collision_check import CollisionCheck
from system.level_loader import LevelLoader

pygame.init()

screen = pygame.display.set_mode([settings.WINDOW_WIDTH, settings.WINDOW_HEIGHT])

player = Player(settings.PLAYER)
ball = Ball(radious=10.0, spawn_position=player.get_position_center())
test_rect = TestRectangleEntity(200, 100, 200, 250)
key_manager = KeyManager()

scene = Scene()
scene.add_entity(player)
scene.add_entity(ball)
scene.add_entity(test_rect)

collisionCheck = CollisionCheck()
LevelLoader.load(settings.LEVEL, scene)
timer = Timer()

collisionCheck.load_colliders(scene)

# collisionManager = CollisionManager()

# collisionManager.register(ball)
# collisionManager.register(player)


running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            scene.on_key_down(event.key)
            key_manager.register_down(event.key)
        if event.type == pygame.KEYUP:
            key_manager.register_up(event.key)
            scene.on_key_up(event.key)
    
    for key in key_manager.get_pressed():
        scene.on_key_pressed(key)

    screen.fill((255, 255, 255))

    delta_time = timer.reset()
    scene.update(delta_time)
    collisionCheck.update()
    # collisionManager.checkCollisions(collidables)

    # if check_circle_rectangle_group_collision(ball.collider, board.get_colliders()):
    #     ball.set_color_collision_triggered()
    # else:
    #     ball.set_color_default()

    scene.draw(screen)

    pygame.display.flip()

pygame.quit()