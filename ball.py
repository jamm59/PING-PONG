import pygame
from pygame.display import update
from variables import *
class Ball:
    def __init__(self):
        self.width,self.height = (S_WIDTH // 2 -50 , S_HEIGHT // 2 - 50)
        self.ball = BALL.get_rect(center=(self.width,self.height))
        self.velocity = 5
        self.x,self.y= 5,5

    def draw(self):
        WINDOW.blit(BALL,self.ball)
    def move(self):
        self.ball.x += self.x
        self.ball.y += self.y
    def update(self):
        if self.ball.top < 0 or  self.ball.bottom > S_HEIGHT - 50:
            self.y = -self.y

    def collide(self,typ):
        if pygame.Rect.colliderect(self.ball,typ):
            self.x = -self.x

    def speed_up(self):
        if '-' in str(self.x):
            self.x = int(f'-{int(str(self.x)[1:]) + 1}')
        else:
            self.x += 1

        if '-' in str(self.y):
            self.y = int(f'-{int(str(self.y)[1:]) + 1}')
        else:
            self.y += 1