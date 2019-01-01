import pyxel
from bullet import bullet
import time
import random


class App:
    def __init__(self):
        pyxel.init(width=189, height=252, caption="shooting", fps=60)
        self.bullets = []
        self.x = 2
        self.frame30_start = time.time()
        self.frame30 = 0
        pyxel.run(self.update, self.draw)

    def update(self):
        for i in range(2):
            self.bullets.append(bullet(1, random.randint(0, pyxel.width), 0, 0, 0, 0))
            """
            self.x += 10
            if self.x > pyxel.width:
                self.x = 2
            """

        for b in self.bullets[::]:
            b.update()
            if b.delete_ok:
                self.bullets.remove(b)

        if pyxel.frame_count % 60 == 0:
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