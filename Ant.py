import numpy as np
from pygame.draw import rect
from pygame import Rect

"""
Now. position += speed, speed += accel, accel = sum of all forces. kinda works.
"""

class Ant:

    def __init__(
            self,
            x,
            y,
            screen,
            terrain,
            color = (200,0,0)):
        self.position = np.array([x, y])
        self.speed = np.array([0,0])
        self.screen = screen
        self.terrain = terrain
        self.stats = {
            'health': 100,
            }
        self.forces = {
            'food': np.array([0, 0]),
            'home': np.array([0, 0]),
            'pheromone?': np.array([0, 0])
            }
        self.test_force = np.array([0, 0])
        self.color = color
        self.nearby = []

    def move(self, dx=0, dy=0):
        """depraciated"""
        self.position[0] += dx
        self.position[1] += dy

    def update(self):
        acceleration = self.test_force #sum of all forces later
        self.speed = acceleration
        np.clip(self.speed, -3, 3, self.speed) #limit or it'll shoot into infinity
        self.position += self.speed

    def show(self):
        rect(self.screen, self.color, Rect(self.position[0], self.position[1], 1, 1))

    def debug(self):
        print(self.position, self.speed)
