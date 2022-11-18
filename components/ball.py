from pygame import Surface
import pygame


COLOR = (0, 20, 150)
RADIOUS = 5

TR = (1, -1)
TM = (0, -1)
TL = (-1, -1)
BR = (1, 1)
BM = (0, 1)
BL = (-1, 1)
MR = (1, 0)
ML = (-1, 0)

class Ball:
    def __init__(self) -> None:
        self.position = [0, 0]
        self.direction = [0, 0]
        self.speed = 100.0

    def draw(self, surface: Surface):
        pygame.draw.circle(surface, COLOR, self.position, RADIOUS)

    def update(self):
        self.move()
    
    def move(self):
        self.position[0] += self.direction[0]
        self.position[1] += self.direction[1]