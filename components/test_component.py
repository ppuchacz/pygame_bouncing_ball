from pygame import Surface
import pygame
from service.collision_manager.rect_collider import RectangleCollider


COLOR = (110, 110, 110)

class TestRectangleComponent:
    collider: RectangleCollider
    width: float
    height: float
    x: float
    y: float

    def __init__(self, pos_x: float, pos_y: float, width: float, height: float) -> None:
        self.x = pos_x
        self.y = pos_y
        self.width = width
        self.height = height
        self.collider = RectangleCollider((self.x, self.y), width, height)

    def draw(self, surface: Surface):
        pygame.draw.rect(surface, COLOR, (self.x, self.y, self.width, self.height))