import enemy9
import pyxel
from . import mission

class Mission9(mission.Mission):

    def __init__(self):
        print("Mission8")
        self.enemy = enemy9.Enemy9(pyxel.width / 2, 40, 16, 16, 220, 8)
        super().__init__()

    def update(self):
        super().update()

    def draw(self):
        super().draw()

    def collision_detection(self):
        super().collision_detection()
