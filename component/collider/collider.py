from core.component import Component


class Collider(Component):
    def __init__(self, is_trigger: bool = False) -> None:
        self.is_trigger = is_trigger
        self.colliders_during_collision = []
    
    def update_collision_status(self, collision_detected: bool, collider) -> None:
        def _find_collider(wanted):
            for c in self.colliders_during_collision:
                if c == wanted:
                    return c
            return None

        if _find_collider(collider) and not collision_detected:
            self.colliders_during_collision.remove(collider)
            self.entity.on_collision_exit(collider)
            collider.entity.on_collision_exit(collider)
        
        if not _find_collider(collider) and collision_detected:
            self.colliders_during_collision.append(collider)
            self.entity.on_collision_enter(collider)
            collider.entity.on_collision_enter(collider)