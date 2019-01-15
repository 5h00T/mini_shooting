from enemy import enemy19
import pyxel
from . import mission


class Mission19(mission.Mission):

    def __init__(self):
        print("Mission18")
        self.enemy = enemy19.Enemy19(pyxel.width / 2, 80, 16, 16, 550, 8)
        super().__init__()

    def update(self):
        super().update()

    def draw(self):
        super().draw()

    def collision_detection(self):
        super().collision_detection()
