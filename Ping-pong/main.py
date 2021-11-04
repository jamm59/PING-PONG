from variables import *
from game import *
from settings import settings
import os

CLICKED_QUIT = False

def draw_quit(box):
    with open('file.txt', 'w') as file:
        file.write('2')
    global CLICKED_QUIT
    q_text = pygame.font.SysFont('Calibri', 30)
    pygame.draw.rect(WINDOW,WHITE,box,border_radius=7)
    WINDOW.blit(q_text.render("Are you sure you ",1,BLACK),(box.x + 80,box.height // 2 + 30 ))
    WINDOW.blit(q_text.render("want to Exit ?",1,BLACK),(box.x + 100,box.height // 2 + 70 ))
    yes = YES.get_rect(center=(box.x+100,box.height // 2 + 150))
    no = NO.get_rect(center=(box.x+250,box.height // 2 + 150))
    WINDOW.blit(YES,yes)
    WINDOW.blit(NO,no)
    mouse = pygame.mouse
    if mouse.get_pressed()[0]:
        if pygame.Rect.collidepoint(yes, mouse.get_pos()):
            with open('file.txt', 'w') as file:
                file.write('0')
            pygame.quit()
            os.sys.exit()
        elif pygame.Rect.collidepoint(no, mouse.get_pos()):
            CLICKED_QUIT = False
            with open('file.txt', 'w') as file:
                file.write('1')

            



def draw_menu(**kwargs):
    WINDOW.fill(BG_COLOR)
    title = pygame.font.SysFont('Calibri', 60)
    title.set_bold(50)
    WINDOW.blit(title.render('PING PONG',1,WHITE),(S_WIDTH // 2 - 200, 30))
    M_FONT.set_bold(2)
    WINDOW.blit(M_FONT.render('MENU', 1, WHITE),(S_WIDTH // 2 - 100,  150))
    for i,(key,value) in enumerate(kwargs.items()):
        if i == 0 or i % 2 == 0:
            pygame.draw.rect(WINDOW,WHITE,value,border_radius=6)
            WINDOW.blit(FONT.render(MENU_V[i],1,BLACK),(value.x + 50, value.y + 5))
        else:
            pygame.draw.rect(WINDOW,BLACK,value,border_radius=6)
            WINDOW.blit(FONT.render(MENU_V[i],1,WHITE),(value.x + 20, value.y + 5))

    if CLICKED_QUIT:
        draw_quit(BOX)

    pygame.display.update()


def menu_main():
    global CLICKED_QUIT
    pygame.display.set_caption('Menu')
    btnx,btny,btnw,btnh = S_WIDTH // 2 - 120,'',150,50
    btn1 = pygame.Rect(btnx,210, btnw,btnh)
    btn2 = pygame.Rect(btnx,280, btnw,btnh)
    btn3 = pygame.Rect(btnx,350, btnw,btnh)
    running = True
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            # if event.type == VIDEORESIZE:
            #     pygame.display.set_mode((int(data[0].strip('\n')),int(data[1].strip('\n'))))
            if event.type == MOUSEBUTTONUP:
                mpos = pygame.mouse.get_pos()
                if pygame.Rect.collidepoint(btn1,mpos):
                    game_ui(draw_quit)
                if pygame.Rect.collidepoint(btn2,mpos):
                    settings()
                if pygame.Rect.collidepoint(btn3,mpos):
                    CLICKED_QUIT = True

        draw_menu(a=btn1,b=btn2,c=btn3)
    pygame.quit()

if __name__ == '__main__':
    menu_main()