class PlayerConfig:
    screen_size: tuple
    initial_size: int
    width_per_size_level: int
    bottom_margin: int
    height: int
    speed: float # px per sec

    def __init__(self, screen_size: tuple, initial_size: int, width_per_size_level: int, bottom_margin: int, height: int, speed: float) -> None:
        self.screen_size = screen_size
        self.initial_size = initial_size
        self.width_per_size_level = width_per_size_level
        self.bottom_margin = bottom_margin
        self.height = height
        self.speed = speed
