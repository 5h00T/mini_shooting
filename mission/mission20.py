from enemy import enemy20
import pyxel
from . import mission


class Mission20(mission.Mission):

    def __init__(self):
        print("Mission20")
        self.enemy = enemy20.Enemy20(pyxel.width / 2, 60, 30, 30, 1600, 8)
        super().__init__()

    def update(self):
        super().update()

    def draw(self):
        super().draw()

    def collision_detection(self):
        super().collision_detection()
