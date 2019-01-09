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
        self.bits = []
        self.standard_position = self.x

    def update(self):
        self.count += 1

        for shot_position in self.shot_positions:
            shot_position.update()

        for bit in self.bits:
            bit.update()
            if not bit.is_active:
                if len(bit.shot_position.bullets) == 0:
                    self.bits.remove(bit)

    def draw(self):
        pyxel.rect(self.view_start_x, self.view_start_y, self.view_start_x + self.width,
                   self.view_start_y + self.height, self.color)

        for bit in self.bits:
            bit.draw()

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

        for bit in self.bits:
            if bit.is_active:
                bit.x = A * math.cos(a * t) + bit.x
                bit.y = B * math.sin(b * t + delta) + bit.y
                bit.view_start_x = A * math.cos(a * t) + bit.view_start_x
                bit.view_start_y = B * math.sin(b * t + delta) + bit.view_start_y
                bit.shot_position.x = A * math.cos(a * t) + bit.shot_position.x
                bit.shot_position.y = B * math.sin(b * t + delta) + bit.shot_position.y

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
        angle度間隔が開いた自機狙いway弾を発射する
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

    def pattern5(self, way, angle, num, speed, delta_speed):
        """
        angle度間隔が開いた自機狙いway弾をnum発delta_speedずつ速度を増やしながら発射する
        :param way: way数
        :param angle: 弾の間の角度
        :param num: 連数
        :param speed: 弾のスピード
        :param delta_speed: 連毎に増やす速度
        :return:
        """

        player_x, player_y = player.Player.getPosition()
        angle_to_player = math.atan2(player_y - self.y, player_x - self.x)
        degree_angle_to_player = math.degrees(angle_to_player)
        _angle = degree_angle_to_player - way * angle / 2 + angle / 2
        for i in range(way):
            _speed = speed
            for j in range(num):
                b = self.bullet_pool.get_bullet(3, self.x, self.y, math.cos(math.radians(_angle)),
                                                math.sin(math.radians(_angle)), _speed, 0)
                if b:
                    self.bullets.append(b)

                _speed += delta_speed
            _angle += angle

    def pattern6(self, angle1, angle2, speed1, speed2, t1, t2):
        """
        angle度の方向に一発発射する
        :param angle1: 角度
        :return:
        """
        b = self.bullet_pool.get_bullet(3, self.x, self.y, math.cos(math.radians(angle1)), math.sin(math.radians(angle1)), speed1, 0)
        if b:
            self.bullets.append(b)
            b.func = b.pattern1(t1, t2, angle2, speed2)

    def pattern7(self, way, angle, speed):
        """
        全方位num弾を最初の弾がangle度に発射されるように発射する
        :param way:
        :param angle:
        :param speed:
        :return:
        """

        _angle = angle
        for i in range(way):
            b = self.bullet_pool.get_bullet(3, self.x, self.y, math.cos(math.radians(_angle)),
                                            math.sin(math.radians(_angle)), speed, 0)
            if b:
                self.bullets.append(b)
            _angle += 360 / way

    def pattern8(self, way, angle1, angle2, speed1, speed2, t1, t2):
        """
        全方位num弾を最初の弾がangle度に発射されるように発射する
        :param way:
        :param angle1:
        :param speed1:
        :return:
        """

        _angle = angle1
        for i in range(way):
            b = self.bullet_pool.get_bullet(3, self.x, self.y, math.cos(math.radians(_angle)),
                                            math.sin(math.radians(_angle)), speed1, 0)
            if b:
                self.bullets.append(b)
                b.set_move_function(b.pattern1(t1, t2, angle2 + math.degrees(math.atan2(b.movement_y, b.movement_x)), speed2))

            _angle += 360 / way

    def pattern9(self, way, angle, speed, a, min_speed, max_speed):
        """
        angle度間隔が開いた自機狙いway弾を発射する
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
                b.set_move_function(b.pattern2(a, min_speed, max_speed))
            _angle += angle

    def pattern10(self, way, angle, target_angle, speed):
        """
        angle度間隔が開いたway弾を中心がtarget_angleの方向に発射する
        :param way: way数
        :param angle: 弾の間の角度
        :param speed: 弾のスピード
        :return:
        """
        _angle = target_angle - way * angle / 2 + angle / 2
        for i in range(way):
            b = self.bullet_pool.get_bullet(3, self.x, self.y, math.cos(math.radians(_angle)),
                                            math.sin(math.radians(_angle)), speed, 0)
            if b:
                self.bullets.append(b)
            _angle += angle

class Bit():

    def __init__(self, x, y, width, height, movement_x, movement_y, hp, color, const_parameter=None):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.movement_x = movement_x
        self.movement_y = movement_y
        self.hp = hp
        self.color = color
        self.count = 0
        self.const_parameter = const_parameter
        self.view_start_x = self.x - self.width / 2
        self.view_start_y = self.y - self.height / 2
        self.shot_position = ShotPosition(self.x, self.y)
        self.is_active = True

    def update(self):
        self.count += 1
        self.shot_position.update()

        if self.x < -10 or self.x > pyxel.width + 10 or self.y < 0 - 10 or self.y > pyxel.height + 10:
            self.is_active = False

    def draw(self):
        if self.is_active:
            pyxel.rect(self.view_start_x, self.view_start_y, self.view_start_x + self.width,
                   self.view_start_y + self.height, self.color)

        self.shot_position.draw()

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
        self.shot_position.x = self.x = A * math.cos(a * t) + self.x
        self.shot_position.y = self.y = B * math.sin(b * t + delta) + self.y

        self.view_start_x = self.x - self.width / 2
        self.view_start_y = self.y - self.height / 2

    def move_pattern2(self, speed):
        """
        movementの向きに従って移動
        :param speed:
        :return:
        """
        self.shot_position.x = self.x = self.movement_x * speed + self.x
        self.shot_position.y = self.y = self.movement_y * speed + self.y

        self.view_start_x = self.x - self.width / 2
        self.view_start_y = self.y - self.height / 2
