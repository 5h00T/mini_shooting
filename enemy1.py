import bullet_pool
import bullet
import pyxel
import enemy


class Enemy1(enemy.Enemy):
    def __init__(self, x, y, width, height, color):
        super().__init__(x, y, width, height, color)

    def update(self):
        super().update()
        if self.count % 30 == 0:
            b = self.bullet_pool.get_bullet(2, self.center_x, self.center_y, 0, 0, 0)
            if b:
                self.bullets.append(b)

    def draw(self):
        super().draw()
