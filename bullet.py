import pyxel


class Bullet():

    def __init__(self, radius, x, y, movement_x, movement_y, speed, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.collision_radius = self.radius * 0.5
        self.speed = speed
        self.color = color
        self.count = 0
        self.movement_x = movement_x
        self.movement_y = movement_y
        self.is_active = False

    def update(self):
        if self.is_active:
            self.count += 1
            self.x += self.movement_x * self.speed
            self.y += self.movement_y * self.speed
            # print(self.x, self.y)

        if self.x < -10 or self.x > pyxel.width + 10 or self.y < 0 - 10 or self.y > pyxel.height + 10:
            self.is_active = False
            self.count = 0

    def draw(self):
        if self.is_active:
            pyxel.circ(self.x, self.y, self.radius, self.color)


class EnemyBullet(Bullet):

    def __init__(self, radius, x, y, movement_x, movement_y, speed, color):
        super().__init__( radius, x, y, movement_x, movement_y, speed, color)

    def update(self):
        super().update()

    def draw(self):
        super().draw()


class PlayerBullet(Bullet):

    def __init__(self, radius, x, y, movement_x, movement_y, speed, color):
        super().__init__( radius, x, y, movement_x, movement_y, speed, color)

    def update(self):
        super().update()

    def draw(self):
        super().draw()
