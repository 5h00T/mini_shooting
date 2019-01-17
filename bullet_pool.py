import bullet

MAX_BULLET_NUM = 250


class EnemyBulletPool():
    """
    敵弾のオブジェクトプール
    ゲーム起動時にMAX_BULLET_NUM個の弾を生成し使いまわす
    """
    bullet_pool = [bullet.EnemyBullet(2, -1, -11, 0, 0, 0, 0) for i in range(MAX_BULLET_NUM)]
    max_bullet_num = MAX_BULLET_NUM

    def __init__(self):
        pass

    @classmethod
    def get_bullet(cls, radius, x, y, movement_x, movement_y, speed, color):
        for i in range(MAX_BULLET_NUM):
            if not cls.bullet_pool[i].is_active:
                cls.bullet_pool[i].is_active = True
                cls.bullet_pool[i].count = 0
                cls.bullet_pool[i].radius = radius
                cls.bullet_pool[i].x = x
                cls.bullet_pool[i].y = y
                cls.bullet_pool[i].movement_x = movement_x
                cls.bullet_pool[i].movement_y = movement_y
                cls.bullet_pool[i].speed = speed
                cls.bullet_pool[i].color = color
                cls.bullet_pool[i].move_functions.clear()

                return cls.bullet_pool[i]

        return None

    @classmethod
    def get_active_bullet_num(cls):
        count = 0
        for i in range(cls.max_bullet_num):
            if not cls.bullet_pool[i].is_active:
                count += 1

        return count

    @classmethod
    def all_reset_bullet(cls):
        for b in cls.bullet_pool:
            b.is_active = False
            b.move_functions.clear()


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
                self.bullet_pool[i].count = 0
                self.bullet_pool[i].x = x
                self.bullet_pool[i].y = y
                self.bullet_pool[i].movement_x = movement_x
                self.bullet_pool[i].movement_y = movement_y
                self.bullet_pool[i].speed = speed
                self.bullet_pool[i].color = color

                return self.bullet_pool[i]

        return None
