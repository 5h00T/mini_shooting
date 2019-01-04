import enemy1
import pyxel
import player
from . import mission

class Mission2(mission.Mission):

    def __init__(self):
        print("Mission2")
        self.enemy = enemy1.Enemy1(pyxel.width / 2, 20, 16, 16, 300, 8)
        super().__init__()

    def update(self):
        super().update()

    def draw(self):
        super().draw()

    def collision_detection(self):
        super().collision_detection()
