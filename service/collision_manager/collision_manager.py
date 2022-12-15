import math

# class CollisionManager:
#     def resolve_collisions(colliables: list):
#         for collidable in colliables:
#             for collider in colliables:


from .circle_collider import CircleCollider
from .rect_collider import RectangleCollider


def check_circle_rectangle_collision(circleCollider: CircleCollider, rectCollider: RectangleCollider) -> bool:
    # check distance between centers
    circle_center = circleCollider.position
    rect_center = [rectCollider.position[0] + rectCollider.width / 2, rectCollider.position[1] + rectCollider.height / 2]
    # dist = math.dist(circle_center, rectCollider)
    # check if too far
    # rect_pos = [rectCollider.pos_x, rectCollider.pos_y]
    # rect_outer_circle_r = math.dist(rect_pos, rect_center)

    # if rect_outer_circle_r + circleCollider.radious < dist:
    #     return False

    # # check if close engough for sure
    # shorter_edge_len = rectCollider.height if rectCollider.width > rectCollider.height else rectCollider.width
    # rect_inner_circle_r = shorter_edge_len / 2

    # if dist <= rect_inner_circle_r + circleCollider.radious:
    #     return True

    # check intersection


    # check if circle inside rectangle

    # check if rectangle inside circle
    

    # pass
    # ----------------------------------------
    # check horizontal dist
    rect_center_x_pos = rect_center[0]
    circle_center_x_pos = circle_center[0]
    h_dist = math.dist([rect_center_x_pos], [circle_center_x_pos])
    
    # if h_dist > rectCollider.width / 2 + circleCollider.radious:
    #     return False

    # check vertical dist
    rect_center_y_pos = rect_center[1]
    circle_center_y_pos = circle_center[1]
    v_dist = math.dist([rect_center_y_pos], [circle_center_y_pos])

    # if v_dist > rectCollider.height / 2 + circleCollider.radious:
    #     return False

    if h_dist <= rectCollider.width / 2 + circleCollider.radious and v_dist <= rectCollider.height / 2 + circleCollider.radious:
        return True

    return False


def check_circle_rectangle_group_collision(circleCollider: CircleCollider, rectColliders: list) -> bool:
    for rectCollider in rectColliders:
        collisionDetected = check_circle_rectangle_collision(circleCollider, rectCollider)
        if collisionDetected:
            return True
    
    return False