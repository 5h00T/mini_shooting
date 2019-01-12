from enemy import enemy
import math


class Enemy4(enemy.Enemy):
    def __init__(self, x, y, width, height, hp, color):
        super().__init__(x, y, width, height, hp, color)
        self.shot_positions.append(enemy.ShotPosition(self.x, self.y))

    def update(self):
        super().update()
        if self.count % 2 == 0:
            self.shot_positions[0].pattern1(90 + 30 * math.sin(self.count), 1.8)

        if self.count % 10 == 0:
            self.shot_positions[0].pattern1(-90 + 30 * math.sin(self.count), 1.8)
            self.shot_positions[0].pattern1(0 + 30 * math.sin(self.count), 1.8)
            self.shot_positions[0].pattern1(180 + 30 * math.sin(self.count), 1.8)

    def draw(self):
        super().draw()
