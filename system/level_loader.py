from config.level import Level
from core.scene import Scene
from entity.cell import Cell


class LevelLoader:
    def load(level: Level, scene: Scene):
        board_width = level.width - level.margin_left - level.margin_right
        board_height = level.height - level.margin_top - level.margin_bottom
        columns_count = len(level.data[0])
        horizontal_spacing_sum = (columns_count - 1) * level.cell_spacing_h
        cell_width = (board_width - horizontal_spacing_sum) / columns_count
        rows_count = len(level.data)
        vertical_spacing_sum = (rows_count - 1) * level.cell_spacing_v
        cell_height = (board_height - vertical_spacing_sum) / rows_count

        def _add_row(pos_x: float, pos_y: float, cells: list):
            for i, cell_id in enumerate(cells):
                if cell_id == 0:
                    continue
                cell = Cell(cell_width, cell_height, pos_x + i * (cell_width + level.cell_spacing_h), pos_y)
                scene.add_entity(cell)

        for i, row in enumerate(level.data):
            pos_y = level.margin_top + i * (cell_height + level.cell_spacing_v)
            _add_row(level.margin_left, pos_y, row)