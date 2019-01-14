import random
from enemy import enemy
import pyxel
import math


class Enemy18(enemy.Enemy):
    def __init__(self, x, y, width, height, hp, color):
        super().__init__(x, y, width, height, hp, color)
        self.shot_positions.append(enemy.ShotPosition(self.x, self.y))
        self.bullet_speed = 1.5
        self.move_functions.append(self.move_pattern1(0.5, 0.3, 1, 2, -math.pi / 2, 0.05, 0, math.inf))

    def update(self):
        super().update()

        if self.count % 240 == 0:
            self.bullet_speed = 1.5
            shot_angle = random.randint(0, 360)
            for i in range(14):
                self.shot_positions[0].pattern14(10, shot_angle+i*1.5, 40.0+i*2, 0.1+i*0.06, 0, 80, 25+i*3, 0.015, 0.001, 4)

        if (self.count+120) % 240 == 0:
            self.bullet_speed = 1.5
            shot_angle = random.randint(0, 360)
            for i in range(14):
                self.shot_positions[0].pattern14(10, shot_angle-i*1.5, -40.0-i*2, 0.1+i*0.06, 0, 80, 25+i*3, 0.02, 0.001, 4)

        if self.hp < 320 and self.count % 60 == 0:
            self.shot_positions[0].pattern3(8, 45, 1.5)

        if self.hp < 130 and self.count % 30 == 0:
            self.shot_positions[0].pattern7(12, random.randint(0, 360), 1.9)

    def draw(self):
        super().draw()
