import random
from enemy import enemy
import math


class Enemy12(enemy.Enemy):
    def __init__(self, x, y, width, height, hp, color):
        super().__init__(x, y, width, height, hp, color)
        self.shot_positions.append(enemy.ShotPosition(self.x, self.y))
        self.shot_count = 0
        self.start_angle = 0
        self.delta_angle2 = 60

    def update(self):
        super().update()

        if self.count % 140 == 0:
            self.shot_count = 0
            self.start_angle = random.randint(0, 360)
            self.delta_angle2 = 60 if self.delta_angle2 < 0 else -60

        if self.shot_count < 16 and self.count % 4 == 0:
            self.shot_positions[0].pattern8(14, self.start_angle, self.delta_angle2, 1.7, 2, 25, 20)
            self.start_angle += -8 - self.shot_count*0.3 if self.delta_angle2 >= 0 else 8 + self.shot_count * 0.3
            self.delta_angle2 += 3 - self.shot_count*0.1 if self.delta_angle2 > 0 else -3 + self.shot_count*0.1
            self.shot_count += 1

        self.move_pattern1(0.4, 0.3, 2, 3, -math.pi / 2, self.count / 30)

    def draw(self):
        super().draw()
