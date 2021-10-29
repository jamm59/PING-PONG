import pygame
from pygame.constants import QUIT
from variables import *
from ball import Ball
from paddle import Paddle

FPS = 60
clock = pygame.time.Clock()

pygame.display.set_caption('PING PONG')


def draw_win(left,right,ball):
    WINDOW.fill(BG_COLOR)
    pygame.draw.rect(WINDOW,(255,255,255),BORDER)
    WINDOW.blit(FONT.render(f'score: {left.score}',1,WHITE),(40, 10))
    WINDOW.blit(FONT.render(f'score: {right.score}',1,WHITE),(S_WIDTH - 150, 10))
    ball.draw()
    left.draw()
    right.draw()
    pygame.display.update()

def check(typ,num):
    keys_pressed = pygame.key.get_pressed()
    first = [pygame.K_UP,pygame.K_DOWN]
    second = [pygame.K_w,pygame.K_s]
    
    if num == 1:
        other = first
    else :
        other = second

    if keys_pressed[other[0]] and typ.paddle.top > 5: # UP
        typ.paddle.y -= typ.velocity

    if keys_pressed[other[1]] and typ.paddle.bottom < S_HEIGHT - 5: # DOWN
        typ.paddle.y += typ.velocity

def main():
    run = True
    left  = Paddle(LEFT_P,(30, S_HEIGHT // 2 -100))
    right = Paddle(RIGHT_P, (S_WIDTH - 30, S_HEIGHT // 2 -50 ))
    m_ball = Ball()
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == QUIT:
                run = False

        if m_ball.ball.left < 0:
            right.score += 1
            m_ball.ball.x,m_ball.ball.y = m_ball.width,m_ball.height 
            m_ball.velocity += 10
        if m_ball.ball.right > S_WIDTH:
            left.score += 1
            m_ball.ball.x,m_ball.ball.y = m_ball.width,m_ball.height
            m_ball.velocity += 10
            
        m_ball.move()
        m_ball.update()
        m_ball.collide(left.paddle)
        m_ball.collide(right.paddle)
        check(left,2)
        check(right,1)
        draw_win(left,right,m_ball)

    pygame.quit()

if __name__ == '__main__':
    main()