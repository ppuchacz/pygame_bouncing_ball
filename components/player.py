from pygame import Surface
import pygame

from config.player import PlayerConfig

COLOR = (100, 150, 20)


class Player:
    def __init__(self, config: PlayerConfig) -> None:
        self.config = config
        self.position = [0, 0]
        self.size = self.config.initial_size
        self.reset_position()
        self.size = config.initial_size
        self.last_update_time = pygame.time.get_ticks()
        self.delta_time = 0.0
    
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
        pygame.draw.rect(surface, COLOR, rect)
    
    def update(self):
        self.delta_time = (pygame.time.get_ticks() - self.last_update_time) / 1000
        self.last_update_time = pygame.time.get_ticks()

    def reset_position(self):
        plane_width = self.get_width()
        plane_height = self.get_height()
        center_x = (self.get_screen_size_x() - plane_width) / 2
        bottom_pos = self.get_screen_size_y() - plane_height - self.config.bottom_margin
        self.position = [center_x, bottom_pos]

    def get_width(self):
        return self.config.width_per_size_level * self.size

    def get_height(self):
        return self.config.height

    def get_pos_x(self):
        return self.position[0]

    def get_pos_y(self):
        return self.position[1]
    
    def get_screen_size_x(self) -> int:
        return self.config.screen_size[0]
    
    def get_screen_size_y(self) -> int:
        return self.config.screen_size[1]
    
    def get_delta_time(self):
        return self.delta_time
