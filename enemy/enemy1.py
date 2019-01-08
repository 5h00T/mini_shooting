from enemy import enemy


class Enemy1(enemy.Enemy):
    def __init__(self, x, y, width, height, hp, color):
        super().__init__(x, y, width, height, hp, color)
        self.shot_positions.append(enemy.ShotPosition(self.x, self.y))

    def update(self):
        super().update()
        if self.count % 60 == 0:
            self.shot_positions[0].pattern3(1, 11, 1.5)

    def draw(self):
        super().draw()
