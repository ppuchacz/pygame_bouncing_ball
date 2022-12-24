from pygame import Surface
import pygame
from component.collider.circle_collider import CircleCollider
from component.collider.collider import Collider
from core.entity import Entity

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

class Ball(Entity):
    def __init__(self, position: tuple = (RADIOUS, RADIOUS), direction: tuple = BM, speed: float = 100.0, radious = RADIOUS, spawn_position=None) -> None:
        super().__init__()
        self.color = COLOR
        self.position = to_array(position)
        self.direction = to_array(direction)
        self.speed = speed
        self.radious = radious
        self.collider = CircleCollider(self.radious, position, is_trigger=True)
        super().register_component(self.collider)
        if spawn_position != None:
            self.spawn_at(spawn_position)

    def draw(self, surface: Surface):
        pygame.draw.circle(surface, self.color, self.position, self.radious)

    def update(self, delta_time: float):
        # self.move(delta_time * self.speed)
        self.position = to_array(pygame.mouse.get_pos())
        self.collider.set_position(self.position)
    
    def move(self, distance):
        self.position[0] += self.direction[0] * distance
        self.position[1] += self.direction[1] * distance

    def on_collision(self, collider: Collider):
        # print("collision in progress {}".format(type(collider.entity)))
        pass
    
    def on_collision_enter(self, collider: Collider):
        print("collision enter {}".format(type(collider.entity)))
        self.set_color_collision_triggered()
    
    def on_collision_exit(self, collider: Collider):
        print("collision exit {}".format(type(collider.entity)))
        self.set_color_default()

    def set_color_default(self):
        self.color = COLOR

    def set_color_collision_triggered(self):
        self.color = COLLISION_TRIGGERED_COLOR
    
    def spawn_at(self, position: tuple):
        self.position = [
            position[0],
            position[1] - self.radious * 3,
            ]