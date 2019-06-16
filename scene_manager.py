import pyxel
import mission_select
import menu
from scene import Scene
import mission_manager
import missions
import sys


class SceneManager():

    def __init__(self):
        self.scene = menu.Menu()
        self.mission = 0

    def update(self):
        scene_transition = self.scene.update()
        if scene_transition[0] == Scene.MENU:
            self.scene = menu.Menu()
        elif scene_transition[0] == Scene.MISSION_SELECT:
            self.scene = mission_select.MissionSelect(scene_transition[1])
        elif scene_transition[0] == Scene.SETTINGS:
            pass
        elif scene_transition[0] == Scene.QUIT:
            # pyxel.quit()
            sys.exit()
        elif scene_transition[0] == Scene.MISSION:
            self.scene = mission_manager.Mission(missions.missions[str(scene_transition[1])], scene_transition[2])

    def draw(self):
        self.scene.draw()
