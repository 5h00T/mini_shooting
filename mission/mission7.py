import enemy7
import pyxel
from . import mission


class Mission7(mission.Mission):

    def __init__(self):
        print("Mission7")
        self.enemy = enemy7.Enemy7(pyxel.width / 2, 40, 16, 16, 110, 8)
        super().__init__()

    def update(self):
        super().update()

    def draw(self):
        super().draw()

    def collision_detection(self):
        super().collision_detection()
