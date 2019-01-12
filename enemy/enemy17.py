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
        self.bit_formation = {"1": {"x": self.x + 50, "y": self.y + 50, "bit_object": None},
                              "2": {"x": self.x - 50, "y": self.y + 50, "bit_object": None},
                              "3": {"x": self.x, "y": self.y + 50, "bit_object": None}}

    def update(self):
        super().update()

        if self.count % 10 == 0 and len(self.bits) < 3:
            self.shot_positions[0].pattern15(sigma=18, speed=1.7)

        print(len(self.bits))
        if self.count % 180 == 0 and len(self.bits) < 3:
            for i in self.bit_formation.keys():
                print(self.bit_formation[i]["bit_object"])
                if self.bit_formation[i]["bit_object"] is None:
                    bit = enemy.Bit(self.x, self.y, 15, 15, 0, 0, 50, 12, {"x": self.x + (int(i) - 2) * 50,
                                                                           "y": self.y + 50})
                    bit.set_move_function(bit.move_pattern3(bit.x, bit.y, bit.const_parameter["x"], bit.const_parameter["y"], 0, 60))
                    self.bits.append(bit)
                    self.bit_formation[i]["bit_object"] = bit
                    break
                elif self.bit_formation[i]["bit_object"].is_active is False:
                    self.bit_formation[i]["bit_object"] = None

        self.move_pattern1(0.3, 0.3, 1, 2, -math.pi / 2, self.count / 140)

        if self.count > 300:
            # self.move_pattern1(0.3, 0.3, 1, 2, -math.pi / 2, self.count / 140)
            pass

    def draw(self):
        super().draw()
