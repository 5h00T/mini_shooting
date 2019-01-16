from scene import Scene


class Mission():

    def __init__(self, mission, charenge_times, best_time):
        print("Mission", mission)
        self.mission = mission()
        self.charenge_times = charenge_times
        self.best_time = best_time
        print(self.mission.__class__.__name__[-2:])
        self.mission_number = int(''.join([ch for ch in self.mission.__class__.__name__[-2:] if ch.isdecimal()]))

    def update(self):
        self.mission.update()

        if self.mission.return_value["status"] == "clear":
            # 最高記録または初回クリアの時にBestTimeを更新
            if self.best_time > self.mission.return_value["time"] or self.best_time == 0:
                self.best_time = self.mission.return_value["time"]
                with open("score.txt", "rt") as f:
                    record_list = f.readlines()
                    new_record_list = record_list
                record = record_list[self.mission_number][:-1].split(",")
                new_record_list[self.mission_number] = "{0},{1},{2},{3}\n".format(record[0], record[1], record[2], self.best_time)

                with open("score.txt", "wt") as f:
                    f.writelines(record_list)

            return Scene.MISSION_SELECT, self.mission_number

        if self.mission.return_value["status"] == "exit":
            return Scene.MISSION_SELECT, self.mission_number

        return Scene.NO_SCENE_CHANGE, 0

    def draw(self):
        self.mission.draw()
