from variables import *
RECT = []
def draw_settings():
    global RECT
    WINDOW.fill(BG_COLOR)
    title = pygame.font.SysFont('Calibri', 60)
    title.set_bold(50)
    WINDOW.blit(title.render('Settings',1,WHITE),(S_WIDTH // 2 - 150, 30))
    h = 140
    w = S_WIDTH // 2 - 120
    for i in range(0,len(SETTINGS_INFO)):
        if i == 0 or i % 2 == 0:
            pygame.draw.rect(WINDOW,WHITE,pygame.Rect(w,h,150,50),border_radius=6)
            WINDOW.blit(FONT.render(SETTINGS_INFO[i],1,BLACK),(w + 10, h + 7))
        else:
            pygame.draw.rect(WINDOW,BLACK,pygame.Rect(w,h,150,50),border_radius=6)
            WINDOW.blit(FONT.render(SETTINGS_INFO[i],1,WHITE),(w + 10, h + 7))
        if len(RECT) < 5:
            RECT.append(pygame.Rect(w,h,150,50))
        h += 70
    pygame.display.update()
def settings():
    setting_on = True
    pygame.display.set_caption('Settings')
    while setting_on:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == QUIT:
                setting_on = False
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    setting_on = False
            if event.type == MOUSEBUTTONUP:
                for i in range(0, len(RECT)):
                    pos = pygame.mouse.get_pos()
                    if pygame.Rect.collidepoint(RECT[i],pos):
                        new_x = SETTINGS_INFO[i].split('x')[0]
                        new_y = SETTINGS_INFO[i].split('x')[1]
                        with open('screen.txt','w') as file:
                            file.write(f'{new_x}\n{new_y}')
        draw_settings()


