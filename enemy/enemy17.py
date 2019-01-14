import random
from enemy import enemy
import pyxel
import math


class Enemy17(enemy.Enemy):
    def __init__(self, x, y, width, height, hp, color):
        super().__init__(x, y, width, height, hp, color)
        self.shot_positions.append(enemy.ShotPosition(self.x, self.y))
        self.bullet_speed = 1.5
        self.shot_count = 0
        self.move_functions.append(self.move_pattern1(0.4, 0.8, 1, 6, math.pi / 2, 0.008))
        self.bit_formation = {"1": {"x": self.x, "y": self.y + 50, "bit_object": None},
                              "2": {"x": self.x - 50, "y": self.y + 50, "bit_object": None},
                              "3": {"x": self.x + 50, "y": self.y + 50, "bit_object": None}}

    def update(self):
        super().update()

        if self.count % 9 == 0 and len(self.bits) < 3:
            self.shot_positions[0].pattern15(sigma=15, speed=1.8)

        print(len(self.bits))
        if self.count % 180 == 0 and len(self.bits) < 3:
            for i in self.bit_formation.keys():
                if self.bit_formation[i]["bit_object"] is None:
                    bit = enemy.Bit(self.x, self.y, 15, 15, 0, 0, 50, 12, {"x": self.x + (int(i) - 2) * 50,
                                                                           "y": self.y + 50,
                                                                           "attack_pattern": random.choice([1, 2, 3]),
                                                                           "shot_count": 0})
                    bit.set_move_function(bit.move_pattern3(bit.x, bit.y, bit.const_parameter["x"], bit.const_parameter["y"], 0, 60))
                    self.bits.append(bit)
                    self.bit_formation[i]["bit_object"] = bit
                    break

        for i in self.bit_formation.keys():
            print(self.bit_formation[i]["bit_object"])
            if self.bit_formation[i]["bit_object"] is not None:
                if self.bit_formation[i]["bit_object"].is_active is False:
                    print("None")
                    self.bit_formation[i]["bit_object"] = None

        for bit in self.bits:
            if bit.const_parameter["attack_pattern"] == 1:
                self.bit_attack_pattern1(bit)
            elif bit.const_parameter["attack_pattern"] == 2:
                self.bit_attack_pattern2(bit)
            elif bit.const_parameter["attack_pattern"] == 3:
                self.bit_attack_pattern3(bit)

    def draw(self):
        super().draw()

    def bit_attack_pattern1(self, bit):
        if bit.is_active:
            if bit.count % 180 == 0:
                bit.const_parameter["shot_count"] = 0

            if bit.count % 5 == 0 and bit.count >= 180 and bit.const_parameter["shot_count"] < 10:
                bit.shot_position.pattern16(2, 19, math.sin(bit.count / 5) * 5, 1, 2.4, 1)
                bit.const_parameter["shot_count"] += 1

    def bit_attack_pattern2(self, bit):
        if bit.is_active:
            if bit.count % 140 == 0 and bit.count >= 130:
                angle = random.randint(0, 360)
                bit.shot_position.pattern14(18, angle, 0, 1, 0.8, 60, 50, 0, 0, math.inf)
                bit.shot_position.pattern14(18, angle + 10, 0, 1, 0.6, 60, 50, 0, 0, math.inf)

    def bit_attack_pattern3(self, bit):
        if bit.is_active:
            if bit.count % 150 == 0:
                bit.const_parameter["shot_count"] = 0

            if bit.count % 140 == 0 and bit.count >= 130:
                bit.shot_position.pattern3(1, 0, 1.8)
                bit.shot_position.pattern3(2, 12, 1.6)
                bit.shot_position.pattern3(3, 14, 1.4)
                bit.shot_position.pattern3(4, 16, 1.2)

                bit.const_parameter["shot_count"] += 1
