from pygame import Surface
import pygame
from component.collider.collider import Collider
from component.collider.rect_collider import RectangleCollider

from config.player import PlayerConfig
from core.entity import Entity

COLOR = (100, 150, 20)
COLLISION_TRIGGERED_COLOR = (255, 50, 50)


class Player(Entity):
    def __init__(self, config: PlayerConfig) -> None:
        super().__init__()
        self.color = COLOR
        self.config = config
        self.position = [0, 0]
        self.size = self.config.initial_size
        self.reset_position()
        self.size = config.initial_size
        self.delta_time = 0.0
        self.collider = RectangleCollider((self.get_pos_x(), self.get_pos_y()), self.get_width(), self.get_height())
        super().register_component(self.collider)
    
    def on_key_up(self, code):
        # print(code)
        pass

    def on_key_down(self, code):
        # print(code)
        pass

    def on_key_pressed(self, code):
        if code == pygame.K_a:
            self.step_left()
        if code == pygame.K_d:
            self.step_right()
    
    def step_left(self):
        self.position[0] -= self.config.speed * self.get_delta_time()

    def step_right(self):
        self.position[0] += self.config.speed * self.get_delta_time()

    def draw(self, surface: Surface):
        rect = (self.get_pos_x(), self.get_pos_y(), self.get_width(), self.get_height())
        pygame.draw.rect(surface, self.color, rect)
    
    def update(self, delta_time: float):
        self.delta_time = delta_time
        self.collider.set_position(self.position)

    def reset_position(self):

        def _get_screen_size_x() -> int:
            return self.config.screen_size[0]
        
        def _get_screen_size_y() -> int:
            return self.config.screen_size[1]

        plane_width = self.get_width()
        plane_height = self.get_height()
        center_x = (_get_screen_size_x() - plane_width) / 2
        bottom_pos = _get_screen_size_y() - plane_height - self.config.bottom_margin
        self.position = [center_x, bottom_pos]

    def get_width(self):
        return self.config.width_per_size_level * self.size

    def get_height(self):
        return self.config.height

    def get_pos_x(self):
        return self.position[0]

    def get_pos_y(self):
        return self.position[1]
    
    def get_position_center(self):
        return [
            self.position[0] + self.get_width() / 2,
            self.position[1] + self.get_height() / 2,
        ]
    
    def get_delta_time(self):
        return self.delta_time

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