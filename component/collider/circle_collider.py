from component.collider.collider import Collider


class CircleCollider(Collider):
    position: tuple
    radious: float

    def __init__(self, radious: float, position: tuple, is_trigger: bool = False) -> None:
        self.radious = radious
        self.position = position
        super().__init__(is_trigger)

    def set_position(self, position: tuple) -> None:
        self.position = position