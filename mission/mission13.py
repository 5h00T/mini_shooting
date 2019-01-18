from enemy import enemy13
import pyxel
from . import mission


class Mission13(mission.Mission):

    def __init__(self):
        self.enemy = enemy13.Enemy13(pyxel.width / 2, 40, 16, 16, 210, 8)
        super().__init__()

    def update(self):
        super().update()

    def draw(self):
        super().draw()

    def collision_detection(self):
        super().collision_detection()
