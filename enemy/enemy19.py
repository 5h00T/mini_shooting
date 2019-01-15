import random
from enemy import enemy
import pyxel
import math


class Enemy19(enemy.Enemy):
    def __init__(self, x, y, width, height, hp, color):
        super().__init__(x, y, width, height, hp, color)
        self.shot_positions.append(enemy.ShotPosition(self.x, self.y))
        self.shot_positions.append(enemy.ShotPosition(self.x-10, self.y-10))
        self.shot_positions.append(enemy.ShotPosition(self.x-10, self.y+10))
        self.shot_positions.append(enemy.ShotPosition(self.x+10, self.y-10))
        self.shot_positions.append(enemy.ShotPosition(self.x+10, self.y+10))
        self.bullet_speed = 1.5
        self.move_functions.append(self.move_pattern1(0.4, 0.4, 1, 2, -math.pi / 2, 0.005))
        self.set_shot_function(
            self.shot_positions[0].pattern19(90, 2, 10, 0, math.inf, lambda count: math.sin(count)))

    def update(self):
        super().update()

        if self.count % 240 == 0:
            shot_angle = random.randint(0, 360)

    def draw(self):
        super().draw()
