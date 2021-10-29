from variables import *
class Paddle:
    def __init__(self,pad,pos):
        self.pad = pad
        self.paddle = self.pad.get_rect(center=pos)
        self.velocity = 10
        self.y = 0
        self.score = 0
    def draw(self):
        WINDOW.blit(self.pad,self.paddle)
