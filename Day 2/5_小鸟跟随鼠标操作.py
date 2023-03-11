import pygame

# 1.监测鼠标事件
pygame.MOUSEBUTTONDOWN
pygame.MOUSEBUTTONUP
pygame.MOUSEMOTION# 鼠标移动

# 2.获取鼠标位置
x=event.pos

# 3.监测某一个点是否在矩形内
if bird_rect.collidepoint(X):
    b_mouse_press =True