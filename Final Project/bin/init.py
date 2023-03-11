import pygame


class init():
    def screen_init(self):
        # 屏幕初始化
        self.width = 800
        self.height = 600
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.background_color = (255, 0, 0)
        # 取消变色功能吧
        # background_color_list = [(128, 128, 128), (0, 0, 255), (255, 0, 0), (0, 255, 0), (255, 255, 255)]
        # background_color_idx = 0
        self.background = pygame.image.load('../resource/pic/background.png').convert()
        self.screen.blit(self.background, (0, 0))

    def word_init(self):
        pygame.font.init()
        pygame.font.get_fonts()

    def music_init(self):
        pygame.mixer.init()
        pygame.mixer.music.load("../resource/sound/cjml.mp3")
        pygame.mixer.music.play(-1, 0)

    def clock_init(self):
        self.this_time = pygame.time.get_ticks()
        self.last_time = pygame.time.get_ticks()
        self.tick = 100
        self.clock = pygame.time.Clock()

    def bird_init(self):
        self.bird = pygame.image.load('../resource/pic/red_bird.png')
        pygame.transform.scale(self.bird, (80, 60))
        self.bird_rect = self.bird.get_rect()
        self.bird_rect.right = 100
        self.bird_rect.top = 100
        self.screen.blit(self.bird, self.bird_rect)
        pygame.display.flip()

    def flag_init(self):
        self.b_quit = False
        self.b_mouse_press = False
        self.b_collide = False
        self.is_pause = False
        self.is_gameover = False
        self.is_going = False
        self.b_quit1 = False

    # 总体初始化
    def game_init(self):
        pygame.init()
        self.screen_init()
        # 分数初始化
        self.scores = 0
        self.step = [0, 0]

        self.word_init()  # 文字初始化
        self.music_init()  # 音乐初始化
        self.clock_init()  # 时间和频率的初始化
        self.bird_init()  # 添加小鸟
        self.flag_init()  # 初始化一些布尔值
        # 球列表
        self.ball_list = []
        self.attack_list = []

    # 开始界面
    def start_screen_init(self):
        gamename = 'Angry Birds'
        color_font = (255, 0, 0)
        font = pygame.font.SysFont("DroidSans.ttf", 80)
        bmp_gamename = font.render(gamename, -1, color_font)
        gamecontinue = 'push Enter to continue'
        color_font = (255, 255, 0)
        font = pygame.font.SysFont("DroidSans.ttf", 40)
        bmp_continue = font.render(gamecontinue, -1, color_font)
        self.screen.blit(bmp_gamename, (220, 250))
        self.screen.blit(bmp_continue, (300, 400))
        pygame.display.flip()


init_example = init()


def init_func():
    init_example.game_init()
    while True:
        init_example.start_screen_init()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    b_quit1 = True
                    break
        if init_example.b_quit1:
            break


if __name__ == "__main__":
    init_func()
