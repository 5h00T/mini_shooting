import pyxel
import math


class Bullet():

    def __init__(self, radius, x, y, movement_x, movement_y, speed, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.collision_radius = self.radius * 0.3
        self.speed = speed
        self.color = color
        self.count = 0
        self.movement_x = movement_x
        self.movement_y = movement_y
        self.is_active = False
        self.move_func = None

    def update(self):
        if self.is_active:
            self.count += 1
            self.x += self.movement_x * self.speed
            self.y += self.movement_y * self.speed
            # print(self.x, self.y)

            if self.move_func is not None:
                try:
                    next(self.move_func)
                except StopIteration:
                    self.move_func = None

        if self.x < -10 or self.x > pyxel.width + 10 or self.y < 0 - 10 or self.y > pyxel.height + 10:
            self.is_active = False
            self.count = 0

    def draw(self):
        if self.is_active:
            pyxel.circ(self.x, self.y, self.radius, self.color)


class EnemyBullet(Bullet):

    def __init__(self, radius, x, y, movement_x, movement_y, speed, color):
        super().__init__(radius, x, y, movement_x, movement_y, speed, color)
        self.count = 0

    def update(self):
        super().update()

    def draw(self):
        super().draw()

    def set_move_function(self, move_function):
        self.move_func = move_function

    def pattern1(self, move1_count, stop_count, angle, speed):
        while True:
            if self.count == move1_count:
                self.movement_x = self.movement_y = 0
            elif self.count == move1_count + stop_count:
                self.movement_x = math.cos(math.radians(angle))
                self.movement_y = math.sin(math.radians(angle))
                self.speed = speed
                break

            yield None

    def pattern2(self, a, min_speed, max_speed):
        while True:
            self.speed += a
            if not (min_speed < self.speed < max_speed):
                break

            yield None


class PlayerBullet(Bullet):

    def __init__(self, radius, x, y, movement_x, movement_y, speed, color):
        super().__init__(radius, x, y, movement_x, movement_y, speed, color)

    def update(self):
        super().update()

    def draw(self):
        super().draw()
