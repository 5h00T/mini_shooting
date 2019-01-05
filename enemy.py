import bullet_pool
import player
import pyxel
import math
import random

class Enemy():
    def __init__(self, x, y, width, height, hp,color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.hp = hp
        self.color = color
        self.count = 0
        self.view_start_x = self.x - self.width / 2
        self.view_start_y = self.y - self.height / 2
        self.shot_positions = []
        self.standard_position = self.x

    def update(self):
        self.count += 1

        for shot_position in self.shot_positions:
            shot_position.update()

    def draw(self):
        pyxel.rect(self.view_start_x, self.view_start_y, self.view_start_x + self.width,
                   self.view_start_y + self.height, self.color)

        for shot_position in self.shot_positions:
            shot_position.draw()

    def move_pattern1(self, A, B, a, b, delta, t):
        """
        x = A cos(at)
        y = B sin(bt+delta)
        の式を用いて座標を更新する
        :param A: 振幅
        :param a: 角周波数
        :param b: 角周波数
        :param delta: 位相差
        :param t:
        :return:
        """
        self.x = A * math.cos(a * t) + self.x
        self.y = B * math.sin(b * t + delta) + self.y

        for shot_position in self.shot_positions:
            shot_position.x = A * math.cos(a * t) + shot_position.x
            shot_position.y = B * math.sin(b * t + delta) + shot_position.y

        self.view_start_x = self.x - self.width / 2
        self.view_start_y = self.y - self.height / 2


class ShotPosition():

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.bullets = []
        self.bullet_pool = bullet_pool.EnemyBulletPool(200)

    def update(self):
        print("bullets", len(self.bullets))
        for b in self.bullets:
            b.update()
            if not b.is_active:
                self.bullets.remove(b)

    def draw(self):
        for b in self.bullets:
            b.draw()

    def pattern1(self, angle, speed):
        """
        angle度の方向に一発発射する
        :param angle: 角度
        :return:
        """
        b = self.bullet_pool.get_bullet(3, self.x, self.y, math.cos(math.radians(angle)), math.sin(math.radians(angle)), speed, 0)
        if b:
            self.bullets.append(b)

    def pattern2(self, speed):
        """
        自機狙いを一発発射する
        :param speed: 弾のスピード
        :return:
        """
        player_x, player_y = player.Player.getPosition()
        angle_to_player = math.atan2(player_y - self.y, player_x - self.x)
        b = self.bullet_pool.get_bullet(3, self.x, self.y, math.cos(angle_to_player),
                                        math.sin(angle_to_player),speed, 0)
        if b:
            self.bullets.append(b)

    def pattern3(self, way, angle, speed):
        """
        自機狙いwayをangle度ずつ発射する
        :param way: way数
        :param angle: 弾の間の角度
        :param speed: 弾のスピード
        :return:
        """
        player_x, player_y = player.Player.getPosition()
        angle_to_player = math.atan2(player_y - self.y, player_x - self.x)
        degree_angle_to_player = math.degrees(angle_to_player)
        _angle = degree_angle_to_player - way * angle / 2 + angle / 2
        for i in range(way):
            b = self.bullet_pool.get_bullet(3, self.x, self.y, math.cos(math.radians(_angle)),
                                            math.sin(math.radians(_angle)), speed, 0)
            if b:
                self.bullets.append(b)
            _angle += angle

    def pattern4(self, way, angle, speed):
        """
        angle度間隔が開いたway弾をランダムな角度で発射する
        :param way:
        :param angle:
        :return:
        """
        _angle = random.uniform(0, 360)
        for i in range(way):
            b = self.bullet_pool.get_bullet(3, self.x, self.y, math.cos(math.radians(_angle)),
                                            math.sin(math.radians(_angle)), speed, 0)
            if b:
                self.bullets.append(b)
            _angle += angle
