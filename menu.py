import pyxel
from scene import Scene


class Menu():

    def __init__(self):
        print("Menu")
        self.cursor = 0
        self.menu_item = ["MissionSelect", "Quit"]
        self.is_active = True

    def update(self):
        # カーソルが要素外を示さないように制限
        if pyxel.btnp(pyxel.KEY_UP, 30, 30):
            self.cursor = max(0, self.cursor - 1)
        elif pyxel.btnp(pyxel.KEY_DOWN, 30, 30):
            self.cursor = min(1, self.cursor + 1)

        if pyxel.btnp(pyxel.KEY_Z, 10, 10):
            if self.cursor == 0:
                return Scene.MISSION_SELECT, 1
            elif self.cursor == 1:
                return Scene.QUIT, 0

        return Scene.NO_SCENE_CHANGE, 0

    def draw(self):
        for i in range(len(self.menu_item)):
            if i == self.cursor:
                pyxel.text(63, 150 + i * 20, self.menu_item[i], 8)
            else:
                pyxel.text(73, 150 + i * 20, self.menu_item[i], 5)


