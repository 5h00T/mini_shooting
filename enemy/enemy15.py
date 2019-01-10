import random
from enemy import enemy
import pyxel
import math


class Enemy15(enemy.Enemy):
    def __init__(self, x, y, width, height, hp, color):
        super().__init__(x, y, width, height, hp, color)
        self.shot_positions.append(enemy.ShotPosition(self.x, self.y))
        self.shot_positions.append(enemy.ShotPosition(0, 0))
        self.shot_positions.append(enemy.ShotPosition(pyxel.width, 0))
        self.shot_count = 0
        self.start_angle = 0
        self.delta_angle2 = 60
        self.position_sigma = 10  # 標準偏差

    def update(self):
        super().update()

        if self.count % 80 == 0 and len(self.bits) < 4:
            self.bits.append(enemy.Bit(self.x, self.y, 10, 10, 0, 0, 9, 4, {
                "move_speed": random.randint(60, 80),
                "direction": 1 if random.random() > 0.5 else -1}))

        if self.count % 1 == 0 and self.count > 160:
            self.shot_positions[1].pattern12(1, 0, random.randint(80, 100), random.gauss(0, self.position_sigma), 0, 2)
            self.shot_positions[2].pattern12(1, 0, random.randint(80, 100), random.gauss(pyxel.width, self.position_sigma), 0, 2)

        if self.count % 30 == 0 and self.position_sigma < 30 and self.count > 330:
            self.position_sigma += 1

        if self.count % 30 == 0 and self.count > 40:
            self.shot_positions[0].pattern3(3, 5, 1.1)

        self.move_pattern1(0.5, 0.5, 3, 2.5, -math.pi / 2, self.count / 90)

    def draw(self):
        super().draw()
