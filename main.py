import pyxel
import bullet
import enemy1
import time
import random
import player
import bullet_pool


class App:
    def __init__(self):
        pyxel.init(width=189, height=252, caption="shooting", fps=60)
        self.x = 2
        self.frame30_start = time.time()
        self.frame30 = 0
        self.player = player.Player(100, 200, 10, 10, 2, 3)
        self.enemy = enemy1.Enemy1(pyxel.width / 2 - 7 , 10, 15, 15, 8)
        pyxel.run(self.update, self.draw)

    def update(self):
        self.enemy.update()
        self.player.update()

        if 0 == pyxel.frame_count % 60:
            self.frame30 = (time.time() - self.frame30_start) * 60
            self.frame30_start = time.time()


    def draw(self):
        pyxel.cls(7)
        self.player.draw()
        self.enemy.draw()
        pyxel.text(100, 220, str(self.frame30), 3)
        pyxel.text(100, 240, str(pyxel.frame_count), 3)


App()
