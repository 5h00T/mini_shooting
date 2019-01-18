from enemy import enemy3
import pyxel
from . import mission


class Mission3(mission.Mission):

    def __init__(self):
        self.enemy = enemy3.Enemy3(pyxel.width / 2, 20, 16, 16, 200, 8)
        super().__init__()

    def update(self):
        super().update()

    def draw(self):
        super().draw()

    def collision_detection(self):
        super().collision_detection()
