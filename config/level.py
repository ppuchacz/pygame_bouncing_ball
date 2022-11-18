class Level:
    width: int
    height: int
    margin_top: int
    margin_right: int
    margin_bottom: int
    margin_left: int
    cell_spacing_v: int
    cell_spacing_h: int
    data: list

    def __init__(self, width: int, height: int, margin_top: int, margin_right: int, margin_bottom: int, margin_left: int, cell_spacing_v: int, cell_spacing_h: int, data: list) -> None:
        self.width = width
        self.height = height
        self.margin_top = margin_top
        self.margin_right = margin_right
        self.margin_bottom = margin_bottom
        self.margin_left = margin_left
        self.cell_spacing_v = cell_spacing_v
        self.cell_spacing_h = cell_spacing_h
        self.data = data
