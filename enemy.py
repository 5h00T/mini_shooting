import bullet_pool
import player
import pyxel
import math

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
        self.bullets = []
        self.bullet_pool = bullet_pool.EnemyBulletPool(200)

    def update(self):
        self.count += 1

        for b in self.bullets:
            b.update()
            if not b.is_active:
                self.bullets.remove(b)

    def draw(self):
        pyxel.rect(self.view_start_x, self.view_start_y, self.view_start_x + self.width,
                   self.view_start_y + self.height, self.color)
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
