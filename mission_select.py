import pyxel
from scene import Scene
import missions

class MissionSelect():

    def __init__(self, cursor_position):
        print("MissionSelect")
        self.cursor = cursor_position
        self.missions = ["mission" + i for i in missions.missions.keys()]
        self.mission_recode = [i for i in open("score.txt").readlines()]
        self.recode_list = ["0", "0", "0", "0"]
        self.menu_item = ["MissionSelect", "Quit"]
        self.is_active = True

    def update(self):
        if pyxel.btnp(pyxel.KEY_UP, 30, 20):
            self.cursor = max(1, self.cursor - 1)
        elif pyxel.btnp(pyxel.KEY_DOWN, 30, 20):
            self.cursor = min(len(self.missions), self.cursor + 1)

        self.recode_list = self.mission_recode[self.cursor].split(",")

        if pyxel.btnp(pyxel.KEY_Z, 10, 10):
            for mission_number in range(1, len(self.missions) + 1):
                if self.cursor == mission_number:
                    return Scene.MISSION, mission_number, int(self.recode_list[2]), int(self.recode_list[3])

        if pyxel.btn(pyxel.KEY_X):
            return Scene.MENU, 0

        return Scene.NO_SCENE_CHANGE, 0

    def draw(self):
        pyxel.text(10, 120, self.menu_item[0], 8)
        pyxel.text(10, 140, self.menu_item[1], 5)

        for i in range(0, len(self.missions)):
            if i+1 == self.cursor:
                pyxel.text(67, 120, self.missions[i], 8)
            elif i+1 > self.cursor:
                pyxel.text(67 + abs(self.cursor - i-1) ** 1.1 * 5,
                           120 - (self.cursor - i) * 10 + 20, self.missions[i], 5)
            else:
                pyxel.text(67 + abs(self.cursor - i-1) ** 1.1 * 5,
                           120 - (self.cursor - i) * 10 + 10, self.missions[i], 5)

        recode_text = "HISTORY:{0}/{1} BESTTIME:{2}".format(self.recode_list[1], self.recode_list[2], self.recode_list[3])
        pyxel.text(67, 130, recode_text, 5)
