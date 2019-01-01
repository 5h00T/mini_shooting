import bullet


class BulletPool():

    def __init__(self, max_bullet_num):
        self.max_bullet_num = max_bullet_num
        self.bullet_pool = []

        for i in range(max_bullet_num):
            self.bullet_pool.append(bullet.bullet(2, -1, -1, 1, 0, 0))

    def get_bullet(self, radius, x, y, vx, vy, color):
        for i in range(self.max_bullet_num):
            if not self.bullet_pool[i].is_active:
                self.bullet_pool[i].is_active = True
                self.bullet_pool[i].radius = radius
                self.bullet_pool[i].x = x
                self.bullet_pool[i].y = y
                self.bullet_pool[i].vx = vx
                self.bullet_pool[i].vy = vy
                self.bullet_pool[i].color = color

                return self.bullet_pool[i]

        return None
