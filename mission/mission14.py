from enemy import enemy14
import pyxel
from . import mission


class Mission14(mission.Mission):

    def __init__(self):
        print("Mission14")
        self.enemy = enemy14.Enemy14(pyxel.width / 2, 40, 16, 16, 210, 8)
        super().__init__()

    def update(self):
        super().update()

    def draw(self):
        super().draw()

    def collision_detection(self):
        super().collision_detection()
