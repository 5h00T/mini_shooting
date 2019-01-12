from enemy import enemy


class Enemy2(enemy.Enemy):
    def __init__(self, x, y, width, height, hp, color):
        super().__init__(x, y, width, height, hp, color)
        self.shot_positions.append(enemy.ShotPosition(self.x, self.y))

    def update(self):
        super().update()
        if self.count % 70 == 0:
            self.shot_positions[0].pattern3(3, 18, 1.1)

    def draw(self):
        super().draw()
