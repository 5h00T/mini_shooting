from enemy import enemy


class Enemy2(enemy.Enemy):
    def __init__(self, x, y, width, height, hp, color):
        super().__init__(x, y, width, height, hp, color)
        self.shot_positions.append(enemy.ShotPosition(self.x, self.y))
        self.set_shot_function(self.shot_positions[0].pattern3(3, 18, 1.1, 70))

    def update(self):
        super().update()

    def draw(self):
        super().draw()
