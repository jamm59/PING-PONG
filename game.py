from variables import *
from ball import Ball
from paddle import Paddle
import random


def draw_win(left,right,ball,text):
    WINDOW.fill(BG_COLOR)
    pygame.draw.rect(WINDOW,(255,255,255),BORDER)
    WINDOW.blit(FONT.render(f'score: {left.score}',1,WHITE),(40, 10))
    WINDOW.blit(FONT.render(f'score: {right.score}',1,WHITE),(S_WIDTH - 150, 10))
    ball.draw()
    left.draw()
    right.draw()
    if text != '':
        FONT2.set_bold(50)
        WINDOW.blit(FONT2.render(text, 1,BLACK),(S_WIDTH // 2 - 150, S_HEIGHT // 2))
        pygame.display.update()
        return False
    pygame.display.update()
    return True

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



def game_ui():
    pygame.display.set_caption('PING PONG')
    run = True
    left  = Paddle(LEFT_P,(30, S_HEIGHT // 2 -100))
    right = Paddle(RIGHT_P, (S_WIDTH - 30, S_HEIGHT // 2 -50 ))
    m_ball = Ball()
    pause = False
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == QUIT:
                run = False
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    run = False
                if event.key == K_SPACE:
                    global BG_COLOR
                    BG_COLOR = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
                    pause = not pause

        if pause:
            continue

        if m_ball.ball.left < 0:
            right.score += 1
            m_ball.ball.x,m_ball.ball.y = m_ball.width,m_ball.height 
            m_ball.speed_up()
        if m_ball.ball.right > S_WIDTH:
            left.score += 1
            m_ball.ball.x,m_ball.ball.y = m_ball.width,m_ball.height
            m_ball.speed_up()
        
        text = ''
        if left.score == 10:
            text += 'LEFT WINS!!'
        elif right.score == 10:
            text += 'RIGHT WINS!!'
            
        m_ball.move()
        m_ball.update()
        m_ball.collide(left.paddle)
        m_ball.collide(right.paddle)
        check(left,2)
        check(right,1)
        if not draw_win(left,right,m_ball,text):
            pygame.time.delay(2000)
            run = False
