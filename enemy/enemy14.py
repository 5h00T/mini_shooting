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
        self.move_functions.append(self.move_pattern1(0.4, 1.1, 2, 5, -math.pi / 2, 0.02))
        self.set_shot_function(self.shot_positions[0].pattern11(10, 36, random.randint(0, 360), 7, 0.8, 0.18, 45))

    def update(self):
        super().update()

        if self.count % 80 == 0 and len(self.bits) < 4:
            bit = enemy.Bit(self.x, self.y, 10, 10, 0, 0, 12, 4, {
                "move_speed": random.uniform(0.020, 0.040),
                "direction": 1 if random.random() > 0.5 else -1})
            bit.set_move_function(bit.move_pattern1(bit.const_parameter["direction"] * 1.4, 1.2, 2, 3, math.pi / 2,
                                 bit.const_parameter["move_speed"]))
            bit.set_shot_function(bit.shot_position.pattern3(2, 15, 2.6, 120))
            self.bits.append(bit)


    def draw(self):
        super().draw()
