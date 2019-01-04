import pyxel
import enum


class Menu():

    def __init__(self):
        print("Menu")
        self.cursor = 0
        self.menu_item = ["MissionSelect", "Settings", "Exit"]
        self.is_active = True

    def update(self):
        if pyxel.btnp(pyxel.KEY_UP, 30, 30):
            self.cursor = max(0, self.cursor - 1)
        elif pyxel.btnp(pyxel.KEY_DOWN, 30, 30):
            self.cursor = min(2, self.cursor + 1)

        if pyxel.btnp(pyxel.KEY_Z, 10, 10):
            if self.cursor == 0:
                return 2, 0
            elif self.cursor == 1:
                return 3, 0
            elif self.cursor == 2:
                return 4, 0

        return 0, 0

    def draw(self):
        for i in range(len(self.menu_item)):
            if i == self.cursor:
                pyxel.text(50, 150 + i * 20, self.menu_item[i], 8)
            else:
                pyxel.text(60, 150 + i * 20, self.menu_item[i], 5)


