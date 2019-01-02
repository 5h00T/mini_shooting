import pyxel
import mission_select
import menu
import sys

class SceneManager():

    def __init__(self):
        print("SceneManager")
        self.scene = menu.Menu()

    def update(self):
        scene_transition = self.scene.update()
        if scene_transition == 1:
            print("1")
            self.scene = menu.Menu()
        elif scene_transition == 2:
            print("2")
            self.scene = mission_select.MissionSelect()
        elif scene_transition == 3:
            print("3")
        elif scene_transition == 4:
            print("4")
            exit()


    def draw(self):
        self.scene.draw()
