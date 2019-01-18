from enemy import enemy17
import pyxel
from . import mission


class Mission17(mission.Mission):

    def __init__(self):
        self.enemy = enemy17.Enemy17(pyxel.width / 2, 35, 16, 16, 180, 8)
        super().__init__()

    def update(self):
        super().update()

    def draw(self):
        super().draw()

    def collision_detection(self):
        super().collision_detection()
