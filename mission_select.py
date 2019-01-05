import pyxel
from scene import Scene


class MissionSelect():

    def __init__(self):
        print("MissionSelect")
        self.cursor = 0
        self.missions = ["mission1", "mission2", "mission3", "mission4", "mission5", "mission6", "mission7"]
        self.is_active = True

    def update(self):
        if pyxel.btnp(pyxel.KEY_UP, 30, 30):
            self.cursor = max(0, self.cursor - 1)
        elif pyxel.btnp(pyxel.KEY_DOWN, 30, 30):
            self.cursor = min(len(self.missions) - 1, self.cursor + 1)

        if pyxel.btnp(pyxel.KEY_Z, 10, 10):
            if self.cursor == 0:
                return Scene.MISSION, 1
            elif self.cursor == 1:
                return Scene.MISSION, 2
            elif self.cursor == 2:
                return Scene.MISSION, 3
            elif self.cursor == 3:
                return Scene.MISSION, 4
            elif self.cursor == 4:
                return Scene.MISSION, 5
            elif self.cursor == 5:
                return Scene.MISSION, 6
            elif self.cursor == 6:
                return Scene.MISSION, 7

        if pyxel.btn(pyxel.KEY_X):
            return Scene.MENU, 0

        return Scene.NO_SCENE_CHANGE, 0

    def draw(self):
        for i in range(len(self.missions)):
            if i == self.cursor:
                pyxel.text(67, 100 + i * 20, self.missions[i], 8)
            else:
                pyxel.text(77, 100 + i * 20, self.missions[i], 5)
