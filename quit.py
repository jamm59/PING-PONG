from variables import *
def draw_quit(box,event):
    global CLICKED_QUIT
    q_text = pygame.font.SysFont('Calibri', 30)
    text = "Want to quit ?"
    pygame.draw.rect(WINDOW,WHITE,box)
    WINDOW.blit(q_text.render(text,1,BLACK),(box.x + 100,box.height // 2 - 50 ))
    yes = YES.get_rect(center=(box.x+100,box.height // 2 + 10))
    no = NO.get_rect(center=(box.x+250,box.height // 2 + 10))
    WINDOW.blit(YES,yes)
    WINDOW.blit(NO,no)
    mpos = pygame.mouse.get_pos()
    mouse = pygame.mouse
    if mouse.get_pressed()[0]:
        if pygame.Rect.collidepoint(yes, mouse.get_pos()):
            pygame.time.delay(2000)
            pygame.quit()
        if pygame.Rect.collidepoint(no, mouse.get_pos()):
            CLICKED_QUIT = False
        print(CLICKED_QUIT)