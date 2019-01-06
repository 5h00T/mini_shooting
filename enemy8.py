import random
import enemy
import math


class Enemy8(enemy.Enemy):
    def __init__(self, x, y, width, height, hp, color):
        super().__init__(x, y, width, height, hp, color)
        self.bits.append(enemy.Bit(self.x, self.y, 5, 5, 10, 4))

    def update(self):
        super().update()
        for bit in self.bits:
            if bit.is_active:
                bit.move_pattern1(1, 1, 1, 2, math.pi / 2, self.count / 40)

        if self.count % 9 == 0:
            for bit in self.bits:
                if bit.is_active:
                    bit.shot_position.pattern1(90, 2)

        self.move_pattern1(1, 1, 2, 2, math.pi/4, self.count / 30)

    def draw(self):
        super().draw()
