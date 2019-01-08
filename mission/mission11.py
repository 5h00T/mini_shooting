from enemy import enemy11
import pyxel
from . import mission

class Mission11(mission.Mission):

    def __init__(self):
        print("Mission11")
        self.enemy = enemy11.Enemy11(pyxel.width / 2, 60, 16, 16, 250, 8)
        super().__init__()

    def update(self):
        super().update()

    def draw(self):
        super().draw()

    def collision_detection(self):
        super().collision_detection()
