import pygame

# 1.添加小鸟
bird=pygame.image.load('pic/bird.png')
bird_rect=bird.get_rect()
bird_rect.right=100
bird_rect.top=100
screen.blit(bird,bird_rect)

# 2.修改图片大小
pygame.transform.scale(image,(80,60))

# 3.让小鸟运行
x_step=1
y_step=1
bird_rect.left+=x_step
bird_rect.top+=y_step

# 4.自动修改小鸟运动轨迹
if bird_rect.right >= width:
    x_step=-1.0
if bird_rect.left <=0:
    x_step=1.0
if bird_rect.bottom>= height:
    y_step=-1.0
if bird_rect.top<=0:
    y_step=1.0

# 5.修改页面刷新频率
tick=100
clock=pygame.time.Clock()
while True:
    clock.tick(tick)