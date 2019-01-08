from enemy import enemy10
import pyxel
from . import mission

class Mission10(mission.Mission):

    def __init__(self):
        print("Mission10")
        self.enemy = enemy10.Enemy10(pyxel.width / 2, 40, 16, 16, 250, 8)
        super().__init__()

    def update(self):
        super().update()

    def draw(self):
        super().draw()

    def collision_detection(self):
        super().collision_detection()
