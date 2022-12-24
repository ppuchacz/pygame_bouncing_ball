from pygame import Surface
import pygame
from component.collider.collider import Collider
from component.collider.rect_collider import RectangleCollider
from config.level import Level
from core.entity import Entity


CELL_COLOR = (150, 50, 80)


class Cell(Entity):
    width: int
    height: int
    x: int
    y: int
    collider: RectangleCollider

    def __init__(self, width, height, x, y) -> None:
        super().__init__()
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.collider = RectangleCollider((x, y), width, height)
        super().register_component(self.collider)
    
    def on_collision(self, collider: Collider) -> None:
        print("cell collision")

    def draw(self, screen: Surface):
        pygame.draw.rect(screen, CELL_COLOR, (self.x, self.y, self.width, self.height))
