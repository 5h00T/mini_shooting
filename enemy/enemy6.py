import random

from enemy import enemy
import math


class Enemy6(enemy.Enemy):
    def __init__(self, x, y, width, height, hp, color):
        super().__init__(x, y, width, height, hp, color)
        self.shot_positions.append(enemy.ShotPosition(self.x - 20, self.y))
        self.shot_positions.append(enemy.ShotPosition(self.x + 20, self.y))
        self.shot_positions.append(enemy.ShotPosition(self.x, self.y))
        self.move_functions.append(self.move_pattern1(0.5, 0.9, 1, 2, math.pi / 2, 0.04))
        angle_function = lambda count: 100 * math.sin(count / 30)
        self.set_shot_function(self.shot_positions[0].pattern1(0, 4, 2, 0, math.inf, angle_function))
        self.set_shot_function(self.shot_positions[1].pattern1(180, 4, 2, 0, math.inf, angle_function))
        self.set_shot_function(self.shot_positions[2].pattern17(0, 360, 0.8, 5))

    def update(self):
        super().update()

    def draw(self):
        super().draw()
