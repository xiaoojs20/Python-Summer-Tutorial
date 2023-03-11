"""
1、点击退出按键，则退出游戏
2、按下空格键或回车键，则退出窗口
"""

import pygame
# 1.对事件进行遍历
for event in pygame.event.get():
    pass

# 2.点击退出按钮事件
if pygame.type==pygame.QUIT:
    pass

# 3.键盘按钮事件
if event.type==pygame.KEYDOWN:
    if event.key==pygame.K_RETURN or event.key==pygame.K_SPACE:
        b_quit=True
        pass
