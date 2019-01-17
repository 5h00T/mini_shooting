import pyxel
import mission_select
import menu
from scene import Scene
import mission_manager
import missions


class SceneManager():

    def __init__(self):
        # print("SceneManager")
        self.scene = menu.Menu()
        self.mission = 0

    def update(self):
        scene_transition = self.scene.update()
        if scene_transition[0] == Scene.MENU:
            print("MENU")
            self.scene = menu.Menu()
        elif scene_transition[0] == Scene.MISSION_SELECT:
            print("MISSION_SELECT")
            self.scene = mission_select.MissionSelect(scene_transition[1])
        elif scene_transition[0] == Scene.SETTINGS:
            print("SETTINGS")
        elif scene_transition[0] == Scene.QUIT:
            print("QUIT")
            pyxel.quit()
        elif scene_transition[0] == Scene.MISSION:
            print("MISSION")
            self.scene = mission_manager.Mission(missions.missions[str(scene_transition[1])], scene_transition[2])

    def draw(self):
        self.scene.draw()
