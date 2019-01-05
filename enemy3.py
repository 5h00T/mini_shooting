import bullet_pool
import bullet
import pyxel
import enemy
import math


class Enemy3(enemy.Enemy):
    def __init__(self, x, y, width, height, hp, color):
        super().__init__(x, y, width, height, hp, color)
        self.shot_positions.append(enemy.ShotPosition(self.x, self.y))

    def update(self):
        super().update()
        if self.count % 70 == 0:
            self.shot_positions[0].pattern3(3, 18, 1.1)

        self.move_pattern1(1, 1, 2, math.pi/2, self.count/20)

    def draw(self):
        super().draw()
