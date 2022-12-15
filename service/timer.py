import pygame


class Timer:
    def __init__(self) -> None:
        self.last_update_time = pygame.time.get_ticks()

    # return time in seconds
    def reset(self) -> float:
        self.delta_time = (pygame.time.get_ticks() - self.last_update_time) / 1000
        self.last_update_time = pygame.time.get_ticks()

        return self.delta_time
