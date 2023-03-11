# 使用函数，封装进击小鸟的程序。

import pygame, random, time

# 封装函数一:初始化函数
def screen_init():
    # 屏幕初始化
    global width, height, screen
    width = 800
    height = 600
    screen = pygame.display.set_mode((width, height))
    global background, background_color
    global background_color_list,background_color_idx
    background_color = (255, 0, 0)
    # 取消变色功能吧
    background_color_list = [(128, 128, 128), (0, 0, 255), (255, 0, 0), (0, 255, 0), (255, 255, 255)]
    background_color_idx = 0
    background = pygame.image.load('pic/background.png').convert()
    screen.blit(background, (0, 0))

def word_init():
    pygame.font.init()
    pygame.font.get_fonts()

def music_init():
    pygame.mixer.init()
    pygame.mixer.music.load("sound/cjml.mp3")
    pygame.mixer.music.play(-1, 0)

def clock_init():
    global this_time, last_time
    this_time = pygame.time.get_ticks()
    last_time = pygame.time.get_ticks()
    global tick, clock
    tick = 100
    clock = pygame.time.Clock()

def bird_init():
    global bird,bird_rect
    bird = pygame.image.load('pic/haha.png')
    pygame.transform.scale(bird, (80, 60))
    bird_rect = bird.get_rect()
    bird_rect.right = 100
    bird_rect.top = 100
    screen.blit(bird, bird_rect)
    pygame.display.flip()

def flag_init():
    global b_quit, b_mouse_press,b_collide,b_quit1
    global is_pause,is_gameover,is_going
    b_quit = False
    b_mouse_press = False
    b_collide = False
    is_pause = False
    is_gameover = False
    is_going = False
    b_quit1 = False

# 总体初始化
def game_init():
    pygame.init()
    screen_init()
    # 分数初始化
    global scores
    scores = 0
    global step
    step = [0, 0]

    word_init()    # 文字初始化
    music_init()  # 音乐初始化
    clock_init()  # 时间和频率的初始化
    bird_init()  # 添加小鸟
    flag_init()  # 初始化一些布尔值
    # 球列表
    global ball_list, attack_list
    ball_list = []
    attack_list = []


# 封装函数二:
# 开始界面
def start_screen_init():
    gamename = 'Incoming soya beans'
    color_font = (255, 0, 0)
    font = pygame.font.SysFont("DroidSans.ttf", 80)
    bmp_gamename = font.render(gamename, -1, color_font)
    gamecontinue = 'push Enter to continue'
    color_font = (255, 255, 0)
    font = pygame.font.SysFont("DroidSans.ttf", 40)
    bmp_continue = font.render(gamecontinue, -1, color_font)
    screen.blit(bmp_gamename, (100, 250))
    screen.blit(bmp_continue, (300, 400))
    pygame.display.flip()

# 封装函数三:游戏正式开始
def game_scores():
    global bmp_gaming
    str_tip = 'score:%s' % scores
    color_font = (255, 255, 255)
    font = pygame.font.SysFont("DroidSans.ttf", 40)
    bmp_gaming = font.render(str_tip, -1, color_font)

def bird_in_screen():
    if bird_rect.right >= width:
        step[0] = -1.0
    if bird_rect.left <= 0:
        step[0] = 1.0
    if bird_rect.bottom >= height:
        step[1] = -1.0
    if bird_rect.top <= 0:
        step[1] = 1.0

def ball_generation():
    # 发出新黄豆
    attack_body = pygame.image.load('pic/haixiu.png')
    attack_rect = bird_rect.copy()
    attack = {"body": attack_body, "rect": attack_rect}
    attack_list.append(attack)

    # 20%的几率产生红色
    rand_val = random.randint(0, 10)
    is_red = rand_val <= 3
    if is_red:
        ball_body = pygame.image.load('pic/love.png')
    else:
        ball_body = pygame.image.load('pic/unhappy.png')

    ball_rect = ball_body.get_rect()
    ball_rect.right = width
    ball_rect.top = random.randint(0, height - ball_rect.height)
    ball = {"body": ball_body, "rect": ball_rect, "red": is_red, "num": 0}
    ball_list.append(ball)

def check_crash():
    global b_collide,is_pause,is_gameover,scores
    for ball in ball_list:
        ball_rect = ball['rect']
        if bird_rect.colliderect(ball_rect) and not ball['red']:  # 吃到白球
            b_collide = True
            is_pause = True
            is_gameover = True
            sound = pygame.mixer.Sound("sound/bomb.wav")
            sound.play()
        if bird_rect.colliderect(ball_rect) and ball['red']:  # 吃到红球
            b_collide = True
            scores += 10
            sound = pygame.mixer.Sound("sound/succeed.wav")
            sound.play()
            ball_list.remove(ball)

    for ball in ball_list:
        for attack in attack_list:
            attack_rect = attack['rect']
            if attack_rect.colliderect(ball['rect']) and not ball['red']:  # 攻击到白球
                b_collide = True
                scores += 1
                ball['num'] += 1
                if not ball['red'] and ball['num'] == 3:
                    ball['body'] = pygame.image.load('pic/love.png')
                    ball['red'] = True
                attack_list.remove(attack)

