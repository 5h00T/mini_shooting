import random
from enemy import enemy
import math


class Enemy14(enemy.Enemy):
    def __init__(self, x, y, width, height, hp, color):
        super().__init__(x, y, width, height, hp, color)
        self.shot_positions.append(enemy.ShotPosition(self.x, self.y))
        self.shot_count = 0
        self.start_angle = 0
        self.delta_angle2 = 60

    def update(self):
        super().update()

        for bit in self.bits:
            if bit.is_active:
                bit.move_pattern1(bit.const_parameter["direction"] * 1.4, 1.2, 2, 3, math.pi / 2,
                                  self.count / bit.const_parameter["move_speed"])

        for bit in self.bits:
            if bit.is_active and bit.count % 120 == 0:
                bit.shot_position.pattern3(2, 15, 2.6)

        if self.count % 80 == 0 and len(self.bits) < 4:
            self.bits.append(enemy.Bit(self.x, self.y, 10, 10, 0, 0, 9, 4, {
                "move_speed": random.randint(60, 80),
                "direction": 1 if random.random() > 0.5 else -1}))

        if self.count % 45 == 0:
            self.shot_positions[0].pattern11(10, 36, random.randint(0, 360), 7, 0.8, 0.18)

        self.move_pattern1(0.3, 1.1, 2, 5, -math.pi / 2, self.count / 60)

    def draw(self):
        super().draw()
