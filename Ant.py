import numpy as np

"""
implement vector-based movement!
"""

class Ant:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.health = 100
        self.stats = {

                }
        #status, backpack,stats...

    def move(self, dx=0, dy=0):
        self.x += dx
        self.y += dy

    def debug(self):
        print(self.x, self.y)
