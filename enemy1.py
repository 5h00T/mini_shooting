import bullet_pool
import bullet
import pyxel
import enemy
import math


class Enemy1(enemy.Enemy):
    def __init__(self, x, y, width, height, hp, color):
        super().__init__(x, y, width, height, hp, color)
        self.shot_positions.append(enemy.ShotPosition(self.x, self.y))

    def update(self):
        super().update()
        if self.count % 10 == 0:
            self.shot_positions[0].pattern2(2)

    def draw(self):
        super().draw()
