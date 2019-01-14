import random
from enemy import enemy
import math


class Enemy13(enemy.Enemy):
    def __init__(self, x, y, width, height, hp, color):
        super().__init__(x, y, width, height, hp, color)
        self.shot_positions.append(enemy.ShotPosition(self.x, self.y))
        self.shot_positions.append(enemy.ShotPosition(self.x-13, self.y))
        self.shot_positions.append(enemy.ShotPosition(self.x+13, self.y))
        self.shot_count = 0
        self.start_angle = 0
        self.delta_angle2 = 60
        self.move_functions.append(self.move_pattern1(2, 1.4, 2, 5, -math.pi / 2, 0.04))

    def update(self):
        super().update()

        if self.count % 140 == 0:
            self.shot_count = 0

        if self.count % 5 == 0 and self.shot_count < 5:
            self.shot_positions[0].pattern10(3, 18, 90, 1.9)
            self.shot_count += 1

        if self.count % 14 == 0:
            target_angle = random.randint(0, 360)
            self.shot_positions[1].pattern7(3, target_angle, 1.2)
            self.shot_positions[2].pattern7(3, target_angle, 1.2)

    def draw(self):
        super().draw()
