from pygame import Surface
import pygame
from component.collider.collider import Collider
from component.collider.rect_collider import RectangleCollider
from core.entity import Entity


COLOR = (110, 110, 110)
COLLISION_TRIGGERED_COLOR = (255, 50, 50)

class TestRectangleEntity(Entity):
    width: float
    height: float
    x: float
    y: float

    def __init__(self, pos_x: float, pos_y: float, width: float, height: float) -> None:
        super().__init__()
        self.x = pos_x
        self.y = pos_y
        self.width = width
        self.height = height
        self.color = COLOR
        collider = RectangleCollider((self.x, self.y), width, height)
        super().register_component(collider)

    def draw(self, surface: Surface):
        pygame.draw.rect(surface, self.color, (self.x, self.y, self.width, self.height))
    
    def on_collision(self, collider: Collider):
        pass
    
    def on_collision_enter(self, collider: Collider):
        self.set_color_collision_triggered()
    
    def on_collision_exit(self, collider: Collider):
        self.set_color_default()

    def set_color_default(self):
        self.color = COLOR

    def set_color_collision_triggered(self):
        self.color = COLLISION_TRIGGERED_COLOR