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
        # self.move_functions.append(self.move_pattern1(0.4, 0.4, 1, 2, -math.pi / 2, 0.005))
        for start_angle in range(0, 360, 30):
            self.set_shot_function(
                self.shot_positions[0].pattern19(start_angle, 2.1, 21, 180, math.inf, 1, 0, 60, lambda count: 16, lambda count: math.sin(self.count / 140) * 3)
            )
        start_angle = random.randint(0, 360)
        self.set_shot_function(self.shot_positions[1].pattern19(start_angle, 1.5, 20, 0, angle_function=lambda count: 7))
        self.set_shot_function(self.shot_positions[2].pattern19(start_angle + 90, 1.5, 20, 0, angle_function=lambda count: -7))
        self.set_shot_function(self.shot_positions[3].pattern19(start_angle + 180, 1.5, 20, 0, angle_function=lambda count: 7))
        self.set_shot_function(self.shot_positions[4].pattern19(start_angle + 270, 1.5, 20, 0, angle_function=lambda count: -7))

    def update(self):
        super().update()

    def draw(self):
        super().draw()
