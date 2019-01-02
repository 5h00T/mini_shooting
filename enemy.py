import bullet_pool
import bullet
import pyxel
import random

class Enemy():
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.count = 0
        self.center_x = self.x + self.width / 2
        self.center_y = self.y + self.height / 2
        self.bullets = []
        self.bullet_pool = bullet_pool.BulletPool(100)

    def update(self):
        self.count += 1

        for b in self.bullets:
            b.update()
            if not b.is_active:
                self.bullets.remove(b)

    def draw(self):
        pyxel.rect(self.x, self.y, self.x + self.width, self.y + self.height, self.color)
        for b in self.bullets:
            b.draw()