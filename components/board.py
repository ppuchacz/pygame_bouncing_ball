from pygame import Surface
import pygame
from config.level import Level

WIDTH = 800
HEIGHT = 600
MARGIN_TOP = 10
MARGIN_LEFT = 10
MARGIN_RIGHT = 10
CELL_SPACEING_V = 5
CELL_SPACEING_H = 5
CELL_COLOR = (150, 50, 80)


class Cell:
    widht: int
    height: int
    x: int
    y: int

    def __init__(self, widht, height, x, y) -> None:
        self.widht = widht
        self.height = height
        self.x = x
        self.y = y
    
    def draw(self, screen: Surface):
        pygame.draw.rect(screen, CELL_COLOR, (self.x, self.y, self.widht, self.height))



class Board:
    board: list = []
    level: Level

    def __init__(self, level: Level) -> None:
        self.load_level(level)

    def load_level(self, level: Level):
        for row_nr, row in enumerate(level.data):
            for cell_nr, cell in enumerate(row):
                if cell == 0:
                    continue
                cell_count_ver = len(level.data)
                cell_count_hor = len(row)
                cell_width = ((level.width - level.margin_left - level.margin_right) / (cell_count_hor)) - (level.cell_spacing_h * (cell_count_hor - 1) / cell_count_hor)
                cell_height = ((level.height - level.margin_top - level.margin_bottom) / (cell_count_ver)) - (level.cell_spacing_v * (cell_count_ver - 1) / cell_count_ver)
                x_pos = level.margin_left + (cell_nr * (cell_width + level.cell_spacing_h))
                y_pos = level.margin_top + (row_nr * (cell_height + level.cell_spacing_v))
                self.board.append(Cell(cell_width, cell_height, x_pos, y_pos))


    def draw(self, screen: Surface):
        for cell in self.board:
            cell.draw(screen)
