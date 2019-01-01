import numpy as np
import pyxel


class bullet():

    def __init__(self, radius, x, y, vx, vy, color):
        self.x = x
        self.y = y
        self.radius = radius
        self. vx = vx
        self.vy = vy
        self.color = color
        self.count = 0

    def update(self):
        self.count += 1
        self.y += 1

    def draw(self):
        pyxel.circ(self.x, self.y, self.radius, self.color)
