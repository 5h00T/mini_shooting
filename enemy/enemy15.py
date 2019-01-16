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
        self.position_sigma = 10  # 標準偏差
        self.move_functions.append(self.move_pattern1(0.5, 0.5, 3, 2.5, -math.pi / 2, 0.01))
        self.set_shot_function(self.shot_positions[0].pattern3(3, 5, 1.1, 40))

    def update(self):
        super().update()

        if self.count % 2 == 0 and self.count > 160:
            self.set_shot_function(
                self.shot_positions[1].pattern12(1, 0, random.randint(80, 100), random.gauss(0, self.position_sigma), 0,
                                                 2, 1, 0, 1))
            self.set_shot_function(self.shot_positions[2].pattern12(1, 0, random.randint(80, 100),
                                                                    random.gauss(pyxel.width, self.position_sigma), 0,
                                                                    2, 1, 0, 1))

        if self.count % 30 == 0 and self.position_sigma < 30 and self.count > 330:
            # 時間が経つにつれ徐々に弾の範囲を広げていく
            self.position_sigma += 1

    def draw(self):
        super().draw()
