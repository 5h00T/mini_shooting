import pyxel
import mission_select
import menu
import enum
import mission_manager
import missions

class Scene(enum.IntEnum):
    MENU = 1
    MISSION_SELECT = 2
    SETTINGS = 3
    EXIT = 4
    MISSION = 5


class SceneManager():

    def __init__(self):
        print("SceneManager")
        self.scene = menu.Menu()
        self.mission = 0

    def update(self):
        scene_transition = self.scene.update()
        if scene_transition[0] == Scene.MENU:
            print("1")
            self.scene = menu.Menu()
        elif scene_transition[0] == Scene.MISSION_SELECT:
            print("2")
            self.scene = mission_select.MissionSelect()
        elif scene_transition[0] == Scene.SETTINGS:
            print("3")
        elif scene_transition[0] == Scene.EXIT:
            print("4")
            pyxel.quit()
        elif scene_transition[0] == Scene.MISSION:
            print("MISSION")
            self.scene = mission_manager.Mission(missions.missions[str(scene_transition[1])])


    def draw(self):
        self.scene.draw()
