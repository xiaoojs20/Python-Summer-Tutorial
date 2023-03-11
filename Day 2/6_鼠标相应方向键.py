import pygame

# 1.监测按键的事件
pygame.KEYUP
pygame.KEYDOWN
pygame.K_UP
pygame.K_DOWN
pygame.K_LEFT
pygame.K_RIGHT

# 2.善于利用dict，降低代码量
press_dict = {pygame.K_UP:(0,-1),pygame.K_DOWN:(0,1),
              pygame.K_LEFT:(-1,0),pygame.K_RIGHT:(1,0)}
if event.key in press_dict:
    press=press_dict[event.key]
    step[0]+=press[0]
    step[1]+=press[1]

bird_rect=bird_rect.move(step)
