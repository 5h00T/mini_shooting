from enemy import enemy12
import pyxel
from . import mission


class Mission12(mission.Mission):

    def __init__(self):
        self.enemy = enemy12.Enemy12(pyxel.width / 2, 90, 16, 16, 210, 8)
        super().__init__()

    def update(self):
        super().update()

    def draw(self):
        super().draw()

    def collision_detection(self):
        super().collision_detection()
