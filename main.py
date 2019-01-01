import pyxel
from bullet import bullet


class App:
    def __init__(self):
        pyxel.init(200, 250)
        self.x = 0
        self.bullet = bullet(4, 20, 0, 0, 0, 4)
        pyxel.run(self.update, self.draw)

    def update(self):
        self.x = (self.x + 1) % pyxel.width
        self.bullet.update()

    def draw(self):
        pyxel.cls(0)
        pyxel.rect(self.x, 0, self.x + 7, 7, 9)
        self.bullet.draw()

App()