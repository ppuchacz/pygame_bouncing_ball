from config.level import Level
from config.player import PlayerConfig


WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

# CELLS_

LEVEL = Level(
    WINDOW_WIDTH,
    WINDOW_HEIGHT,
    10,
    10,
    300,
    10,
    5,
    5,
    [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 0, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
    ]
)

PLAYER = PlayerConfig(
    (WINDOW_WIDTH, WINDOW_HEIGHT),
    2,
    30,
    20,
    20,
    500.0
)

BALL_INITIAL_POSITION = (100, 100)