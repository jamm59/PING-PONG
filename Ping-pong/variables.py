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
DIR = 'H:/Ping-pong-master/Ping-pong/assets'
S_WIDTH,S_HEIGHT  = 900,500
WIDTH,HEIGHT = 40,150
D_WIDTH,D_HEIGHT = 40,40
BALL = pygame.image.load(f'{DIR}/ball.png')
BALL = pygame.transform.scale(BALL,(50,50))
LEFT_P = pygame.transform.scale(pygame.image.load(f'{DIR}/bat.png'),(WIDTH,HEIGHT))
RIGHT_P = pygame.transform.scale(pygame.image.load(f'{DIR}/bat.png'),(WIDTH,HEIGHT))
YES = pygame.transform.scale(pygame.image.load(f'{DIR}/yes.png'),(D_WIDTH,D_HEIGHT))
NO = pygame.transform.scale(pygame.image.load(f'{DIR}/no.png'),(D_WIDTH,D_HEIGHT))
BORDER = pygame.Rect(S_WIDTH // 2, 0, 5,S_HEIGHT)
WINDOW = pygame.display.set_mode((S_WIDTH,S_HEIGHT))
BOX = pygame.Rect(S_WIDTH // 2 - 210, 100, 400, 200)



