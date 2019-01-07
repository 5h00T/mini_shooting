import random
import enemy
import math


class Enemy7(enemy.Enemy):
    def __init__(self, x, y, width, height, hp, color):
        super().__init__(x, y, width, height, hp, color)
        self.shot_positions.append(enemy.ShotPosition(self.x - 10, self.y))
        self.shot_positions.append(enemy.ShotPosition(self.x + 10, self.y))
        self.shot_positions.append(enemy.ShotPosition(self.x, self.y + 10))
        self.shot_positions.append(enemy.ShotPosition(self.x, self.y - 10))
        self.shot_positions.append(enemy.ShotPosition(self.x, self.y))

    def update(self):
        super().update()
        if self.count % 9 == 0:
            angle = self.count * 2.4
            self.shot_positions[0].pattern1(angle, 0.6)
            self.shot_positions[1].pattern1(angle, 0.6)
            self.shot_positions[2].pattern1(angle, 0.6)
            self.shot_positions[3].pattern1(angle, 0.6)

        if self.count % 40 == 0 or (self.count > 600 and self.count % 23 == 0):
            self.shot_positions[4].pattern2(2)

    def draw(self):
        super().draw()
