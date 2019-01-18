from scene import Scene


class Mission():
    """
    ミッション中のクラスを保持して管理、記録の更新を行う
    """

    def __init__(self, mission, best_time):
        self.mission = mission()
        self.best_time = best_time
        self.mission_number = int(''.join([ch for ch in self.mission.__class__.__name__[-2:] if ch.isdecimal()]))
        # 挑戦回数を追加
        with open("score.txt", "rt") as f:
            record_list = f.readlines()
            new_record_list = record_list
        record = record_list[self.mission_number][:-1].split(",")
        new_record_list[self.mission_number] = "{0},{1},{2},{3}\n".format(record[0], record[1], str(int(record[2]) + 1),
                                                                          record[3])
        with open("score.txt", "wt") as f:
            f.writelines(new_record_list)

    def update(self):
        self.mission.update()

        if self.mission.return_value["status"] == "clear":

            # クリア回数を追加
            with open("score.txt", "rt") as f:
                record_list = f.readlines()
                new_record_list = record_list
            record = record_list[self.mission_number][:-1].split(",")
            # 最高記録または初回クリアの時にBestTimeを更新
            if self.best_time > self.mission.return_value["time"] or self.best_time == 0:
                new_record_list[self.mission_number] = "{0},{1},{2},{3}\n".format(record[0], str(int(record[1]) + 1),
                                                                                  record[2],
                                                                                  self.mission.return_value["time"])
            else:
                new_record_list[self.mission_number] = "{0},{1},{2},{3}\n".format(record[0], str(int(record[1]) + 1),
                                                                                  record[2],
                                                                                  record[3])
            with open("score.txt", "wt") as f:
                f.writelines(new_record_list)

            return Scene.MISSION_SELECT, self.mission_number

        if self.mission.return_value["status"] == "exit":
            return Scene.MISSION_SELECT, self.mission_number

        return Scene.NO_SCENE_CHANGE, 0

    def draw(self):
        self.mission.draw()
