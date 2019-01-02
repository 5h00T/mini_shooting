import pyxel


class Player():

    def __init__(self, x, y, width, height, collision_radius, speed):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.center_x = self.x + self.width / 2
        self.center_y = self.y + self.height / 2
        self.collision_radius = collision_radius
        self.speed = speed
        self.slow_speed = 0.5

    def update(self):
        self.move()

    def draw(self):
        pyxel.rect(self.x, self.y, self.x + self.width, self.y + self.height, 9)

    def move(self):
        is_slanting = False
        slanting_speed = 0.71
        if (pyxel.btn(pyxel.KEY_RIGHT) or pyxel.btn(pyxel.KEY_LEFT)) and \
            (pyxel.btn(pyxel.KEY_UP) or pyxel.btn(pyxel.KEY_DOWN)):
            print("as")
            is_slanting = True

        if pyxel.btn(pyxel.KEY_RIGHT):
            self.x += self.speed * (slanting_speed if is_slanting else 1)
        elif pyxel.btn(pyxel.KEY_LEFT):
            self.x -= self.speed * (slanting_speed if is_slanting else 1)

        if pyxel.btn(pyxel.KEY_UP):
            self.y -= self.speed * (slanting_speed if is_slanting else 1)
        elif pyxel.btn(pyxel.KEY_DOWN):
            self.y += self.speed * (slanting_speed if is_slanting else 1)
