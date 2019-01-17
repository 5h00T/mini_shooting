from enemy import enemy4
import pyxel
from . import mission


class Mission4(mission.Mission):

    def __init__(self):
        print("Mission4")
        self.enemy = enemy4.Enemy4(pyxel.width / 2, 20, 16, 16, 180, 8)
        super().__init__()

    def update(self):
        super().update()

    def draw(self):
        super().draw()

    def collision_detection(self):
        super().collision_detection()
