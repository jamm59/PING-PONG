import pygame
from pygame.locals import *
pygame.font.init()
FPS = 60
clock = pygame.time.Clock()
MENU_V = ['Play','Settings','Quit']
SETTINGS_INFO = ['900x500','900x600','1000x600','1000x700','1200x700']
M_FONT = pygame.font.SysFont('Calibri', 40)
FONT = pygame.font.SysFont('Calibri', 35)
FONT2 = pygame.font.SysFont('Calibri', 60)
WHITE = (255,255,255)
BLACK = (0,0,0)
BG_COLOR = (255,213,213)
DIR = 'assets'
S_WIDTH  = 900
S_HEIGHT = 500
WIDTH = 40
HEIGHT = 150
BALL = pygame.image.load(f'{DIR}/ball.png')
LEFT_P = pygame.image.load(f'{DIR}/bat.png')
RIGHT_P = pygame.image.load(f'{DIR}/bat.png')
BALL = pygame.transform.scale(BALL,(50,50))
LEFT_P = pygame.transform.scale(LEFT_P,(WIDTH,HEIGHT))
RIGHT_P = pygame.transform.scale(RIGHT_P,(WIDTH,HEIGHT))
BORDER = pygame.Rect(S_WIDTH // 2, 0, 5,S_HEIGHT)
WINDOW = pygame.display.set_mode((S_WIDTH,S_HEIGHT))



def draw_settings():
    WINDOW.fill(BG_COLOR)
    title = pygame.font.SysFont('Calibri', 60)
    title.set_bold(50)
    WINDOW.blit(title.render('Settings',1,WHITE),(S_WIDTH // 2 - 150, 30))
    h = 140
    w = S_WIDTH // 2 - 120
    for i in range(0,len(SETTINGS_INFO)):
        if i == 0 or i % 2 == 0:
            pygame.draw.rect(WINDOW,WHITE,pygame.Rect(w,h,150,50))
            WINDOW.blit(FONT.render(SETTINGS_INFO[i],1,BLACK),(w + 10, h + 7))
        else:
            pygame.draw.rect(WINDOW,BLACK,pygame.Rect(w,h,150,50))
            WINDOW.blit(FONT.render(SETTINGS_INFO[i],1,WHITE),(w + 10, h + 7))
        
        h += 70
    pygame.display.update()
def settings():
    setting_on = True
    while setting_on:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == QUIT:
                setting_on = False
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    setting_on = False

        draw_settings()


