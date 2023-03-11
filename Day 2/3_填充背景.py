"""
1、填充界面颜色
2、按下任意键，界面颜色发生变化
"""

import pygame

# 填充界面颜色
screen.fill((0,0,0))
pygame.display.flip()

# 响应键盘事件，修改页面颜色
background_color_list=[(128,128,128),(0,0,255),(255,0,0,),(0,255,0),(255,255,255)]
background_color_idx=0
if event.type==pygame.KEYDOWN:
    background_color_idx+=1
    if background_color_idx >= len(background_color_list):
        background_color_idx=0
    screen.fill(background_color_list[background_color_idx])



