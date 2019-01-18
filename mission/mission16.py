from enemy import enemy16
import pyxel
from . import mission


class Mission16(mission.Mission):

    def __init__(self):
        self.enemy = enemy16.Enemy16(pyxel.width / 2, 80, 16, 16, 400, 8)
        super().__init__()

    def update(self):
        super().update()

    def draw(self):
        super().draw()

    def collision_detection(self):
        super().collision_detection()
