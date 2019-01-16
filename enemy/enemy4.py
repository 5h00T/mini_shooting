from enemy import enemy
import math


class Enemy4(enemy.Enemy):
    def __init__(self, x, y, width, height, hp, color):
        super().__init__(x, y, width, height, hp, color)
        self.shot_positions.append(enemy.ShotPosition(self.x, self.y))
        angle_function = lambda count: 30 * math.sin(self.count)
        self.set_shot_function(self.shot_positions[0].pattern1(90, 1.8, 2, 0, math.inf, angle_function))
        self.set_shot_function(self.shot_positions[0].pattern1(-90, 1.8, 10, 0, math.inf, angle_function))
        self.set_shot_function(self.shot_positions[0].pattern1(0, 1.8, 10, 0, math.inf, angle_function))
        self.set_shot_function(self.shot_positions[0].pattern1(180, 1.8, 10, 0, math.inf, angle_function))

    def update(self):
        super().update()

    def draw(self):
        super().draw()
