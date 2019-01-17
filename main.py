import pyxel
import scene_manager
import time
import os


class App:
    def __init__(self):
        pyxel.init(width=189, height=252, caption="shooting", fps=60)
        self.one_second_count = 0
        self.fps_base_time = time.time()
        self.fps = 0
        self.scene_manager = scene_manager.SceneManager()
        # 記録用ファイルがない場合は起動時に作成
        if not os.path.exists("score.txt"):
            with open("score.txt", "wt") as f:
                for mission_number in range(0, 21):
                    f.writelines(str(mission_number) + "," + "0" + "," + "0" + "," + "0" + "\n")

        pyxel.run(self.update, self.draw)

    def update(self):
        self.one_second_count += 1
        self.scene_manager.update()

        now = time.time()
        if now - self.fps_base_time >= 1:
            self.fps = self.one_second_count / (now - self.fps_base_time)
            self.fps_base_time = now
            self.one_second_count = 0

    def draw(self):
        pyxel.cls(7)
        self.scene_manager.draw()
        pyxel.text(173, 246, str(self.fps)[:4], 3)


App()
