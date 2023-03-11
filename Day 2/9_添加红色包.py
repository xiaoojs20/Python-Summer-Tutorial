import pygame

# 1.20%的几率回产生红色
rand_val=random.randint(0,10)
is_red=rand_val<=3
if is_red:
    ball_body=pygame.image.load('pic/red_ball.png')
else:
    ball_body=pygame.image.load('pic/ball.png')
ball={"body":ball_body,"rect":ball_rect,"red":is_red}

ball_rect=ball_body.get_rect()
ball_rect.right=width
ball_rect.top=random.randint(0,height-ball_rect.height)
ball={"body":ball_body,"rect":ball_rect,"red":is_red}

# 2.如果吃到了红包，则分值+40，如果吃到的不是红色，则game over
for ball in ball_list:;
    ball_rect=ball['rect']
    is_red=ball['red']
    if bird_rect.colliderect(ball_reect):
        if is_red:
            scores += 40
            ball_list.remove(ball)
        else:
            is_game_over=True

# 3. 如果没有吃到红包，则游戏速度*2
tick *= 2

# 4.如果分值<0，则游戏结束
if scores<0:
    is_game_over=True