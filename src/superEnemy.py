import random
import pygame
import enemyTank

# 加入自己和玩家坐标，直接向基地冲
class SuperEnemy(enemyTank.EnemyTank):
    def __init__(self, x=None, kind=None, isred=None):
        enemyTank.EnemyTank.__init__(self, x, kind, isred)
        self.num_jiuzheng = 0


    def move(self, tankGroup, brickGroup, ironGroup, mx=None, my=None, dx=None, dy=None, nandu=None):
        self.rect = self.rect.move(self.speed * self.dir_x, self.speed * self.dir_y)

        # 画坦克的图像
        if self.dir_x == 0 and self.dir_y == -1:
            self.tank_R0 = self.tank.subsurface((0, 0), (48, 48))
            self.tank_R1 = self.tank.subsurface((48, 0), (48, 48))
        elif self.dir_x == 0 and self.dir_y == 1:
            self.tank_R0 = self.tank.subsurface((0, 48), (48, 48))
            self.tank_R1 = self.tank.subsurface((48, 48), (48, 48))
        elif self.dir_x == -1 and self.dir_y == 0:
            self.tank_R0 = self.tank.subsurface((0, 96), (48, 48))
            self.tank_R1 = self.tank.subsurface((48, 96), (48, 48))
        elif self.dir_x == 1 and self.dir_y == 0:
            self.tank_R0 = self.tank.subsurface((0, 144), (48, 48))
            self.tank_R1 = self.tank.subsurface((48, 144), (48, 48))

        # 碰撞地图边缘
        if self.rect.top < 3:
            self.rect = self.rect.move(self.speed * 0, self.speed * 1)
            self.dir_x, self.dir_y = random.choice(([0, 1], [0, -1], [1, 0], [-1, 0]))
        elif self.rect.bottom > 630 - 3:
            self.rect = self.rect.move(self.speed * 0, self.speed * -1)
            self.dir_x, self.dir_y = random.choice(([0, 1], [0, -1], [1, 0], [-1, 0]))
        elif self.rect.left < 3:
            self.rect = self.rect.move(self.speed * 1, self.speed * 0)
            self.dir_x, self.dir_y = random.choice(([0, 1], [0, -1], [1, 0], [-1, 0]))
        elif self.rect.right > 630 - 3:
            self.rect = self.rect.move(self.speed * -1, self.speed * 0)
            self.dir_x, self.dir_y = random.choice(([0, 1], [0, -1], [1, 0], [-1, 0]))

        ##############################   改写部分    ##############################

        # 碰撞坦克和石头
        if pygame.sprite.spritecollide(self, ironGroup, False, None) \
                or pygame.sprite.spritecollide(self, tankGroup, False, None) \
                or pygame.sprite.spritecollide(self, brickGroup, False, None) :
            self.rect = self.rect.move(self.speed * -self.dir_x, self.speed * -self.dir_y)
            self.dir_x, self.dir_y = random.choice(([0, 1], [0, -1], [1, 0], [-1, 0]))


        ##############################   加上策略    ##############################
        '''
        具体策略
        1.尽可能的打掉砖块(难以实现)(因为会鬼畜)
        2.尽可能的向玩家射击
        3.尽可能的向城堡靠近
        4.一旦在一条线上，尽可能的发射子弹
        5.实验发现，不要过分的纠正方向，不然会原地转弯
        '''

        self.num_jiuzheng = self.num_jiuzheng + 1
        if (nandu != None and self.num_jiuzheng == 30):
            # print(self.num_jiuzheng)
            # 纠正方向
            if (random.random() < nandu):
                self.rect = self.rect.move(self.speed * -self.dir_x, self.speed * -self.dir_y)

                # 随机选择靠近玩家还是攻击基地
                if(random.random() < 0.3):
                    # 随机选择下x,y方向来靠近玩家
                    if (random.random() < 0.5):
                        if dx > mx:
                            self.dir_x = 1
                            self.dir_y = 0
                        else:
                            self.dir_x = -1
                            self.dir_y = 0
                    else:
                        if dy > my:
                            self.dir_y = 1
                            self.dir_x = 0
                        else:
                            self.dir_y = -1
                            self.dir_x = 0

                else:
                    # 随机选择下x,y方向来靠近基地
                    if (random.random() < 0.5):
                        if 291 > mx:
                            self.dir_x = 1
                            self.dir_y = 0
                        else:
                            self.dir_x = -1
                            self.dir_y = 0
                    else:
                        if 579 > my:
                            self.dir_y = 1
                            self.dir_x = 0
                        else:
                            self.dir_y = -1
                            self.dir_x = 0

            # print(mx, my, dx, dy, self.dir_x, self.dir_y)
        else:
            # print(self.num_jiuzheng)
            if self.num_jiuzheng > 30:
                self.num_jiuzheng = 0

