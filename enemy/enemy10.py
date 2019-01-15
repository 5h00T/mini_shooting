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

        if self.count % 80 == 0 and len(self.bits) < 4:
            bit = enemy.Bit(self.x, self.y, 10, 10, 0, 0, 9, 4, {
                "move_speed": random.uniform(0.01, 0.05),
                "direction": 1 if random.random() > 0.5 else -1})
            self.bits.append(bit)
            bit.set_shot_function(bit.shot_position.pattern5(1, 0, 5, 1.9, 0.2, 90, 60))
            bit.set_move_function(bit.move_pattern1(bit.const_parameter["direction"] * 2, 1, 2, 3, math.pi / 2,
                                                    bit.const_parameter["move_speed"], 60, math.inf))

        if self.count % 100 == 0:
            angle_function1 = lambda count: -(68 - count/5 * 3)
            angle_function2 = lambda count: 68 - count/5 * 3
            self.set_shot_function(self.shot_positions[0].pattern1(self.main_shot_target_position, 2, 5, 0, 105, angle_function1))
            self.set_shot_function(self.shot_positions[0].pattern1(self.main_shot_target_position, 2, 5, 0, 105, angle_function2))
            self.main_shot_target_position = \
                max(min(random.randint(self.main_shot_target_position - 10, self.main_shot_target_position + 10),
                        105), 75)

    def draw(self):
        super().draw()
