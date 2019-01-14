import random
from enemy import enemy
import math


class Enemy8(enemy.Enemy):
    def __init__(self, x, y, width, height, hp, color):
        super().__init__(x, y, width, height, hp, color)
        self.shot_positions.append(enemy.ShotPosition(self.x, self.y))
        self.set_shot_function(self.shot_positions[0].pattern3(3, 9, 1.8, 50))

    def update(self):
        super().update()

        if self.count > 130 and self.count % 90 == 0 and len(self.bits) < 5:
            bit = enemy.Bit(self.x, self.y, 10, 10, 0, 0, 15, 4, {
                "move_speed": random.uniform(0.02, 0.04),
                "direction": 1 if random.random() > 0.5 else -1})
            bit.set_move_function(bit.move_pattern1(bit.const_parameter["direction"], 1, 2, 3, math.pi / 2,
                                  bit.const_parameter["move_speed"], 0, math.inf))
            bit.set_shot_function(bit.shot_position.pattern17(50, 130, 2, 25))
            self.bits.append(bit)

    def draw(self):
        super().draw()
