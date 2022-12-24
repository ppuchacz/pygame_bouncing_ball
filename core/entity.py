from pygame import Surface

from core.component import Component


class Entity:
    def __init__(self) -> None:
        self.components = []
    
    def draw(self, surface: Surface) -> None:
        pass
    
    def update(self, delta_time: float) -> None:
        pass
    
    def on_key_up(self, code) -> None:
        pass
    
    def on_key_down(self, code) -> None:
        pass
    
    def on_key_pressed(self, code) -> None:
        pass

    def register_component(self, component: Component) -> None:
        component.entity = self
        self.components.append(component)
    
    def has_component(self, componentType: type) -> bool:
        for component in self.components:
            if isinstance(component, componentType):
                return True
        
        return False
    
    def get_component(self, componentType) -> Component:
        for component in self.components:
            if isinstance(component, componentType):
                return component
        
        raise Exception("Component of type {} not found in {}".format(componentType, type(self)))