import random
from enemy import enemy
import math


class Enemy10(enemy.Enemy):
    def __init__(self, x, y, width, height, hp, color):
        super().__init__(x, y, width, height, hp, color)
        self.shot_positions.append(enemy.ShotPosition(self.x, self.y))
        self.shot_count = 0
        self.main_shot_target_position = 90

    def update(self):
        super().update()
        for bit in self.bits:
            if bit.is_active:
                bit.move_pattern1(bit.const_parameter["direction"] * 2, 1, 2, 3, math.pi / 2,
                                  self.count / bit.const_parameter["move_speed"])

        for bit in self.bits:
            if bit.is_active and bit.count % 90 == 0:
                bit.shot_position.pattern5(1, 0, 5, 1.9, 0.2)

        if self.count % 80 == 0 and len(self.bits) < 4:
            self.bits.append(enemy.Bit(self.x, self.y, 10, 10, 0, 0, 9, 4, {
                "move_speed": random.randint(20, 50),
                "direction": 1 if random.random() > 0.5 else -1}))

        if self.count % 5 == 0:
            self.shot_count += 1
            self.shot_positions[0].pattern1(self.main_shot_target_position + 68 - self.shot_count * 3, 2)
            self.shot_positions[0].pattern1(self.main_shot_target_position - 68 + self.shot_count * 3, 2)
            if self.shot_count > 20:
                self.shot_count = 0
                self.main_shot_target_position = \
                    max(min(random.randint(self.main_shot_target_position - 10, self.main_shot_target_position + 10),
                            120), -60)

    def draw(self):
        super().draw()
