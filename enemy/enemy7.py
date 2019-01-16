import math

from enemy import enemy


class Enemy7(enemy.Enemy):
    def __init__(self, x, y, width, height, hp, color):
        super().__init__(x, y, width, height, hp, color)
        self.shot_positions.append(enemy.ShotPosition(self.x - 10, self.y))
        self.shot_positions.append(enemy.ShotPosition(self.x + 10, self.y))
        self.shot_positions.append(enemy.ShotPosition(self.x, self.y + 10))
        self.shot_positions.append(enemy.ShotPosition(self.x, self.y - 10))
        self.shot_positions.append(enemy.ShotPosition(self.x, self.y))
        angle_function = lambda count: 2.4 * count
        self.set_shot_function(self.shot_positions[0].pattern1(0, 0.6, 9, 0, math.inf, angle_function))
        self.set_shot_function(self.shot_positions[1].pattern1(0, 0.6, 9, 0, math.inf, angle_function))
        self.set_shot_function(self.shot_positions[2].pattern1(0, 0.6, 9, 0, math.inf, angle_function))
        self.set_shot_function(self.shot_positions[3].pattern1(0, 0.6, 9, 0, math.inf, angle_function))
        self.set_shot_function(self.shot_positions[4].pattern2(2, 40))
        self.set_shot_function(self.shot_positions[4].pattern2(2, 40, 500))

    def update(self):
        super().update()

    def draw(self):
        super().draw()
