from variables import *
from game import *
from settings import settings
from quit import *


def draw_menu(new,**kwargs):
    WINDOW.fill(BG_COLOR)
    title = pygame.font.SysFont('Calibri', 60)
    title.set_bold(50)
    WINDOW.blit(title.render('PING PONG',1,WHITE),(S_WIDTH // 2 - 200, 30))
    M_FONT.set_bold(2)
    WINDOW.blit(M_FONT.render('MENU', 1, WHITE),(S_WIDTH // 2 - 100, S_HEIGHT // 2 - 100))
    for i,(key,value) in enumerate(kwargs.items()):
        if i == 0 or i % 2 == 0:
            pygame.draw.rect(WINDOW,WHITE,value)
            WINDOW.blit(FONT.render(MENU_V[i],1,BLACK),(value.x + 50, value.y + 5))
        else:
            pygame.draw.rect(WINDOW,BLACK,value)
            WINDOW.blit(FONT.render(MENU_V[i],1,WHITE),(value.x + 20, value.y + 5))

    if CLICKED_QUIT:
        draw_quit(BOX,new)

    pygame.display.update()


def menu_main():
    global CLICKED_QUIT
    pygame.display.set_caption('Menu')
    btnx,btny,btnw,btnh = S_WIDTH // 2 - 120,'',150,50
    btn1 = pygame.Rect(btnx,210, btnw,btnh)
    btn2 = pygame.Rect(btnx,280, btnw,btnh)
    btn3 = pygame.Rect(btnx,350, btnw,btnh)
    running = True
    new_e = None
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False

            if event.type == MOUSEBUTTONUP:
                mpos = pygame.mouse.get_pos()
                if pygame.Rect.collidepoint(btn1,mpos):
                    game_ui()
                if pygame.Rect.collidepoint(btn2,mpos):
                    settings()
                if pygame.Rect.collidepoint(btn3,mpos):
                    CLICKED_QUIT = True
                    new_e = event

        draw_menu(new_e,a=btn1,b=btn2,c=btn3)
    pygame.quit()

if __name__ == '__main__':
    menu_main()