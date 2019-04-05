import pyxel
import bullet_pool
import math


class Player():
    x = -10
    y = -10

    def __init__(self, x, y, width, height, collision_radius, speed):
        Player.x = x
        Player.y = y
        self.width = width
        self.height = height
        self.view_start_x = self.x - self.width / 2  # 長方形の始点
        self.view_start_y = self.y - self.height / 2  # 長方形の始点
        self.collision_radius = collision_radius  # あたり判定
        self.speed = speed
        self.slow_speed = 0.5  # 低速移動したときのスピード
        self.count = 0
        self.bullet_pool = bullet_pool.PlayerBulletPool(28)
        self.bullets = []

    @classmethod
    def getPosition(cls):
        return cls.x, cls.y

    def update(self):
        self.count += 1
        for b in self.bullets[:]:
            b.update()
            if not b.is_active:
                self.bullets.remove(b)
        self.move()

        if pyxel.btnp(pyxel.KEY_Z, 10, 10):
            self.shot(6, -97.5, 3, 5, 1, 1)

    def draw(self):
        pyxel.rect(self.view_start_x, self.view_start_y, self.view_start_x + self.width,
                   self.view_start_y + self.height, 9)
        pyxel.pix(self.x, self.y, 12)
        for b in self.bullets:
            b.draw()

    def move(self):
        is_slanting = False
        slanting_speed = 0.71
        is_slow = False

        if pyxel.btn(pyxel.KEY_LEFT_SHIFT):
            is_slow = True

        # 上または下と左または右が押されたとき移動量を0.71倍する
        if (pyxel.btn(pyxel.KEY_RIGHT) or pyxel.btn(pyxel.KEY_LEFT)) and \
            (pyxel.btn(pyxel.KEY_UP) or pyxel.btn(pyxel.KEY_DOWN)):
            is_slanting = True

        if pyxel.btn(pyxel.KEY_RIGHT):
            Player.x += self.speed * (slanting_speed if is_slanting else 1) * (self.slow_speed if is_slow else 1)
        elif pyxel.btn(pyxel.KEY_LEFT):
            Player.x -= self.speed * (slanting_speed if is_slanting else 1) * (self.slow_speed if is_slow else 1)

        if pyxel.btn(pyxel.KEY_UP):
            Player.y -= self.speed * (slanting_speed if is_slanting else 1) * (self.slow_speed if is_slow else 1)
        elif pyxel.btn(pyxel.KEY_DOWN):
            Player.y += self.speed * (slanting_speed if is_slanting else 1) * (self.slow_speed if is_slow else 1)

        self.view_start_x = Player.x - self.width / 2
        self.view_start_y = Player.y - self.height / 2

        # 画面外に行かないように移動制限
        if self.view_start_x < 0:
            Player.x = self.width / 2
        elif self.view_start_x + self.width >= pyxel.width:
            Player.x = pyxel.width - self.width / 2 - 1

        if self.view_start_y < 0:
            Player.y = self.height / 2
        elif self.view_start_y + self.height >= pyxel.height:
            Player.y = pyxel.height - self.height / 2 - 1

        self.view_start_x = Player.x - self.width / 2
        self.view_start_y = Player.y - self.height / 2

    def shot(self, way, start_angle, delta_angle, speed, radius, color):
        angle = start_angle
        _bullets = []
        for i in range(way):
            b = self.bullet_pool.get_bullet(radius, Player.x, Player.y, math.cos(math.radians(angle)),
                                            math.sin(math.radians(angle)), speed, color)
            angle += delta_angle
            if b:
                _bullets.append(b)
            else:
                for _b in _bullets:
                    _b.is_active = False
                break
        else:
            self.bullets.extend(_bullets)
