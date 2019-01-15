import random
from enemy import enemy
import pyxel
import math
import player
import numpy as np


class Enemy20(enemy.Enemy):
    def __init__(self, x, y, width, height, hp, color):
        super().__init__(x, y, width, height, hp, color)
        self.shot_positions.append(enemy.ShotPosition(self.x, self.y))
        self.shot_positions.append(enemy.ShotPosition(self.x-20, self.y-20))
        self.shot_positions.append(enemy.ShotPosition(self.x-20, self.y+20))
        self.shot_positions.append(enemy.ShotPosition(self.x+20, self.y-20))
        self.shot_positions.append(enemy.ShotPosition(self.x+20, self.y+20))
        self.pattern1_init = False
        self.pattern2_init = False
        self.pattern3_init = False
        self.pattern4_init = False
        self.shot_count = 0
        # self.set_move_function(self.move_pattern2(self.x, self.y, 100, 200, 0, 300))

    def update(self):
        super().update()

        self.shot_count += 1
        if self.shot_count < 600 and self.pattern1_init is False:
            self.pattern1_init = True
            angle_function = lambda count: random.randint(0, 360)
            self.set_shot_function(self.shot_positions[0].pattern18(0, 2.5, 2, 90, 600, angle_function))
            self.set_shot_function(self.shot_positions[1].pattern18(0, 1.3, 4, 90, 600, angle_function))
            self.set_shot_function(self.shot_positions[2].pattern18(0, 1.3, 4, 90, 600, angle_function))
            self.set_shot_function(self.shot_positions[3].pattern18(0, 1.3, 4, 90, 600, angle_function))
            self.set_shot_function(self.shot_positions[4].pattern18(0, 1.3, 4, 90, 600, angle_function))
        elif 670 < self.shot_count < 1300:
            if self.pattern2_init is False:
                self.pattern2_init = True

            if self.shot_count % 50 == 0:
                player_x, player_y = player.Player.getPosition()
                angle_to_player = math.atan2(player_y - self.y, player_x - self.x)
                for i in range(3):
                    bit = enemy.Bit(self.x, self.y, 10, 10, math.cos(angle_to_player),
                                    math.sin(angle_to_player), 7, 4)
                    bit.set_move_function(bit.move_pattern2(1.2 + i * 0.3))
                    bit.set_shot_function(bit.shot_position.pattern1(math.degrees(angle_to_player) + 20, 1.4, 40))
                    bit.set_shot_function(bit.shot_position.pattern1(math.degrees(angle_to_player) - 20, 1.4, 40))
                    self.bits.append(bit)
                    bit.set_return_shot(bit.shot_position.pattern14(10, random.randint(0, 360), 0, 3, 0, 2, 60,  0.01, -1, math.inf, 1, 0, 1, None))
        elif self.shot_count == 1420:
            for i in range(3):
                for angle in range(0, 181, 20):
                    bit = enemy.Bit(self.x, self.y, 10, 10, math.cos(math.radians(angle)),
                                    math.sin(math.radians(angle)), 7, 4)
                    bit.set_move_function(bit.move_pattern2(0.3 + i * 0.3))
                    bit.set_shot_function(bit.shot_position.pattern1(angle + 90, 1.4, 40, 0, math.inf))
                    bit.set_shot_function(bit.shot_position.pattern1(angle - 90, 1.4, 40, 0, math.inf))
                    self.bits.append(bit)
                    bit.set_return_shot(
                        bit.shot_position.pattern14(10, random.randint(0, 360), 0, 3, 0, 2, 60, 0.01, -1, math.inf, 1, 0, 1,
                                                    None))
        elif 2000 < self.shot_count < 2900:
            if self.pattern3_init is False:
                self.pattern3_init = True
                self.set_move_function(self.move_pattern1(1, 1, 2, 3, math.pi / 6, 0.02, 0, 800))
                angle_function = lambda count: random.randint(0, 360)
                angle = random.randint(0, 360)
                self.set_shot_function(
                    self.shot_positions[0].pattern14(5, angle, 0, 2, 1.6, 40, 50, 0, -1, math.inf, 30, 0, 800,
                                                     angle_function))

                self.set_shot_function(
                    self.shot_positions[0].pattern14(5, angle + 36, 0, 2, 1.1, 40, 50, 0, -1, math.inf, 30, 0, 800,
                                                     angle_function))
                angle = random.randint(0, 360)
                self.set_shot_function(
                    self.shot_positions[1].pattern14(5, angle, 0, 2, 1.6, 40, 50, 0, -1, math.inf, 30, 0, 800,
                                                     angle_function))

                self.set_shot_function(
                    self.shot_positions[1].pattern14(5, angle + 36, 0, 2, 1.1, 40, 50, 0, -1, math.inf, 30, 0, 800,
                                                     angle_function))
                angle = random.randint(0, 360)
                self.set_shot_function(
                    self.shot_positions[2].pattern14(5, angle, 0, 2, 1.6, 40, 50, 0, -1, math.inf, 30, 0, 800,
                                                     angle_function))

                self.set_shot_function(
                    self.shot_positions[2].pattern14(5, angle + 36, 0, 2, 1.1, 40, 50, 0, -1, math.inf, 30, 0, 800,
                                                     angle_function))
                angle = random.randint(0, 360)
                self.set_shot_function(
                    self.shot_positions[3].pattern14(5, angle, 0, 2, 1.6, 40, 50, 0, -1, math.inf, 30, 0, 800,
                                                     angle_function))
                self.set_shot_function(
                    self.shot_positions[3].pattern14(5, angle + 36, 0, 2, 1.1, 40, 50, 0, -1, math.inf, 30, 0, 800,
                                                     angle_function))
                angle = random.randint(0, 360)
                self.set_shot_function(
                    self.shot_positions[4].pattern14(5, angle, 0, 2, 1.6, 40, 50, 0, -1, math.inf, 30, 0, 800,
                                                     angle_function))
                self.set_shot_function(
                    self.shot_positions[4].pattern14(5, angle + 36, 0, 2, 1.1, 40, 50, 0, -1, math.inf, 30, 0, 800,
                                                     angle_function))
        elif self.shot_count == 3000:
            self.set_move_function(self.move_pattern2(self.x, self.y, pyxel.width / 2, 70, 0, 50))
        elif self.shot_count == 3100:
            angle = random.randint(0, 360)

            self.set_shot_function(
                self.shot_positions[0].pattern14(20, angle, 0, 1.3, 1.6, 40, 50, 0, -1, math.inf, 1, 0, 1))
            self.set_shot_function(
                self.shot_positions[0].pattern14(20, angle + 9, 0, 1.3, 1.1, 40, 50, 0, -1, math.inf, 1, 0, 1))
            angle = random.randint(0, 360)
            self.set_shot_function(
                self.shot_positions[1].pattern14(20, angle, 0, 1.3, 1.6, 40, 50, 0, -1, math.inf, 1, 0, 1))
            self.set_shot_function(
                self.shot_positions[1].pattern14(20, angle + 9, 0, 1.3, 1.1, 40, 50, 0, -1, math.inf, 1, 0, 1))
            angle = random.randint(0, 360)
            self.set_shot_function(
                self.shot_positions[2].pattern14(20, angle, 0, 1.3, 1.6, 40, 50, 0, -1, math.inf, 1, 0, 1))
            self.set_shot_function(
                self.shot_positions[2].pattern14(20, angle + 9, 0, 1.3, 1.1, 40, 50, 0, -1, math.inf, 1, 0, 1))
            angle = random.randint(0, 360)
            self.set_shot_function(
                self.shot_positions[3].pattern14(20, angle, 0, 1.3, 1.6, 40, 50, 0, -1, math.inf, 1, 0, 1))
            self.set_shot_function(
                self.shot_positions[3].pattern14(20, angle + 9, 0, 1.3, 1.1, 40, 50, 0, -1, math.inf, 1, 0, 1))
            angle = random.randint(0, 360)
            self.set_shot_function(
                self.shot_positions[4].pattern14(20, angle, 0, 1.3, 1.6, 40, 50, 0, -1, math.inf, 1, 0, 1))
            self.set_shot_function(
                self.shot_positions[4].pattern14(20, angle + 9, 0, 1.3, 1.1, 40, 50, 0, -1, math.inf, 1, 0, 1))
        elif self.shot_count == 3300:
            self.shot_count = 0
            self.pattern1_init = False
            self.pattern2_init = False
            self.pattern3_init = False

    def draw(self):
        super().draw()
