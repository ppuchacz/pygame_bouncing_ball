import math
from component.collider.circle_collider import CircleCollider
from component.collider.collider import Collider
from component.collider.rect_collider import RectangleCollider
from core.scene import Scene


class CollisionCheck:
    colliders = []
    triggers = []
    
    def load_colliders(self, scene: Scene):
        entities = scene.find_entities_having_component(Collider)
        for entity in entities:
            collider = entity.get_component(Collider)
            self.colliders.append(collider)
            if collider.is_trigger:
                self.triggers.append(collider)

    def update(self) -> None:
        for trigger in self.triggers:
            for collider in self.colliders:
                if trigger.entity == collider.entity:
                    continue
                collision_detected = self.check_collision(trigger, collider)
                if collision_detected:
                    trigger.entity.on_collision(collider)
                    collider.entity.on_collision(collider)
                    trigger.update_collision_status(True, collider)
                else:
                    trigger.update_collision_status(False, collider)

    def check_collision(self, trigger, collider) -> bool:
        circleCollider = None
        rectangleCollider = None

        if isinstance(trigger, CircleCollider):
            circleCollider = trigger

        if isinstance(collider, CircleCollider):
            circleCollider = collider

        if isinstance(trigger, RectangleCollider):
            rectangleCollider = trigger

        if isinstance(collider, RectangleCollider):
            rectangleCollider = collider
        
        if circleCollider is None or rectangleCollider is None:
            raise Exception("Collision detection strategy not known for colliders with type {} and {}".format(type(trigger), type(collider)))
        
        return self.check_circle_rectangle_collision(circleCollider, rectangleCollider)
    
    # possibly refactor to use strategy
    def check_circle_rectangle_collision(self, circleCollider: CircleCollider, rectCollider: RectangleCollider) -> bool:
        # check distance between centers
        circle_center = circleCollider.position
        rect_center = [rectCollider.position[0] + rectCollider.width / 2, rectCollider.position[1] + rectCollider.height / 2]

        # check horizontal dist
        rect_center_x_pos = rect_center[0]
        circle_center_x_pos = circle_center[0]
        h_dist = math.dist([rect_center_x_pos], [circle_center_x_pos])

        # check vertical dist
        rect_center_y_pos = rect_center[1]
        circle_center_y_pos = circle_center[1]
        v_dist = math.dist([rect_center_y_pos], [circle_center_y_pos])

        if h_dist <= rectCollider.width / 2 + circleCollider.radious and v_dist <= rectCollider.height / 2 + circleCollider.radious:
            return True

        return False

