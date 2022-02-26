import pygame
from pygame.locals import *
import sys

# 使用pygame之前必须初始化
pygame.init()
# 设置用于显示的窗口，单位为像素
screen = pygame.display.set_mode((630, 630))
# 设置标题
pygame.display.set_caption("MyGame")

# 加载图片
bg_img = pygame.image.load("../../image/choose_1_or_2.jpg").convert()  # 背景图片
bg_img = pygame.transform.scale(bg_img, (600, 600))
hero_img = pygame.image.load("../../image/choose_tank.jpg").convert_alpha()  # 坦克图片
hero_img = pygame.transform.scale(hero_img, (50, 50))

# 渲染图片
screen.blit(bg_img, (0, 0))  # 绘制背景
screen.blit(hero_img, (120, 340))  # 绘制选择 1
# screen.blit(hero_img, (120, 380))  # 绘制选择 2

while True:
    choose = 1
    for event in pygame.event.get():  # 循环获取事件
        if event.type == QUIT:  # 若检测到事件类型为退出，则退出系统
            pygame.quit()
            sys.exit()

        # 选择单双人
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_c and pygame.KMOD_CTRL:
                pygame.quit()
                sys.exit()
            if event.key == pygame.K_DOWN:
                choose = 2
                screen.fill((0, 0, 0))
                screen.blit(bg_img, (0, 0))
                screen.blit(hero_img, (120, 380))  # 绘制选择 2
            if event.key == pygame.K_UP:
                choose = 1
                screen.fill((0, 0, 0))
                screen.blit(bg_img, (0, 0))
                screen.blit(hero_img, (120, 340))  # 绘制选择 1
            if event.key == pygame.K_RETURN:
                print(choose)

    pygame.display.update()  # 刷新屏幕内容