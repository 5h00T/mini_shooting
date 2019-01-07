import pyxel
from scene import Scene
import missions

class MissionSelect():

    def __init__(self, cursor_position):
        print("MissionSelect")
        self.cursor = cursor_position
        self.missions = ["mission" + i for i in missions.missions.keys()]
        self.menu_item = ["MissionSelect", "Settings", "Exit"]
        self.is_active = True

    def update(self):
        if pyxel.btnp(pyxel.KEY_UP, 30, 30):
            self.cursor = max(1, self.cursor - 1)
        elif pyxel.btnp(pyxel.KEY_DOWN, 30, 30):
            self.cursor = min(len(self.missions), self.cursor + 1)

        if pyxel.btnp(pyxel.KEY_Z, 10, 10):
            print(self.cursor)
            for mission_number in range(1, len(self.missions) + 1):
                if self.cursor == mission_number:
                    return Scene.MISSION, mission_number

        if pyxel.btn(pyxel.KEY_X):
            return Scene.MENU, 0

        return Scene.NO_SCENE_CHANGE, 0

    def draw(self):
        pyxel.text(10, 120, self.menu_item[0], 8)
        pyxel.text(10, 140, self.menu_item[1], 5)
        pyxel.text(10, 160, self.menu_item[2], 5)

        for i in range(0, len(self.missions)):
            if i+1 == self.cursor:
                pyxel.text(67, 120, self.missions[i], 8)
            elif i+1 > self.cursor:
                pyxel.text(67 + abs(self.cursor - i)**1.1 * 5, 120 - (self.cursor - i) * 10 + 20, self.missions[i], 5)
            else:
                pyxel.text(67 + abs(self.cursor - i) ** 1.1 * 5, 120 - (self.cursor - i) * 10, self.missions[i],5)
