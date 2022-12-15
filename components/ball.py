from pygame import Surface
import pygame
from service.collision_manager.circle_collider import CircleCollider

from utils import to_array


COLOR = (0, 20, 150)
COLLISION_TRIGGERED_COLOR = (255, 50, 50)
RADIOUS = 10

TR = (1, -1)
TM = (0, -1)
TL = (-1, -1)
BR = (1, 1)
BM = (0, 1)
BL = (-1, 1)
MR = (1, 0)
ML = (-1, 0)
DIR_STILL = (0, 0)

class Ball:
    def __init__(self, position: tuple = (RADIOUS, RADIOUS), direction: tuple = BM, speed: float = 100.0, radious = RADIOUS, spawn_position=None) -> None:
        self.color = COLOR
        self.position = to_array(position)
        self.direction = to_array(direction)
        self.speed = speed
        self.radious = radious
        self.collider = CircleCollider(self.radious, position)
        if spawn_position != None:
            self.spawn_at(spawn_position)
    
    def on_key_up(self, code):
        # print(code)
        pass

    def on_key_down(self, code):
        if code == pygame.K_p:
            self.set_color_collision_triggered()
        if code == pygame.K_o:
            self.set_color_default()
        pass

    def on_key_pressed(self, code):
        pass

    def draw(self, surface: Surface):
        pygame.draw.circle(surface, self.color, self.position, self.radious)

    def update(self, delta_time: float):
        # self.move(delta_time * self.speed)
        # self.position = to_array(pygame.mouse.get_pos())
        self.collider.set_position(self.position)
    
    def move(self, distance):
        self.position[0] += self.direction[0] * distance
        self.position[1] += self.direction[1] * distance

    def on_collision(self, direction: tuple):
        pass

    def set_color_default(self):
        self.color = COLOR

    def set_color_collision_triggered(self):
        self.color = COLLISION_TRIGGERED_COLOR
    
    def spawn_at(self, position: tuple):
        self.position = [
            position[0],
            position[1] - self.radious * 3,
            ]