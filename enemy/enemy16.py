import random
from enemy import enemy
import pyxel
import math


class Enemy16(enemy.Enemy):
    def __init__(self, x, y, width, height, hp, color):
        super().__init__(x, y, width, height, hp, color)
        self.shot_positions.append(enemy.ShotPosition(self.x, self.y))
        self.bullet_speed = 1.5

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

        if self.hp < 320 and self.count % 20 == 0:
            self.shot_positions[0].pattern3(12, 30, 1.5)

        self.move_pattern1(0.5, 0.3, 1, 2, -math.pi / 2, self.count / 140)

    def draw(self):
        super().draw()
