import bullet_pool
import bullet
import pyxel

class Enemy():
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.count = 0

    def update(self):
        self.count += 1

    def draw(self):
        pyxel.rect(self.x, self.y, self.width, self.height, self.color)