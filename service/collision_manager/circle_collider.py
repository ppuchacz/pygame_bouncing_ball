class CircleCollider:
    position: tuple
    radious: float

    def __init__(self, radious: float, position: tuple) -> None:
        self.radious = radious
        self.position = position

    def set_position(self, position: tuple) -> None:
        self.position = position