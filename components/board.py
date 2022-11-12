from utils import clone_list

WIDTH = 100
HEIGHT = 100
CELLS_HOTIZONTAL = 10
CELLS_VERTICAL = 10
MARGIN_TOP = 10
MARGIN_LEFT = 10
MARGIN_RIGHT = 10

class Board:
    board = []
    def __init__(self, level) -> None:
        self.board = clone_list(level)
        Board.validate_level(level)
    def draw(self, screen):
        for self.board

    def validate_level(level):
        if not isinstance(level, list):
            raise 
