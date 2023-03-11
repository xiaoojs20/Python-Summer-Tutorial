import os
import json
import random
import pygame
import time
from init import *
from draw import *
from move import *
from event import *


def main():
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
        if not init_example.is_pause and not init_example.is_gameover:
            init_example.this_time = pygame.time.get_ticks()
            if init_example.last_time < init_example.this_time - 500:
                init_example.last_time = init_example.this_time
                draw_example.ball_generation()  # 发出新黄豆 # 20%的几率产生红色
            draw_example.drow_ball()  # 绘制多个小球
            move_example.ball_move()  # 小球移动, 害羞黄豆移动
            event_example.check_crash()  # 检测碰撞

        # 监测鼠标和键盘的状态
        for event_example.event in pygame.event.get():
            # 鼠标响应
            mouse_pos = pygame.mouse.get_pos()
            if event_example.event.type == pygame.QUIT:
                init_example.b_quit = True
                break
            if event_example.event.type == pygame.MOUSEBUTTONDOWN and not init_example.is_pause:
                if init_example.bird_rect.collidepoint(mouse_pos):
                    init_example.b_mouse_press = True
            if event_example.event.type == pygame.MOUSEBUTTONUP and not init_example.is_pause:
                init_example.b_mouse_press = False
            if event_example.event.type == pygame.MOUSEMOTION and not init_example.is_pause:
                if init_example.b_mouse_press:
                    event_example.mouse_move()
                pass
            # 键盘响应
            init_example.is_going = False
            if event_example.event.type == pygame.KEYDOWN:
                if not init_example.is_pause:
                    # change_bg()# 按任意键背景变色
                    event_example.key_move()  # 键盘上下左右移动
                # 退出游戏
                if event_example.event.key == pygame.K_RETURN:
                    init_example.b_quit = True
                    break
                if event_example.event.key == pygame.K_SPACE and not init_example.is_gameover:
                    if not init_example.is_pause:
                        init_example.is_pause = True
                    else:
                        init_example.is_pause = False
        if init_example.is_going:
            init_example.bird_rect = init_example.bird_rect.move(init_example.step)
        if init_example.is_gameover:
            event_example.gameover()
        if init_example.b_quit:
            break
        # 退出游戏
    pygame.quit()


if __name__ == '__main__':
    main()


