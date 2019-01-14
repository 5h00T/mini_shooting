import random
from enemy import enemy
import math


class Enemy11(enemy.Enemy):
    def __init__(self, x, y, width, height, hp, color):
        super().__init__(x, y, width, height, hp, color)
        self.shot_positions.append(enemy.ShotPosition(self.x, self.y))
        self.shot_count = 0
        self.start_angle = 0
        self.delta_angle2 = 0

    def update(self):
        super().update()

        if self.count % 70 == 0:
            self.shot_count = 0
            self.start_angle = random.randint(0, 360)
            self.delta_angle2 = 1 if self.delta_angle2 < 0 else -1

        if self.count % 3 == 0 and self.shot_count < 20:
            self.set_shot_function(
                self.shot_positions[0].pattern8(6, self.start_angle, self.delta_angle2, 0.8, 2.1, 50, 20, 1, 0, 1))
            self.start_angle += 9 if self.delta_angle2 >= 0 else -9
            self.delta_angle2 += -1 - self.shot_count ** 1.2 if self.delta_angle2 < 0 else 1 + self.shot_count ** 1.2
            self.shot_count += 1

    def draw(self):
        super().draw()
