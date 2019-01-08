from enemy import enemy1
import pyxel
from . import mission

class Mission1(mission.Mission):

    def __init__(self):
        print("Mission1")
        self.enemy = enemy1.Enemy1(pyxel.width / 2, 20, 16, 16, 240, 8)
        super().__init__()

    def update(self):
        super().update()

    def draw(self):
        super().draw()

    def collision_detection(self):
        super().collision_detection()
