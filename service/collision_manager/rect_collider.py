class RectangleCollider:
    position: tuple
    width: float
    height: float

    def __init__(self, position: tuple, width: float, height: float) -> None:
        self.position = position
        self.width = width
        self.height = height
    
    def set_position(self, position: tuple) -> None:
        self.position = position
