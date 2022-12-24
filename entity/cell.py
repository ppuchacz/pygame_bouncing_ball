from pygame import Surface
import pygame
from component.collider.collider import Collider
from component.collider.rect_collider import RectangleCollider
from config.level import Level
from core.entity import Entity


CELL_COLOR = (150, 50, 80)
COLLISION_TRIGGERED_COLOR = (255, 50, 50)


class Cell(Entity):
    width: int
    height: int
    x: int
    y: int

    def __init__(self, width, height, x, y) -> None:
        super().__init__()
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.color = CELL_COLOR
        collider = RectangleCollider((x, y), width, height)
        super().register_component(collider)

    def on_collision(self, collider: Collider):
        pass
    
    def on_collision_enter(self, collider: Collider):
        self.set_color_collision_triggered()
    
    def on_collision_exit(self, collider: Collider):
        self.set_color_default()

    def draw(self, screen: Surface):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

    def set_color_default(self):
        self.color = CELL_COLOR

    def set_color_collision_triggered(self):
        self.color = COLLISION_TRIGGERED_COLOR