from core.component import Component


class Collider(Component):
    def __init__(self, is_trigger: bool = False) -> None:
        self.is_trigger = is_trigger