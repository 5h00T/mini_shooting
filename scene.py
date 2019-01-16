import enum


class Scene(enum.IntEnum):
    NO_SCENE_CHANGE = 0
    MENU = 1
    MISSION_SELECT = 2
    SETTINGS = 3
    QUIT = 4
    MISSION = 5
