import pygame, random, time
# 初始化
pygame.init()
# 屏幕初始化
width = 800
height = 600
screen = pygame.display.set_mode((width, height))
background_color=(255,0,0)
background_color_list=[(128,128,128),(0,0,255),(255,0,0),(0,255,0),(255,255,255)]
background_color_idx=0
screen.fill((0,0,0))
# 分数初始化
scores=0
step=[0,0]
# 文字初始化
pygame.font.init()
# 音乐初始化
pygame.mixer.init()
pygame.mixer.music.load("sound/蜜雪冰城.mp3")
pygame.mixer.music.play(-1, 0)
# 时间的初始化
this_time = pygame.time.get_ticks()
last_time = pygame.time.get_ticks()
# 添加小鸟
bird = pygame.image.load('pic/haha.png')
pygame.transform.scale(bird, (80, 60))
bird_rect = bird.get_rect()
bird_rect.right = 100
bird_rect.top = 100
screen.blit(bird, bird_rect)
pygame.display.flip()
# 球列表
ball_list = []
# 修改页面刷新频率
tick = 100
clock = pygame.time.Clock()
# 初始化一些布尔值
b_quit = False
b_mouse_press = False
b_collide=False
is_pause = False
is_gameover=False
is_going=False

# 主循环
while True:
    clock.tick(tick)
    # 得分文字
    str_tip = 'score:%s' % scores
    color_font = (255, 255, 255)
    font = pygame.font.SysFont("Song", 40)
    bmp_gaming = font.render(str_tip, -1, color_font)
    # 让小鸟运行,自动修改小鸟运动轨迹,全身在屏幕范围内
    if bird_rect.right >= width:
        x_step = -1.0
    if bird_rect.left <= 0:
        x_step = 1.0
    if bird_rect.bottom >= height:
        y_step = -1.0
    if bird_rect.top <= 0:
        y_step = 1.0

    # 不暂停的情况下
    if not is_pause:
        # 利用dict来存储每个小球的信息body rect
        # 利用random包，来生成随机数
        this_time = pygame.time.get_ticks()
        if last_time < this_time - 500:
            last_time = this_time
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
            ball = {"body": ball_body, "rect": ball_rect, "red": is_red}
            ball_list.append(ball)

        # 绘制多个小球
        screen.fill((0,0,0))
        for ball in ball_list:
            screen.blit(ball['body'], ball['rect'])
        screen.blit(bird, bird_rect)
        screen.blit(bmp_gaming, (0, 0))
        pygame.display.flip()

        # 小球移动
        ball_x_step = -1
        for ball in ball_list:
            ball["rect"].right += ball_x_step

        # 检测碰撞
        for ball in ball_list:
            ball_rect = ball['rect']
            if bird_rect.colliderect(ball_rect) and not ball['red']: #吃到白球
                b_collide = True
                is_pause = True
                is_gameover = True
                sound = pygame.mixer.Sound("sound/bomb.wav")
                sound.play()
            if bird_rect.colliderect(ball_rect) and ball['red']: # 吃到红球
                b_collide = True
                scores += 40
                sound = pygame.mixer.Sound("sound/succeed.wav")
                sound.play()
                ball_list.remove(ball)

    # 监测鼠标和键盘的状态
    for event in pygame.event.get():
        # 鼠标响应
        mouse_pos = pygame.mouse.get_pos()
        if event.type == pygame.QUIT:
            b_quit=True
            break
        if event.type == pygame.MOUSEBUTTONDOWN and not is_pause:
            if bird_rect.collidepoint(mouse_pos):
                b_mouse_press = True
        if event.type == pygame.MOUSEBUTTONUP and not is_pause:
            b_mouse_press = False
        if event.type == pygame.MOUSEMOTION and not is_pause:
            if b_mouse_press:
                x = pygame.mouse.get_pos()
                bird_rect.left=x[0]-bird_rect.width/2
                bird_rect.top=x[1]-bird_rect.height/2
                screen.fill(background_color_list[background_color_idx])
                screen.blit(bird, bird_rect)
            pass

        # 键盘响应
        # 按任意键背景变色
        is_going = False
        if event.type == pygame.KEYDOWN:
            if not is_pause:
                # background_color_idx += 1
                # screen.fill(background_color_list[background_color_idx])
                # pygame.display.flip()
                # if background_color_idx >= len(background_color_list)-1:
                #     background_color_idx = 0
                # screen.fill(background_color_list[background_color_idx])
                # screen.blit(bird, bird_rect)
                # pygame.display.flip()
            # 键盘上下左右移动

                press_dict = {pygame.K_UP: (0, -2), pygame.K_DOWN: (0, 2),
                              pygame.K_LEFT: (-3, 0), pygame.K_RIGHT: (2, 0)}
                if event.key in press_dict:
                    press = press_dict[event.key]
                    step[0] = press[0]
                    step[1] = press[1]
                    bird_rect.right += step[0]
                    bird_rect.top += step[1]
                    is_going=True
            # 退出游戏
            if event.key == pygame.K_RETURN:
                b_quit = True
                break
            if event.key == pygame.K_SPACE:
                if not is_pause:
                    is_pause=True
                else:
                    is_pause=False
    if is_going:
        bird_rect = bird_rect.move(step)

    if is_gameover:
        str_tip = 'Final:%s' % scores
        color_font = (255, 0, 0)
        font = pygame.font.SysFont("Song", 60)
        bmp_gameover = font.render(str_tip, -1, color_font)
        screen.blit(bmp_gameover, (330, 250))
        pygame.display.flip()
    if b_quit:
        break
# 退出游戏
pygame.quit()

