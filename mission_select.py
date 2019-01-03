import pyxel


class MissionSelect():

    def __init__(self):
        print("MissionSelect")
        self.cursor = 0
        self.missions = ["mission1", "mission2", "mission3"]
        self.is_active = True

    def update(self):
        if pyxel.btnp(pyxel.KEY_UP, 30, 30):
            self.cursor = max(0, self.cursor - 1)
        elif pyxel.btnp(pyxel.KEY_DOWN, 30, 30):
            self.cursor = min(2, self.cursor + 1)

        if pyxel.btnp(pyxel.KEY_Z, 10, 10):
            if self.cursor == 0:
                return 5, 1
            elif self.cursor == 1:
                return 5, 2
            elif self.cursor == 2:
                return 3

        if pyxel.btn(pyxel.KEY_X):
            return 1

        return 0

    def draw(self):
        for i in range(len(self.missions)):
            if i == self.cursor:
                pyxel.text(50, 150 + i * 20, self.missions[i], 8)
            else:
                pyxel.text(60, 150 + i * 20, self.missions[i], 5)
