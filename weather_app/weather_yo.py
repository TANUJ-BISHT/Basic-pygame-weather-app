import pygame
import pygame_gui
import weather_img

pygame.init()
width, height = 800, 800
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("TANUJ LEARNING WEATHER APP")
clock = pygame.time.Clock()
manager = pygame_gui.UIManager((width, height))
text_box = pygame_gui.elements.UITextEntryLine(
    relative_rect=pygame.Rect((100, 100), (600, 40)),
    manager=manager
)
background_image = pygame.image.load('assets/default.jpg').convert_alpha()
background_image = pygame.transform.scale(background_image, (800, 800))
screen.blit(background_image, (-1, -1))
font = pygame.font.Font(None, 36)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        manager.process_events(event)

    head = font.render('ENTER CITY NAME IN TEXT BOX (*_*)',True, (255, 255, 255))
    screen.blit(head,(190, 50))
    manager.update(clock.tick(60)/1000)
    manager.draw_ui(screen)
    pygame.display.update()

    city = text_box.text
    if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
        try:
            data = weather_img.get_weather_data(city)
            text_render = font.render(data[1], True, (255, 255, 255))
            text_render_rect = text_render.get_rect()
            text_render_rect.center = (width // 2, height // 2)
            temp_img = pygame.image.load(weather_img.get_img(data[0])).convert_alpha()
            temp_img = pygame.transform.scale(temp_img, (800, 800))
            screen.blit(temp_img, (-1, -1))
            screen.blit(text_render, text_render_rect)
        except:
            text_render1 = font.render('CITY KA NAME DHANG SE DAL CHAL.... :)',True,(255, 255, 255))
            text_render_rect1 = text_render1.get_rect()
            text_render_rect1.center = (width // 2, (height // 2) - 50)
            screen.blit(text_render1, text_render_rect1)

pygame.quit()