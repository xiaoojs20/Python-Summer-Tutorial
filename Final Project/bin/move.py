import os
import json
import random
import pygame
import time
from init import *
from draw import *


class move():

    def ball_move(self):
        # 小球移动
        ball_x_step = -1
        for ball in init_example.ball_list:
            ball["rect"].right += ball_x_step
        # 害羞黄豆移动
        attack_x_step = 3
        for attack in init_example.attack_list:
            attack["rect"].right += attack_x_step


move_example = move()


def move_func():
    init_example.game_init()
    while True:
        init_example.start_screen_init()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    init_example.b_quit1 = True
                    break
        if init_example.b_quit1:
            break
    while True:
        init_example.tick = init_example.tick * 1.000001
        init_example.clock.tick(init_example.tick)
        draw_example.game_scores()  # 得分文字
        draw_example.bird_in_screen()  # 让小鸟运行,自动修改小鸟运动轨迹,全身在屏幕范围内
        # 不暂停的情况下

        init_example.this_time = pygame.time.get_ticks()
        if init_example.last_time < init_example.this_time - 500:
            init_example.last_time = init_example.this_time
            draw_example.ball_generation()  # 发出新黄豆 # 20%的几率产生红色
        draw_example.drow_ball()  # 绘制多个小球
        move_example.ball_move()  # 小球移动, 害羞黄豆移动

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()


if __name__ == "__main__":
    move_func()
