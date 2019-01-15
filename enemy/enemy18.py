import random
from enemy import enemy
import pyxel
import math


class Enemy18(enemy.Enemy):
    def __init__(self, x, y, width, height, hp, color):
        super().__init__(x, y, width, height, hp, color)
        self.shot_positions.append(enemy.ShotPosition(self.x, self.y))

        self.bullet_speed = 1.5
        self.shot_count = 0
        self.pattern1_init = False
        self.pattern2_init = False
        self.pattern3_init = False
        self.first_angle = random.randint(0, 360)
        self.move_functions.append(self.move_pattern1(0.5, 0.3, 1, 2, -math.pi / 2, 0.05, 0, math.inf))

    def update(self):
        super().update()

        if self.shot_count < 600 and self.pattern1_init is False:
            self.pattern1_init = True
            angle1_function = lambda count: count + 20
            for i in range(4):
                self.set_shot_function(
                    self.shot_positions[0].pattern14(3, self.first_angle, 20, 0.8 + i * 0.5, 1.4, 50, 20, 0, 0, 9, 10, 0,
                                                     600, angle1_function))
                self.set_shot_function(
                    self.shot_positions[0].pattern14(3, self.first_angle, -20, 0.8 + i * 0.5, 1.4, 50, 20, 0, 0, 9, 10,
                                                     0, 600, angle1_function))
        elif 650 < self.shot_count < 1300:
            if self.pattern2_init is False:
                self.pattern2_init = True
                self.set_shot_function(self.shot_positions[0].pattern1(120, 2, 2, 0, 650, lambda count: count**1.6))
                self.set_shot_function(
                    self.shot_positions[0].pattern1(60, 2, 2, 0, 650, lambda count: -count ** 1.6))
            if self.shot_count % 80 == 0 and len(self.bits) < 4:
                bit = enemy.Bit(self.x, self.y, 10, 10, 0, 0, 18, 4, {
                    "move_speed": random.uniform(0.010, 0.060),
                    "direction": 1 if random.random() > 0.5 else -1})
                bit.set_move_function(bit.move_pattern1(bit.const_parameter["direction"] * 1.5, 1.3, 2, 3, math.pi / 2,
                                                        bit.const_parameter["move_speed"]))
                bit.set_shot_function(bit.shot_position.pattern3(2, 25, 3.5, 20, 0, math.inf))
                self.bits.append(bit)
        elif self.shot_count > 1400:
            if self.pattern3_init is False:
                self.bits.clear()
                self.move_functions.clear()
                self.pattern3_init = True

            if self.shot_count % 140 == 0:
                for angle in range(70, 430, 40):
                    bit = enemy.Bit(self.x, self.y, 10, 10, math.cos(math.radians(angle)), math.sin(math.radians(angle)), 15, 4, {
                        "first_bullet_angle": random.randint(0, 360)
                    })
                    bit.set_move_function(bit.move_pattern2(2.2))
                    bit.set_shot_function(bit.shot_position.pattern14(1, bit.const_parameter["first_bullet_angle"], 0, 0, 0.1, 60, 60, 0.02, -1, math.inf, 4, 0, math.inf, lambda count: math.sin(count/60) * 3))
                    self.bits.append(bit)

        self.shot_count += 1

    def draw(self):
        super().draw()
