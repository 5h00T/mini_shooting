class Mission():

    def __init__(self, mission):
        print("Mission", mission)
        self.mission = mission()

    def update(self):
        self.mission.update()

    def draw(self):
        self.mission.draw()

