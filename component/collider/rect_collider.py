from component.collider.collider import Collider


class RectangleCollider(Collider):
    position: tuple
    width: float
    height: float

    def __init__(self, position: tuple, width: float, height: float, is_trigger: bool = False) -> None:
        self.position = position
        self.width = width
        self.height = height
        super().__init__(is_trigger)
    
    def set_position(self, position: tuple) -> None:
        self.position = position
