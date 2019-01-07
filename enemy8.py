import random
import enemy
import math


class Enemy8(enemy.Enemy):
    def __init__(self, x, y, width, height, hp, color):
        super().__init__(x, y, width, height, hp, color)
        self.shot_positions.append(enemy.ShotPosition(self.x, self.y))

    def update(self):
        super().update()
        for bit in self.bits:
            if bit.is_active:
                bit.move_pattern1(bit.const_parameter["direction"], 1, 2, 3, math.pi / 2,
                                  self.count / bit.const_parameter["move_speed"])

        if self.count % 25 == 0:
            for bit in self.bits:
                if bit.is_active:
                    bit.shot_position.pattern1(random.randint(50, 130), 2)

        if self.count > 130 and self.count % 90 == 0 and len(self.bits) < 5:
            self.bits.append(enemy.Bit(self.x, self.y, 10, 10, 15, 4, {
                "move_speed": random.randint(30, 60),
                "direction": 1 if random.random() > 0.5 else -1}))

        if self.count % 50 == 0:
            self.shot_positions[0].pattern3(3, 9, 1.8)

    def draw(self):
        super().draw()
