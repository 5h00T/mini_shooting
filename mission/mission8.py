from enemy import enemy8
import pyxel
from . import mission


class Mission8(mission.Mission):

    def __init__(self):
        self.enemy = enemy8.Enemy8(pyxel.width / 2, 40, 16, 16, 220, 8)
        super().__init__()

    def update(self):
        super().update()

    def draw(self):
        super().draw()

    def collision_detection(self):
        super().collision_detection()
