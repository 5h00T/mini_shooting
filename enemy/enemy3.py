from enemy import enemy
import math


class Enemy3(enemy.Enemy):
    def __init__(self, x, y, width, height, hp, color):
        super().__init__(x, y, width, height, hp, color)
        self.shot_positions.append(enemy.ShotPosition(self.x, self.y))
        self.set_move_function(self.move_pattern1(2, 0.5, 1, 2, math.pi/2, 0.03))
        self.set_shot_function(self.shot_positions[0].pattern4(6, 60, 2.1, 40))

    def update(self):
        super().update()

    def draw(self):
        super().draw()
