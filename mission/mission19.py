from enemy import enemy19
import pyxel
from . import mission


class Mission19(mission.Mission):

    def __init__(self):
        self.enemy = enemy19.Enemy19(pyxel.width / 2, 100, 16, 16, 400, 8)
        super().__init__()

    def update(self):
        super().update()

    def draw(self):
        super().draw()

    def collision_detection(self):
        super().collision_detection()
