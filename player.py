import pyxel


class Player():
    x = -10
    y = -10
    def __init__(self, x, y, width, height, collision_radius, speed):
        Player.x = x
        Player.y = y
        self.width = width
        self.height = height
        self.view_start_x = self.x - self.width / 2
        self.view_start_y = self.y - self.height / 2
        self.collision_radius = collision_radius
        self.speed = speed
        self.slow_speed = 0.5

    def update(self):
        self.move()

    def draw(self):
        pyxel.rect(self.view_start_x, self.view_start_y, self.view_start_x + self.width,
                   self.view_start_y + self.height, 9)
        pyxel.pix(self.x, self.y, 12)

    def move(self):
        is_slanting = False
        slanting_speed = 0.71
        if (pyxel.btn(pyxel.KEY_RIGHT) or pyxel.btn(pyxel.KEY_LEFT)) and \
            (pyxel.btn(pyxel.KEY_UP) or pyxel.btn(pyxel.KEY_DOWN)):
            is_slanting = True

        if pyxel.btn(pyxel.KEY_RIGHT):
            Player.x += self.speed * (slanting_speed if is_slanting else 1)
            self.view_start_x = self.x - self.width / 2
            self.view_start_y = self.y - self.height / 2
        elif pyxel.btn(pyxel.KEY_LEFT):
            Player.x -= self.speed * (slanting_speed if is_slanting else 1)
            self.view_start_x = self.x - self.width / 2
            self.view_start_y = self.y - self.height / 2

        if pyxel.btn(pyxel.KEY_UP):
            Player.y -= self.speed * (slanting_speed if is_slanting else 1)
            self.view_start_x = self.x - self.width / 2
            self.view_start_y = self.y - self.height / 2
        elif pyxel.btn(pyxel.KEY_DOWN):
            Player.y += self.speed * (slanting_speed if is_slanting else 1)
            self.view_start_x = self.x - self.width / 2
            self.view_start_y = self.y - self.height / 2

    @classmethod
    def getPosition(cls):
        return cls.x, cls.y
