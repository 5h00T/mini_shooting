import random
import enemy
import math
import player


class Enemy9(enemy.Enemy):
    def __init__(self, x, y, width, height, hp, color):
        super().__init__(x, y, width, height, hp, color)
        self.shot_positions.append(enemy.ShotPosition(self.x, self.y))

    def update(self):
        super().update()
        for bit in self.bits:
            if bit.is_active:
                bit.move_pattern2(1.8)

        if self.count % 25 == 0:
            for bit in self.bits:
                if bit.is_active:
                    bit.shot_position.pattern1(0, 1.3)
                    bit.shot_position.pattern1(180, 1.3)

        if self.count > 130 and self.count % 10 == 0 and len(self.bits) < 5:
            player_x, player_y = player.Player.getPosition()
            angle_to_player = math.atan2(player_y - self.y, player_x - self.x)
            self.bits.append(enemy.Bit(self.x, self.y, 10, 10, math.cos(angle_to_player),
                                            math.sin(angle_to_player), 4, 4))

        if self.count % 50 == 0:
            self.shot_positions[0].pattern3(3, 9, 1.8)

    def draw(self):
        super().draw()