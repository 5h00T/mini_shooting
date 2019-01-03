import bullet_pool
import bullet
import pyxel
import enemy
import math


class Enemy1(enemy.Enemy):
    def __init__(self, x, y, width, height, color):
        super().__init__(x, y, width, height, color)

    def update(self):
        super().update()
        if self.count % 1 == 0:
            self.pattern2(3)

    def draw(self):
        super().draw()
