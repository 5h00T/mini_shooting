from enemy import enemy18
import pyxel
from . import mission


class Mission18(mission.Mission):

    def __init__(self):
        self.enemy = enemy18.Enemy18(pyxel.width / 2, 80, 16, 16, 550, 8)
        super().__init__()

    def update(self):
        super().update()

    def draw(self):
        super().draw()

    def collision_detection(self):
        super().collision_detection()
