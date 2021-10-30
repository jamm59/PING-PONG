import pygame
from pygame.display import update
from variables import *
class Ball:
    def __init__(self):
        self.width,self.height = (S_WIDTH // 2 -50 , S_HEIGHT // 2 - 50)
        self.ball = BALL.get_rect(center=(self.width,self.height))
        self.velocity = 5
        self.x,self.y= 5,5
        self.count = 0

    def draw(self):
        WINDOW.blit(BALL,self.ball)
    def move(self):
        self.ball.x += self.x
        self.ball.y += self.y
    def update(self):
        if self.ball.top < 0 or  self.ball.bottom > S_HEIGHT - 10:
            self.y = -self.y

    def collide(self,typ):
        if typ.x < S_WIDTH // 2:
            if pygame.Rect.colliderect(self.ball,typ) and self.ball.x >= typ.x + 10:
                self.x = -self.x
        else:
            if pygame.Rect.colliderect(self.ball,typ) and self.ball.x >= typ.x - 35:
                self.x = -self.x


    def speed_up(self):
        if self.count % 2 == 0:
            if '-' in str(self.x):
                self.x = int(f'-{int(str(self.x)[1:]) + 1}')
            else:
                self.x += 1

            if '-' in str(self.y):
                self.y = int(f'-{int(str(self.y)[1:]) + 1}')
            else:
                self.y += 1
        self.count += 1