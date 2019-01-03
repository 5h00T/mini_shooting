import bullet


class EnemyBulletPool():

    def __init__(self, max_bullet_num):
        self.max_bullet_num = max_bullet_num
        self.bullet_pool = []

        for i in range(max_bullet_num):
            self.bullet_pool.append(bullet.EnemyBullet(2, -1, -11, 0, 0, 0, 0))

    def get_bullet(self, radius, x, y, movement_x, movement_y, speed, color):
        for i in range(self.max_bullet_num):
            if not self.bullet_pool[i].is_active:
                self.bullet_pool[i].is_active = True
                self.bullet_pool[i].radius = radius
                self.bullet_pool[i].x = x
                self.bullet_pool[i].y = y
                self.bullet_pool[i].movement_x = movement_x
                self.bullet_pool[i].movement_y = movement_y
                self.bullet_pool[i].speed = speed
                self.bullet_pool[i].color = color

                return self.bullet_pool[i]

        return None

class PlayerBulletPool():

    def __init__(self, max_bullet_num):
        self.max_bullet_num = max_bullet_num
        self.bullet_pool = []

        for i in range(max_bullet_num):
            self.bullet_pool.append(bullet.PlayerBullet(2, -1, -11, 0, 0, 0, 0))

    def get_bullet(self, radius, x, y, movement_x, movement_y, speed, color):
        for i in range(self.max_bullet_num):
            if not self.bullet_pool[i].is_active:
                self.bullet_pool[i].is_active = True
                self.bullet_pool[i].radius = radius
                self.bullet_pool[i].x = x
                self.bullet_pool[i].y = y
                self.bullet_pool[i].movement_x = movement_x
                self.bullet_pool[i].movement_y = movement_y
                self.bullet_pool[i].speed = speed
                self.bullet_pool[i].color = color

                return self.bullet_pool[i]

        return None