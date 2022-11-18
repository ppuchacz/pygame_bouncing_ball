class KeyManager:
    def __init__(self) -> None:
        self.keys = {}

    def register_up(self, code: int):
        if self.keys.get(code) != None:
            self.keys.pop(code)

    def register_down(self, code: int):
        self.keys[code] = True

    def get_pressed(self) -> dict:
        return self.keys
