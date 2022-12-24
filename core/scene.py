from pygame import Surface

from core.entity import Entity


class Scene:
    entities: list = []

    def add_entity(self, entity: Entity) -> None:
        if not isinstance(entity, Entity):
            raise Exception("Given object is not an instance of Entity")

        self.entities.append(entity)
    
    def draw(self, surface: Surface) -> None:
        for entity in self.entities:
            entity.draw(surface)
    
    def update(self, delta_time: float) -> None:
        for entity in self.entities:
            entity.update(delta_time)
    
    def on_key_up(self, code) -> None:
        for entity in self.entities:
            entity.on_key_up(code)

    def on_key_down(self, code) -> None:
        for entity in self.entities:
            entity.on_key_down(code)

    def on_key_pressed(self, code) -> None:
        for entity in self.entities:
            entity.on_key_pressed(code)

    def find_entities_having_component(self, componentType: type) -> list:
        entities = []
        for entity in self.entities:
            if entity.has_component(componentType):
                entities.append(entity)
        
        return entities