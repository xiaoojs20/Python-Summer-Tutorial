import pygame

# 1.利用dict来存储每个小球的信息body rect
ball={"body":ball_body,"rect":ball_rect}

# 2.绘制多个小球
for ball in ball_list:
    screen.blit(ball['body'],ball['rect'])

# 3.利用random包，来生成随机数
if last_time < this_time-0.5:
    last_time=this_time
    ball_body=pygame.image.load('pic/ball.png')
    ball_rect=ball_body.get_rect()
    ball_rect.right=width
    ball_rect.top=random.randint(0,height-ball_rect.height)
    ball={"body":ball_body,"rect":ball_rect}
    ball_list.append(ball)

# 4.调用colliderect，来检测两个矩形是否发生碰撞
b_collide=False
for ball in ball_list:
    ball_rect = ball['rect']
    if bird_rect.colliderect(ball_rect):
        b_collide=True
        break