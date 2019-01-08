import random
import enemy
import math
import player
import numpy as np


class Enemy9(enemy.Enemy):
    def __init__(self, x, y, width, height, hp, color):
        super().__init__(x, y, width, height, hp, color)
        self.shot_positions.append(enemy.ShotPosition(self.x, self.y))

    def update(self):
        super().update()
        for bit in self.bits:
            if bit.is_active:
                bit.move_pattern2(1.8)

        if self.count % 50 == 0:
            for bit in self.bits:
                if bit.is_active:
                    bit.shot_position.pattern1(0, 1.3)
                    bit.shot_position.pattern1(180, 1.3)

        if self.count > 130 and self.count % 150 == 0:
            player_x, player_y = player.Player.getPosition()
            angle_to_player = math.atan2(player_y - self.y, player_x - self.x)
            for i in np.arange(0.4, 1.3, 0.2):
                self.bits.append(enemy.Bit(self.x, self.y, 10, 10, math.cos(angle_to_player) * i,
                                           math.sin(angle_to_player) * i, 6, 4))

        if self.count % 90 == 0:
            self.shot_positions[0].pattern5(7, 2, 5, 1, 0.2)

    def draw(self):
        super().draw()
