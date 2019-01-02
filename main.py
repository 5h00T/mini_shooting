import pyxel
import game_manager
import time
import menu
import math

class App:
    def __init__(self):
        pyxel.init(width=189, height=252, caption="shooting", fps=60)
        self.frame30_start = time.time()
        self.frame30 = 0
        self.scene_manager = game_manager.SceneManager()
        pyxel.run(self.update, self.draw)

    def update(self):
        self.scene_manager.update()

        if 0 == pyxel.frame_count % 60:
            self.frame30 = (time.time() - self.frame30_start) * 60
            self.frame30_start = time.time()

    def draw(self):
        pyxel.cls(7)
        self.scene_manager.draw()
        pyxel.text(100, 220, str(self.frame30)[:4], 3)
        pyxel.text(100, 240, str(pyxel.frame_count), 3)


App()
