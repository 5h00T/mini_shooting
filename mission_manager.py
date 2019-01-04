import pyxel
from scene import Scene


class Mission():

    def __init__(self, mission):
        print("Mission", mission)
        self.mission = mission()

    def update(self):
        self.mission.update()

        if self.mission.return_value == 2:
            return Scene.MISSION_SELECT, 0

        if self.mission.return_value == 3:
            return Scene.MISSION_SELECT, 1

        if pyxel.btn(pyxel.KEY_Q):
            return Scene.MISSION_SELECT, 0

        return Scene.NO_SCENE_CHANGE, 0

    def draw(self):
        self.mission.draw()

