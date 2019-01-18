from enemy import enemy15
import pyxel
from . import mission


class Mission15(mission.Mission):

    def __init__(self):
        self.enemy = enemy15.Enemy15(pyxel.width / 2, 40, 16, 16, 300, 8)
        super().__init__()

    def update(self):
        super().update()

    def draw(self):
        super().draw()

    def collision_detection(self):
        super().collision_detection()
