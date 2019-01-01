import pyxel


class bullet():

    def __init__(self, radius, x, y, vx, vy, color):
        self.x = x
        self.y = y
        self.radius = radius
        self. vx = vx
        self.vy = vy
        self.color = color
        self.count = 0
        self.is_active = False

    def update(self):
        if self.is_active:
            self.count += 1
            self.y += 0.8

        if self.x < -10 or self.x > pyxel.width + 10 or self.y < 0 - 10 or self.y > pyxel.height + 10:
            self.is_active = False
            self.count = 0

    def draw(self):
        if self.is_active:
            pyxel.circ(self.x, self.y, self.radius, self.color)
