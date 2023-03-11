import os
import json
import random
import pygame
import time
from init import *
from draw import *
from move import *


class event_class():

    def change_bg(self):
        init_example.background_color_idx += 1
        init_example.screen.fill(init_example.background_color_list[init_example.background_color_idx])
        pygame.display.flip()
        if init_example.background_color_idx >= len(init_example.background_color_list) - 1:
            init_example.background_color_idx = 0
        init_example.screen.fill(init_example.background_color_list[init_example.background_color_idx])
        init_example.screen.blit(init_example.bird, init_example.bird_rect)
        pygame.display.flip()

    def check_crash(self):
        for ball in init_example.ball_list:
            init_example.ball_rect = ball['rect']
            if init_example.bird_rect.colliderect(init_example.ball_rect) and not ball['red']:  # 吃到白球
                init_example.b_collide = True
                init_example.is_pause = True
                init_example.is_gameover = True
                sound = pygame.mixer.Sound("../resource/sound/bomb.wav")
                sound.play()
            if init_example.bird_rect.colliderect(init_example.ball_rect) and ball['red']:  # 吃到红球
                init_example.b_collide = True
                init_example.scores += 10
                sound = pygame.mixer.Sound("../resource/sound/succeed.wav")
                sound.play()
                init_example.ball_list.remove(ball)

        for ball in init_example.ball_list:
            for attack in init_example.attack_list:
                attack_rect = attack['rect']
                if attack_rect.colliderect(ball['rect']) and not ball['red']:  # 攻击到白球
                    init_example.b_collide = True
                    init_example.scores += 1
                    ball['num'] += 1
                    if not ball['red'] and ball['num'] == 3:
                        ball['body'] = pygame.image.load('../resource/pic/egg.png')
                        ball['red'] = True
                    init_example.attack_list.remove(attack)

    def mouse_move(self):
        x = pygame.mouse.get_pos()
        init_example.bird_rect.left = x[0] - init_example.bird_rect.width / 2
        init_example.bird_rect.top = x[1] - init_example.bird_rect.height / 2
        # screen.fill(background_color_list[background_color_idx])
        init_example.screen.blit(init_example.bird, init_example.bird_rect)

    def key_move(self):
        self.press_dict = {pygame.K_UP: (0, -2), pygame.K_DOWN: (0, 2),
                           pygame.K_LEFT: (-3, 0), pygame.K_RIGHT: (2, 0)}
        if self.event.key in self.press_dict:
            press = self.press_dict[self.event.key]
            init_example.step[0] = press[0]
            init_example.step[1] = press[1]
            init_example.bird_rect.right += init_example.step[0]
            init_example.bird_rect.top += init_example.step[1]
            init_example.is_going = True

    def gameover(self):
        self.score_list = []
        if not os.path.exists("../resource/json/score.json"):
            self.score_list = [0]
            with open("../resource/json/score.json", 'w') as fp:
                json.dump(self.score_list, fp)
        else:
            with open("../resource/json/score.json") as fp:
                self.score_list = json.load(fp)
            self.score_list.append(init_example.scores)
            with open("../resource/json/score.json", 'w') as fp:
                json.dump(self.score_list, fp)
        best_score = 0
        for i in range(len(self.score_list)):
            self.score_list[i] == int(self.score_list[i])
        self.best_score = max(self.score_list)
        str_tip_1 = f'Final:{init_example.scores}'
        str_tip_2 = f'Best:{self.best_score}'
        color_font = (255, 0, 0)
        font = pygame.font.SysFont("DroidSans.ttf", 100)
        bmp_gameover = font.render(str_tip_1, -1, color_font)
        init_example.screen.blit(bmp_gameover, (270, 200))
        font = pygame.font.SysFont("DroidSans.ttf", 60)
        bmp_gameover = font.render(str_tip_2, -1, color_font)
        init_example.screen.blit(bmp_gameover, (320, 300))
        pygame.display.flip()

    def event_func(self):
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
            for self.event in pygame.event.get():
                # 鼠标响应
                mouse_pos = pygame.mouse.get_pos()
                if self.event.type == pygame.QUIT:
                    init_example.b_quit = True
                    break
                if self.event.type == pygame.MOUSEBUTTONDOWN and not init_example.is_pause:
                    if init_example.bird_rect.collidepoint(mouse_pos):
                        init_example.b_mouse_press = True
                if self.event.type == pygame.MOUSEBUTTONUP and not init_example.is_pause:
                    init_example.b_mouse_press = False
                if self.event.type == pygame.MOUSEMOTION and not init_example.is_pause:
                    if init_example.b_mouse_press:
                        event_example.mouse_move()
                    pass
                # 键盘响应
                init_example.is_going = False
                if self.event.type == pygame.KEYDOWN:
                    if not init_example.is_pause:
                        # change_bg()# 按任意键背景变色
                        event_example.key_move()  # 键盘上下左右移动
                    # 退出游戏
                    if self.event.key == pygame.K_RETURN:
                        init_example.b_quit = True
                        break
                    if self.event.key == pygame.K_SPACE and not init_example.is_gameover:
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


event_example = event_class()

if __name__ == "__main__":
    event_example.event_func()
