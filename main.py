import pyxel
import bullet
import time
import random
import bullet_pool


class App:
    def __init__(self):
        pyxel.init(width=189, height=252, caption="shooting", fps=60)
        self.bullets = []
        self.bullet_pool = bullet_pool.BulletPool(1000)
        self.x = 2
        self.frame30_start = time.time()
        self.frame30 = 0
        pyxel.run(self.update, self.draw)

    def update(self):
        for i in range(10):
            bullet = self.bullet_pool.get_bullet(1, random.randint(0, 240), 0, 0, 0, 0)
            if bullet:
                self.bullets.append(bullet)

        for bullet in self.bullets:
            bullet.update()
            if not bullet.is_active:
                self.bullets.remove(bullet)

        if 0 == pyxel.frame_count % 60:
            self.frame30 = (time.time() - self.frame30_start) * 60
            self.frame30_start = time.time()

        print(len(self.bullets))

    def draw(self):
        pyxel.cls(7)
        pyxel.text(100, 220, str(self.frame30), 3)
        pyxel.text(100, 240, str(pyxel.frame_count), 3)
        for b in self.bullets:
            b.draw()


App()
