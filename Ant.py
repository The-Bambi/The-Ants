import numpy as np

"""
implement vector-based movement!
"""

class Ant:

    def __init__(self, x, y, screen, terrain):
        self.x = x
        self.y = y
        self.position = np.array([self.x, self.y])
        self.speed = np.array([0,0])
        self.screen = screen
        self.terrain = terrain
        self.stats = {
            'health': 100,
            }
        self.vectors = {
            'food': np.array([0, 0]),
            'home': np.array([0, 0]),
            'pheromone?': np.array([0,0])
            }

    def move(self, dx=0, dy=0):
        """depraciated"""
        self.x += dx
        self.y += dy

    def update(self):
        self.speed = 'sum_of_all_vectors'
        self.position += self.speed

    def show(self):
        # self.screen.pokaż_mnie!
        pass

    def debug(self):
        print(self.x, self.y)
