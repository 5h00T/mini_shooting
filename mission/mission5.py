from enemy import enemy5
import pyxel
from . import mission


class Mission5(mission.Mission):

    def __init__(self):
        print("Mission5")
        self.enemy = enemy5.Enemy5(pyxel.width / 2, 40, 16, 16, 50, 8)
        super().__init__()

    def update(self):
        super().update()

    def draw(self):
        super().draw()

    def collision_detection(self):
        super().collision_detection()
