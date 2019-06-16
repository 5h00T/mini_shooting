import bullet_pool
import player
import pyxel
import math
import random


class Enemy():
    def __init__(self, x, y, width, height, hp, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.hp = hp
        self.color = color
        self.count = 0
        self.view_start_x = self.x - self.width / 2
        self.view_start_y = self.y - self.height / 2
        self.shot_positions = []  # 弾源を格納するリスト
        self.bits = []
        self.move_functions = []
        # self.shot_functions = {}
        self.shot_functions = []

    def update(self):
        self.count += 1

        for move_function in self.move_functions:
            if move_function is not None:
                try:
                    next(move_function)
                except StopIteration:
                    self.move_functions.remove(move_function)

        for shot_function in self.shot_functions:
            if shot_function is not None:
                try:
                    next(shot_function)
                except StopIteration:
                    self.shot_functions.remove(shot_function)

        for shot_position in self.shot_positions:
            shot_position.update()

        for bit in self.bits:
            bit.update()
            if not bit.is_active:
                if len(bit.shot_position.bullets) == 0:
                    self.bits.remove(bit)

    def draw(self):
        pyxel.rect(self.view_start_x, self.view_start_y, self.width, self.height, self.color)

        for bit in self.bits:
            bit.draw()

        for shot_position in self.shot_positions:
            shot_position.draw()

    def set_move_function(self, move_function):
        self.move_functions.append(move_function)

    def set_shot_function(self, shot_function):
        self.shot_functions.append(shot_function)

    def move_pattern1(self, A, B, a, b, delta, speed, start_count=0, end_count=math.inf):
        """
        x = A cos(at)
        y = B sin(bt+delta)
        の式を用いて座標を更新する
        :param A: 振幅
        :param a: 角周波数
        :param b: 角周波数
        :param delta: 位相差
        :param t: 時間
        :return:
        """
        count = 0

        while True:
            if count >= start_count:
                self.x = A * math.cos(a * count * speed) + self.x
                self.y = B * math.sin(b * count * speed + delta) + self.y

                for shot_position in self.shot_positions:
                    shot_position.x = A * math.cos(a * count * speed) + shot_position.x
                    shot_position.y = B * math.sin(b * count * speed + delta) + shot_position.y

                for bit in self.bits:
                    if bit.is_active:
                        bit.x = A * math.cos(a * count * speed) + bit.x
                        bit.y = B * math.sin(b * count * speed + delta) + bit.y
                        bit.view_start_x = bit.x - bit.width / 2
                        bit.view_start_y = bit.y - bit.height / 2
                        bit.shot_position.x = A * math.cos(a * count * speed) + bit.shot_position.x
                        bit.shot_position.y = B * math.sin(b * count * speed + delta) + bit.shot_position.y

                self.view_start_x = self.x - self.width / 2
                self.view_start_y = self.y - self.height / 2

            count += 1

            if count >= end_count:
                break

            yield

    def move_pattern2(self, start_position_x, start_position_y, target_position_x, target_position_y, start_count,
                      end_count):
        """
        終点の方向に直線移動
        :param start_position_x: 開始位置
        :param start_position_y: 開始位置
        :param target_position_x: 終点
        :param target_position_y: 終点
        :param start_count: 移動開始カウント
        :param end_count: 移動終了カウント
        """

        count = 0
        while True:
            if start_count <= count:
                self.x = (target_position_x - start_position_x) / end_count + self.x
                self.y = (target_position_y - start_position_y) / end_count + self.y

                for shot_position in self.shot_positions:
                    shot_position.x = (target_position_x - start_position_x) / end_count + shot_position.x
                    shot_position.y = (target_position_y - start_position_y) / end_count + shot_position.y

                for bit in self.bits:
                    if bit.is_active:
                        bit.x = (target_position_x - start_position_x) / end_count + bit.x
                        bit.y = (target_position_y - start_position_y) / end_count + bit.y
                        bit.view_start_x = bit.x - bit.width / 2
                        bit.view_start_y = bit.y - bit.height / 2
                        bit.shot_position.x = (target_position_x - start_position_x) / end_count + bit.shot_position.x
                        bit.shot_position.y = (target_position_y - start_position_y) / end_count + bit.shot_position.y

                self.view_start_x = self.x - self.width / 2
                self.view_start_y = self.y - self.height / 2

            count += 1

            if count >= end_count:
                break

            yield


class ShotPosition():
    """
    Enemyが共通して使う弾幕は関数にして呼び出す
    各パターンの引数について
    interval_count: 何フレームごとに発射するか
    start_count: 開始カウント
    end_count: 終了カウント
    angle_function: 発射ごとに角度を変更したい場合増加させる角度を返す関数を指定する
    """

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.bullets = []
        self.bullet_pool = bullet_pool.EnemyBulletPool

    def update(self):
        for b in self.bullets[:]:
            b.update()
            if not b.is_active:
                self.bullets.remove(b)

    def draw(self):
        for b in self.bullets:
            b.draw()

    def pattern1(self, angle, speed, interval_count, start_count=0, end_count=math.inf, angle_function=None):
        """
        angle度の方向に一発発射する
        :param angle: 角度
        :param speed: 弾の速さ
        :param interval_count: 何フレームごとに発射するか
        :param start_count: 開始カウント
        :param end_count: 終了カウント
        :param angle_function: 発射ごとに角度を変更したい場合増加させる角度を返す関数を指定する
        """
        count = 0
        while count < end_count:
            if count >= start_count:
                if count % interval_count == 0:
                    if angle_function is not None:
                        _angle = angle + angle_function(count)
                    else:
                        _angle = angle

                    b = self.bullet_pool.get_bullet(3, self.x, self.y, math.cos(math.radians(_angle)),
                                                    math.sin(math.radians(_angle)), speed, 0)
                    if b:
                        self.bullets.append(b)

            count += 1
            yield

    def pattern2(self, speed, interval_count, start_count=0, end_count=math.inf):
        """
        自機狙いを一発発射する
        :param speed: 弾のスピード
        """
        count = 0
        while count < end_count:
            if count >= start_count:
                if count % interval_count == 0:
                    player_x, player_y = player.Player.getPosition()
                    angle_to_player = math.atan2(player_y - self.y, player_x - self.x)
                    b = self.bullet_pool.get_bullet(3, self.x, self.y, math.cos(angle_to_player),
                                                    math.sin(angle_to_player), speed, 0)
                    if b:
                        self.bullets.append(b)
            count += 1
            yield

    def pattern3(self, way, angle, speed, interval_count, start_count=0, end_count=math.inf):
        """
        angle度間隔が開いた自機狙いway弾を発射する
        :param way: way数
        :param angle: 弾の間の角度
        :param speed: 弾のスピード
        :return:
        """
        count = 0
        while count < end_count:
            if count >= start_count:
                if count % interval_count == 0:
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
            count += 1
            yield

    def pattern4(self, way, angle, speed, interval_count, start_count=0, end_count=math.inf):
        """
        angle度間隔が開いたway弾をランダムな角度で発射する
        :param way: way数
        :param angle: 弾の間の角度
        :return:
        """
        count = 0
        while count < end_count:
            if count >= start_count:
                if count % interval_count == 0:
                    _angle = random.uniform(0, 360)
                    for i in range(way):
                        b = self.bullet_pool.get_bullet(3, self.x, self.y, math.cos(math.radians(_angle)),
                                                        math.sin(math.radians(_angle)), speed, 0)
                        if b:
                            self.bullets.append(b)
                        _angle += angle
            count += 1
            yield

    def pattern5(self, way, angle, num, speed, delta_speed, interval_count, start_count=0, end_count=math.inf):
        """
        angle度間隔が開いた自機狙いway弾をnum発delta_speedずつ速度を増やしながら発射する
        :param way: way数
        :param angle: 弾の間の角度
        :param num: 連数
        :param speed: 弾のスピード
        :param delta_speed: 連毎に増やす速度
        :return:
        """
        count = 0
        while count < end_count:
            if count >= start_count:
                if (start_count + count) % interval_count == 0:
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
            count += 1
            yield

    def pattern6(self, angle1, angle2, speed1, speed2, move_time, stop_time, interval_count, start_count=0, end_count=math.inf):
        """
        angle度の方向に一発発射
        発射後move_timeカウント後stop_timeカウント停止しangle2角度変えながらspeed2で移動する
        :param angle1: 発射時の角度
        :param angle2: 停止後に加える角度
        :param speed1: 発射時の速度
        :param speed2: 再移動時の速度
        :param move_time: 最初に停止するまでのカウント
        :param stop_time: 停止時間
        """
        count = 0
        while count < end_count:
            if count >= start_count:
                if (start_count + count) % interval_count == 0:
                    b = self.bullet_pool.get_bullet(3, self.x, self.y, math.cos(math.radians(angle1)),
                                                    math.sin(math.radians(angle1)), speed1, 0)
                    if b:
                        b.set_move_function(b.pattern1(move_time, stop_time, angle2, speed2))
            count += 1
            yield

    def pattern7(self, way, angle, speed, interval_count, start_count=0, end_count=math.inf):
        """
        全方位num弾を最初の弾がangle度に発射されるように発射する
        :param way: way数
        :param angle: 最初の弾の方向
        :param speed: 弾の速さ
        :return:
        """
        count = 0
        while count < end_count:
            if count >= start_count:
                if (start_count + count) % interval_count == 0:
                    _angle = angle
                    for i in range(way):
                        b = self.bullet_pool.get_bullet(3, self.x, self.y, math.cos(math.radians(_angle)),
                                                        math.sin(math.radians(_angle)), speed, 0)
                        if b:
                            self.bullets.append(b)
                        _angle += 360 / way
            count += 1
            yield

    def pattern8(self, way, angle1, angle2, speed1, speed2, move_time, stop_time, interval_count, start_count=0, end_count=math.inf):
        """
        全方位num弾を最初の弾がangle度に発射されるように発射する
        発射後move_timeカウント後stop_timeカウント停止しangle2角度変えてspeed2で移動する
        :param way: way数
        :param angle1: 発射時の角度
        :param angle2: 停止後に加える角度
        :param speed1: 発射時の速度
        :param speed2: 再移動時の速度
        :param move_time: 最初に停止するまでのカウント
        :param stop_time: 停止時間
        """
        count = 0
        while count < end_count:
            if count >= start_count:
                if (start_count + count) % interval_count == 0:
                    _angle = angle1
                    for i in range(way):
                        b = self.bullet_pool.get_bullet(3, self.x, self.y, math.cos(math.radians(_angle)),
                                                        math.sin(math.radians(_angle)), speed1, 0)
                        if b:
                            self.bullets.append(b)
                            b.set_move_function(
                                b.pattern1(move_time, stop_time, angle2 + math.degrees(math.atan2(b.movement_y, b.movement_x)),
                                           speed2))

                        _angle += 360 / way
            count += 1
            yield

    def pattern9(self, way, angle, speed, a, min_speed, max_speed, change_start_count, change_end_count, interval_count,
                 start_count=0, end_count=math.inf):
        """
        angle度間隔が開いた自機狙いway弾を発射する
        発射後change_start_count後に弾のスピードを毎フレームaずつ加速させる
        change_end_count後に加速を終了
        :param way: way数
        :param angle: 弾の間の角度
        :param speed: 弾の速さ
        :param a: 加速度
        :param min_speed: スピードの下限
        :param max_speed: スピードの上限
        :param change_start_count: 速度を変化の開始カウント
        :param change_end_count: 速度を変化の停止カウント
        """
        count = 0
        while count < end_count:
            if count >= start_count:
                if (start_count + count) % interval_count == 0:
                    player_x, player_y = player.Player.getPosition()
                    angle_to_player = math.atan2(player_y - self.y, player_x - self.x)
                    degree_angle_to_player = math.degrees(angle_to_player)
                    _angle = degree_angle_to_player - way * angle / 2 + angle / 2
                    for i in range(way):
                        b = self.bullet_pool.get_bullet(3, self.x, self.y, math.cos(math.radians(_angle)),
                                                        math.sin(math.radians(_angle)), speed, 0)
                        if b:
                            self.bullets.append(b)
                            b.set_move_function(
                                b.pattern2(a, min_speed, max_speed, change_start_count, change_end_count))
                        _angle += angle
            count += 1
            yield

    def pattern10(self, way, angle, target_angle, speed, interval_count, start_count=0, end_count=math.inf):
        """
        angle度間隔が開いたway弾を中心がtarget_angleの方向に発射する
        :param way: way数
        :param angle: 弾の間の角度
        :param target_angle: 発射方向
        :param speed: 弾の速さ
        """
        count = 0
        while count < end_count:
            if count >= start_count:
                if (start_count + count) % interval_count == 0:
                    _angle = target_angle - way * angle / 2 + angle / 2
                    for i in range(way):
                        b = self.bullet_pool.get_bullet(3, self.x, self.y, math.cos(math.radians(_angle)),
                                                        math.sin(math.radians(_angle)), speed, 0)
                        if b:
                            self.bullets.append(b)
                        _angle += angle
            count += 1
            yield

    def pattern11(self, way, angle, target_angle, num, speed, delta_speed, interval_count, start_count=0,
                  end_count=math.inf):
        """
        angle度間隔が開いたway弾をnum発delta_speedずつ速度を増やしながらtarget_angle方向に向けて発射する
        :param way: way数
        :param angle: 弾の間の角度
        :param target_angle: 発射方向
        :param num: 連数
        :param speed: 弾の速さ
        :param delta_speed: 連毎に増やす速度
        :return:
        """
        count = 0
        while count < end_count:
            if count >= start_count:
                if (start_count + count) % interval_count == 0:
                    _angle = target_angle - way * angle / 2 + angle / 2
                    for i in range(way):
                        _speed = speed
                        for j in range(num):
                            b = self.bullet_pool.get_bullet(3, self.x, self.y, math.cos(math.radians(_angle)),
                                                            math.sin(math.radians(_angle)), _speed, 0)
                            if b:
                                self.bullets.append(b)

                            _speed += delta_speed
                        _angle += angle
            count += 1
            yield

    def pattern12(self, way, angle, target_angle, shot_position_x, shot_position_y, speed, interval_count,
                  start_count=0, end_count=math.inf):
        """
        angle度間隔が開いたway弾を中心がtarget_angleの方向に発射する
        発射後move_timeカウント後stop_timeカウント停止しangle2角度変えながらspeed2で移動する
        :param way: way数
        :param angle: 弾の間の角度
        :param target_angle: 発射方向
        :param shot_position_x: 発射位置
        :param shot_position_y:  発射位置
        :param speed: 弾の速さ
        :return:
        """
        count = 0
        while count < end_count:
            if count >= start_count:
                if (start_count + count) % interval_count == 0:
                    _angle = target_angle - way * angle / 2 + angle / 2
                    for i in range(way):
                        b = self.bullet_pool.get_bullet(3, shot_position_x, shot_position_y,
                                                        math.cos(math.radians(_angle)),
                                                        math.sin(math.radians(_angle)), speed, 0)
                        if b:
                            self.bullets.append(b)
                        _angle += angle
            count += 1
            yield

    def pattern13(self, way, angle1, angle2, change_start_count, speed, interval_count, start_count=0,
                  end_count=math.inf):
        """
        全方位num弾を最初の弾がangle1度に発射されるように発射する
        :param way: way数
        :param angle1: 発射時の角度
        :param angle2: 変更する角度
        :param change_start_count: 角度を変更する
        :param speed: 弾の速さ
        """
        count = 0
        while count < end_count:
            if count >= start_count:
                if (start_count + count) % interval_count == 0:
                    _angle = angle1
                    for i in range(way):
                        b = self.bullet_pool.get_bullet(3, self.x, self.y, math.cos(math.radians(_angle)),
                                                        math.sin(math.radians(_angle)), speed, 0)
                        if b:
                            self.bullets.append(b)
                            b.set_move_function(b.pattern3(angle2, change_start_count))

                        _angle += 360 / way
            count += 1
            yield

    def pattern14(self, way, angle1, angle2, speed1, speed2, move_time, stop_time, a, min_speed, max_speed, interval_count,
                  start_count=0, end_count=math.inf, angle_function1=None):
        """
        全方位num弾を最初の弾がangle度に発射されるように発射する
        発射後move_timeカウント後stop_timeカウント停止しangle2角度変えながらspeed2で移動
        また再移動後に弾のスピードを毎フレームaずつ加速させる
        :param way: way数
        :param angle1: 発射時の角度
        :param angle2: 停止後に加える角度
        :param speed1: 発射時の弾の速さ
        :param speed2: 再移動時の弾の速さ
        :param move_time: 最初に停止するまでのカウント
        :param stop_time: 停止時間
        :param a: 加速度
        :param min_speed: スピードの下限
        :param max_speed: スピードの上限
        :return:
        """
        count = 0
        while count < end_count:
            if count >= start_count:
                if (start_count + count) % interval_count == 0:
                    if angle_function1 is not None:
                        _angle = angle1 + angle_function1(count)
                    else:
                        _angle = angle1

                    for i in range(way):
                        b = self.bullet_pool.get_bullet(3, self.x, self.y, math.cos(math.radians(_angle)),
                                                        math.sin(math.radians(_angle)), speed1, 0)
                        if b:
                            self.bullets.append(b)
                            b.set_move_function(
                                b.pattern1(move_time, stop_time, angle2 + math.degrees(math.atan2(b.movement_y, b.movement_x)),
                                           speed2))
                            b.set_move_function(b.pattern2(a, min_speed, max_speed, stop_time, 999))

                        _angle += 360 / way
            count += 1
            yield

    def pattern15(self, sigma, speed, interval_count, start_count=0, end_count=math.inf):
        """
        自機への角度を平均、標準偏差をsigmaの正規分布に従う乱数ずらした弾を一発発射する
        :param sigma: 標準偏差
        :param speed: 弾の速さ
        """
        count = 0
        while count < end_count:
            if count >= start_count:
                if (start_count + count) % interval_count == 0:
                    player_x, player_y = player.Player.getPosition()
                    angle_to_player_degree = math.degrees(math.atan2(player_y - self.y, player_x - self.x))
                    angle = math.radians(random.gauss(angle_to_player_degree, sigma))
                    b = self.bullet_pool.get_bullet(3, self.x, self.y, math.cos(angle),
                                                    math.sin(angle), speed, 0)
                    if b:
                        self.bullets.append(b)
            count += 1
            yield

    def pattern16(self, way, angle, delta_angle, num, speed, delta_speed, interval_count, start_count=0,
                  end_count=math.inf, angle_function=None):
        """
        angle度間隔が開いた自機狙いway弾をdelta_angleずつずらし、num発delta_speedずつ速度を増やしながら発射する
        :param way: way数
        :param angle: 弾の間の角度
        :param delta_angle: 自機狙いをずらす角度
        :param num: 連数
        :param speed: 弾の速さ
        :param delta_speed: 連毎に増やす速度
        """
        count = 0
        while count < end_count:
            if count >= start_count:
                if (start_count + count) % interval_count == 0:
                    player_x, player_y = player.Player.getPosition()
                    angle_to_player = math.atan2(player_y - self.y, player_x - self.x)
                    degree_angle_to_player = math.degrees(angle_to_player) + delta_angle
                    _angle = degree_angle_to_player - way * angle / 2 + angle / 2
                    if angle_function is not None:
                        _angle = _angle + angle_function(count)
                    for i in range(way):
                        _speed = speed
                        for j in range(num):
                            b = self.bullet_pool.get_bullet(3, self.x, self.y, math.cos(math.radians(_angle)),
                                                            math.sin(math.radians(_angle)), _speed, 0)
                            if b:
                                self.bullets.append(b)

                            _speed += delta_speed
                        _angle += angle
            count += 1
            yield

    def pattern17(self, min_angle, max_angle, speed, interval_count, start_count=0, end_count=math.inf):
        """
        min_angleからmax_angle度のランダムな方向に一発発射する
        :param min_angle: 発射する角度の範囲の下限
        :param max_angle: 発射する角度の範囲の上限
        :param speed: 弾の速さ
        """
        count = 0
        while count < end_count:
            if count > start_count:
                if count % interval_count == 0:
                    angle = random.uniform(min_angle, max_angle)

                    b = self.bullet_pool.get_bullet(3, self.x, self.y, math.cos(math.radians(angle)),
                                                    math.sin(math.radians(angle)), speed, 0)
                    if b:
                        self.bullets.append(b)

            count += 1
            yield

    def pattern18(self, start_angle, speed, interval_count, start_count=0, end_count=math.inf, angle_function=None):
        """
        発射角度をangle_functionによって決める
        :param start_angle: 一発目に発射する角度
        :param speed: 弾の速さ
        """
        count = 0
        angle = start_angle
        while count < end_count:
            if count > start_count:
                if count % interval_count == 0:
                    if angle_function is not None:
                        angle += angle_function(count)

                    b = self.bullet_pool.get_bullet(3, self.x, self.y, math.cos(math.radians(angle)),
                                                    math.sin(math.radians(angle)), speed, 0)
                    if b:
                        self.bullets.append(b)

            count += 1
            yield

    def pattern19(self, angle, speed, interval_count, start_count=0, end_count=math.inf, bullet_change_interval=1,
                  bullet_change_start_count=0, bullet_change_end_count=math.inf, angle_function=None,
                  bullet_angle_function=None):
        """
        angle度の方向に一発発射する
        発射された弾はbullet_change_start_count後に角度をbullet_angle_function関数に従って変更する
        :param angle_function: 発射ごとに角度を変更したい場合増加させる角度を返す関数を指定する
        :param bullet_change_end_count:
        :param bullet_angle_function: 発射後の弾の角度を決定する関数
        :param speed: 弾の速さ
        :param bullet_change_interval: 弾の角度を変える頻度
        :param bullet_change_start_count: 弾の角度変更を終了するカウント
        :param angle: 発射時の角度
        :return:
        """
        count = 0
        _angle = angle
        while count < end_count:
            if count >= start_count:
                if count % interval_count == 0:
                    if angle_function is not None:
                        _angle = _angle + angle_function(count)
                    b = self.bullet_pool.get_bullet(3, self.x, self.y, math.cos(math.radians(_angle)),
                                                    math.sin(math.radians(_angle)), speed, 0)
                    if b:
                        self.bullets.append(b)
                        b.set_move_function(
                            b.pattern4(bullet_angle_function if bullet_angle_function else lambda count: 0,
                                       bullet_change_interval, bullet_change_start_count, bullet_change_end_count))

            count += 1
            yield


class Bit(Enemy):

    def __init__(self, x, y, width, height, movement_x, movement_y, hp, color, const_parameter=None):
        super().__init__(x, y, width, height, hp, color)
        self.count = 0
        self.const_parameter = const_parameter
        self.view_start_x = self.x - self.width / 2
        self.view_start_y = self.y - self.height / 2
        self.shot_position = ShotPosition(self.x, self.y)
        self.is_active = True
        self.movement_x = movement_x
        self.movement_y = movement_y
        self.move_functions = []
        self.shot_functions = []
        self.return_shot_functions = []  # 撃ち返し弾のパターンを格納
        self.is_shooted_return_shot = False

    def update(self):
        self.count += 1
        self.shot_position.update()

        if self.hp <= 0 and not self.is_shooted_return_shot:
            self.is_shooted_return_shot = True
            for return_shot_function in self.return_shot_functions:
                if return_shot_function is not None:
                    try:
                        next(return_shot_function)
                    except StopIteration:
                        self.return_shot_functions.remove(return_shot_function)

        if self.is_active:
            for move_function in self.move_functions:
                if move_function is not None:
                    try:
                        next(move_function)
                    except StopIteration:
                        self.move_functions.remove(move_function)

            for shot_function in self.shot_functions:
                if shot_function is not None:
                    try:
                        next(shot_function)
                    except StopIteration:
                        self.shot_functions.remove(shot_function)

        if self.x < -10 or self.x > pyxel.width + 10 or self.y < 0 - 10 or self.y > pyxel.height + 10:
            self.is_active = False

    def draw(self):
        if self.is_active:
            pyxel.rect(self.view_start_x, self.view_start_y,  self.width, self.height, self.color)

    def set_move_function(self, move_function):
        self.move_functions.append(move_function)

    def set_shot_function(self, shot_function):
        self.shot_functions.append(shot_function)

    def set_return_shot(self, shot_function):
        self.return_shot_functions.append(shot_function)

    def move_pattern1(self, A, B, a, b, delta, speed, start_count=0, end_count=math.inf):
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

        count = 0
        while True:
            if count >= start_count:
                self.shot_position.x = self.x = A * math.cos(a * count * speed) + self.x
                self.shot_position.y = self.y = B * math.sin(b * count * speed + delta) + self.y

                self.view_start_x = self.x - self.width / 2
                self.view_start_y = self.y - self.height / 2

            if count >= end_count:
                break

            count += 1
            yield

    def move_pattern2(self, speed, start_count=0, end_count=math.inf):
        """
        movementの向きに従って移動
        :param speed:
        :return:
        """

        count = 0
        while True:
            if count >= start_count:
                self.shot_position.x = self.x = self.movement_x * speed + self.x
                self.shot_position.y = self.y = self.movement_y * speed + self.y

                self.view_start_x = self.x - self.width / 2
                self.view_start_y = self.y - self.height / 2

            if count >= end_count:
                break

            count += 1
            yield

    def move_pattern3(self, start_position_x, start_position_y, target_position_x, target_position_y, start_count,
                      end_count):
        """
        初期位置から終点位置まで直線移動
        :param start_count: 移動開始カウント
        :param end_count: 移動終了カウント
        :param start_position_x: 移動開始地点
        :param start_position_y: 移動開始地点
        :param target_position_x: 移動終了地点
        :param target_position_y: 移動終了地点
        :return:
        """

        count = 0
        while count < end_count:
            self.shot_position.x = self.x = (target_position_x - start_position_x) / end_count + self.x
            self.shot_position.y = self.y = (target_position_y - start_position_y) / end_count + self.y

            self.view_start_x = self.x - self.width / 2
            self.view_start_y = self.y - self.height / 2

            count += 1
            yield