def drow_ball():
    screen.fill((129, 216, 209))
    screen.blit(background, (0, 0))
    for ball in ball_list:
        screen.blit(ball['body'], ball['rect'])
    # 绘制发射害羞黄豆
    for attack in attack_list:
        screen.blit(attack['body'], attack['rect'])
    screen.blit(bird, bird_rect)
    screen.blit(bmp_gaming, (30, 20))
    pygame.display.flip()

def ball_move():
    # 小球移动
    ball_x_step = -1
    for ball in ball_list:
        ball["rect"].right += ball_x_step
    # 害羞黄豆移动
    attack_x_step = 3
    for attack in attack_list:
        attack["rect"].right += attack_x_step

def change_bg():
    global background_color_idx,background_color_list
    background_color_idx += 1
    screen.fill(background_color_list[background_color_idx])
    pygame.display.flip()
    if background_color_idx >= len(background_color_list)-1:
        background_color_idx = 0
    screen.fill(background_color_list[background_color_idx])
    screen.blit(bird, bird_rect)
    pygame.display.flip()

def mouse_move():
    x = pygame.mouse.get_pos()
    bird_rect.left = x[0] - bird_rect.width / 2
    bird_rect.top = x[1] - bird_rect.height / 2
    # screen.fill(background_color_list[background_color_idx])
    screen.blit(bird, bird_rect)

def key_move():
    global press_dict, is_going
    press_dict = {pygame.K_UP: (0, -2), pygame.K_DOWN: (0, 2),
                  pygame.K_LEFT: (-3, 0), pygame.K_RIGHT: (2, 0)}
    if event.key in press_dict:
        press = press_dict[event.key]
        step[0] = press[0]
        step[1] = press[1]
        bird_rect.right += step[0]
        bird_rect.top += step[1]
        is_going = True

def gameover():
    str_tip = 'Final:%s' % scores
    color_font = (255, 0, 0)
    font = pygame.font.SysFont("DroidSans.ttf", 60)
    bmp_gameover = font.render(str_tip, -1, color_font)
    screen.blit(bmp_gameover, (320, 250))
    pygame.display.flip()


# 游戏初始化
game_init()

# 第一个主循环，显示游戏正式开始前的界面
while True:
    start_screen_init()
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                b_quit1 = True
                break
    if b_quit1:
        break

# 第二个主循环，开始游戏
while True:
    tick = tick * 1.000001
    clock.tick(tick)
    game_scores()  # 得分文字
    bird_in_screen()  # 让小鸟运行,自动修改小鸟运动轨迹,全身在屏幕范围内
    # 不暂停的情况下
    if not is_pause and not is_gameover:
        this_time = pygame.time.get_ticks()
        if last_time < this_time - 500:
            last_time = this_time
            ball_generation()  # 发出新黄豆 # 20%的几率产生红色
        drow_ball()  # 绘制多个小球
        ball_move()   # 小球移动, 害羞黄豆移动
        check_crash()  # 检测碰撞
    # 监测鼠标和键盘的状态
    for event in pygame.event.get():
        # 鼠标响应
        mouse_pos = pygame.mouse.get_pos()
        if event.type == pygame.QUIT:
            b_quit = True
            break
        if event.type == pygame.MOUSEBUTTONDOWN and not is_pause:
            if bird_rect.collidepoint(mouse_pos):
                b_mouse_press = True
        if event.type == pygame.MOUSEBUTTONUP and not is_pause:
            b_mouse_press = False
        if event.type == pygame.MOUSEMOTION and not is_pause:
            if b_mouse_press:
                mouse_move()
            pass
        # 键盘响应
        is_going = False
        if event.type == pygame.KEYDOWN:
            if not is_pause:
                # change_bg()# 按任意键背景变色
                key_move() # 键盘上下左右移动
            # 退出游戏
            if event.key == pygame.K_RETURN:
                b_quit = True
                break
            if event.key == pygame.K_SPACE and not is_gameover:
                if not is_pause:
                    is_pause = True
                else:
                    is_pause = False
    if is_going:
        bird_rect = bird_rect.move(step)
    if is_gameover:
        gameover()
    if b_quit:
        break
# 退出游戏
pygame.quit()

