from enemy import enemy
import math


class Enemy5(enemy.Enemy):
    def __init__(self, x, y, width, height, hp, color):
        super().__init__(x, y, width, height, hp, color)
        self.shot_positions.append(enemy.ShotPosition(self.x, self.y))
        self.move_functions.append(self.move_pattern1(1.6, 0.5, 1, 2, math.pi / 2, 0.03))
        angle_function1 = lambda count: 26 * math.sin(count / 20)
        angle_function2 = lambda count: -26 * math.sin(count / 20)
        self.set_shot_function(self.shot_positions[0].pattern1(130, 4, 2, 0, math.inf, angle_function1))
        self.set_shot_function(self.shot_positions[0].pattern1(50, 4, 2, 0, math.inf, angle_function2))
        self.set_shot_function(self.shot_positions[0].pattern1(90, 0.8, 10, 0, math.inf, angle_function1))

    def update(self):
        super().update()

    def draw(self):
        super().draw()
