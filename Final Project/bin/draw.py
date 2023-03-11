import random
import pygame
import time
from init import *


# 封装函数三:游戏正式开始

class draw():
    def game_scores(self):
        str_tip = 'score:%s' % init_example.scores
        color_font = (255, 255, 255)
        font = pygame.font.SysFont("DroidSans.ttf", 40)
        self.bmp_gaming = font.render(str_tip, -1, color_font)

    def bird_in_screen(self):
        if init_example.bird_rect.right >= init_example.width:
            init_example.step[0] = -1.0
        if init_example.bird_rect.left <= 0:
            init_example.step[0] = 1.0
        if init_example.bird_rect.bottom >= init_example.height:
            init_example.step[1] = -1.0
        if init_example.bird_rect.top <= 0:
            init_example.step[1] = 1.0

    def ball_generation(self):
        # 发出新黄豆
        attack_body = pygame.image.load('../resource/pic/blue_bird.png')
        attack_rect = init_example.bird_rect.copy()
        attack = {"body": attack_body, "rect": attack_rect}
        init_example.attack_list.append(attack)

        # 20%的几率产生红色
        rand_val = random.randint(0, 10)
        is_red = rand_val <= 3
        if is_red:
            ball_body = pygame.image.load('../resource/pic/egg.png')
        else:
            ball_body = pygame.image.load('../resource/pic/pig.png')

        ball_rect = ball_body.get_rect()
        ball_rect.right = init_example.width
        ball_rect.top = random.randint(0, init_example.height - ball_rect.height)
        ball = {"body": ball_body, "rect": ball_rect, "red": is_red, "num": 0}
        init_example.ball_list.append(ball)

    def drow_ball(self):
        init_example.screen.fill((129, 216, 209))
        init_example.screen.blit(init_example.background, (0, 0))
        for ball in init_example.ball_list:
            init_example.screen.blit(ball['body'], ball['rect'])
        # 绘制发射害羞黄豆
        for attack in init_example.attack_list:
            init_example.screen.blit(attack['body'], attack['rect'])
        init_example.screen.blit(init_example.bird, init_example.bird_rect)
        init_example.screen.blit(self.bmp_gaming, (30, 20))
        pygame.display.flip()


draw_example = draw()


def draw_func():
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
        draw_example.game_scores()  # 得分文字
        draw_example.bird_in_screen()  # 让小鸟运行,自动修改小鸟运动轨迹,全身在屏幕范围内
        # 不暂停的情况下

        init_example.this_time = pygame.time.get_ticks()
        if init_example.last_time < init_example.this_time - 500:
            init_example.last_time = init_example.this_time
            draw_example.ball_generation()  # 发出新黄豆 # 20%的几率产生红色
        draw_example.drow_ball()  # 绘制多个小球

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()


if __name__ == "__main__":
    draw_func()
