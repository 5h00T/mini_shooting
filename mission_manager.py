import pyxel


class Mission():

    def __init__(self, mission):
        print("Mission", mission)
        self.mission = mission()

    def update(self):
        self.mission.update()

        if self.mission.return_value == 2:
            return 2

        if pyxel.btn(pyxel.KEY_Q):
            return 2

    def draw(self):
        self.mission.draw()

