import pyxel
from scene import Scene


class Mission():

    def __init__(self, mission):
        print("Mission", mission)
        self.mission = mission()
        self.mission_number = int(self.mission.__class__.__name__[-1])

    def update(self):
        self.mission.update()

        if self.mission.return_value == 2:
            return Scene.MISSION_SELECT, self.mission_number

        if self.mission.return_value == 3:
            return Scene.MISSION_SELECT, self.mission_number

        return Scene.NO_SCENE_CHANGE, 0

    def draw(self):
        self.mission.draw()

