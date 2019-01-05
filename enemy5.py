import enemy
import math


class Enemy5(enemy.Enemy):
    def __init__(self, x, y, width, height, hp, color):
        super().__init__(x, y, width, height, hp, color)
        self.shot_positions.append(enemy.ShotPosition(self.x, self.y))

    def update(self):
        super().update()
        if self.count % 2 == 0:
            self.shot_positions[0].pattern1(130 + 26 * math.sin(self.count / 20), 4)
            self.shot_positions[0].pattern1(50 - 26 * math.sin(self.count / 20), 4)

        if self.count % 10 == 0:
            self.shot_positions[0].pattern1(90 + 26 * math.sin(self.count / 20), 0.8)

        self.move_pattern1(1.6, 0.5, 1, 2, math.pi / 2, self.count / 40)

    def draw(self):
        super().draw()
