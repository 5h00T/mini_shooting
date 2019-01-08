import random

from enemy import enemy
import math


class Enemy6(enemy.Enemy):
    def __init__(self, x, y, width, height, hp, color):
        super().__init__(x, y, width, height, hp, color)
        self.shot_positions.append(enemy.ShotPosition(self.x - 20, self.y))
        self.shot_positions.append(enemy.ShotPosition(self.x + 20, self.y))
        self.shot_positions.append(enemy.ShotPosition(self.x, self.y))

    def update(self):
        super().update()
        if self.count % 2 == 0:
            self.shot_positions[0].pattern1(0 + 100 * math.sin(self.count / 30), 4)
            self.shot_positions[1].pattern1(180 + 100 * math.sin(self.count / 30), 4)

        if self.count % 5 == 0:
            self.shot_positions[2].pattern1(random.uniform(0, 360), 0.8)

        self.move_pattern1(0.5, 0.9, 1, 2, math.pi / 2, self.count / 30)

    def draw(self):
        super().draw()
