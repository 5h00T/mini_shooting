import enemy1
import pyxel
import player

class Mission2():

    def __init__(self):
        print("Mission1")
        self.player = player.Player(pyxel.width / 2, 200, 10, 10, 2, 2)
        self.enemy = enemy1.Enemy1(pyxel.width / 2, 10, 16, 16, 8)
        self.enemy = enemy1.Enemy1(pyxel.width / 2, 90, 16, 16, 8)

    def update(self):
        self.player.update()
        self.enemy.update()

    def draw(self):
        self.player.draw()
        self.enemy.draw()