import pygame
"""
1.游戏中，左上角显示分值，字体是白色40号
2.游戏结束后，在屏幕正中央显示最终的得到，字体是红色60号字
3.某小球在最左侧消失后，游戏得分+10
"""

# 1.文字初始化
pygame.font.init()

# 2.设置字体和大小
font=pygame.font.SysFont("Song",40)

# 3.文字->图片
str_tip='Final:%s'% scores
color_font=(255,0,0)
bmp_gameover=font.render(str_tip,-1,color_font)

# 4.打印图片
screen.blit(bmp_gameover,(top,left))

