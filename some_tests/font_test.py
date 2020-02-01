import pygame

pygame.init()

sc = pygame.display.set_mode((400, 300))
sc.fill((200, 255, 200))

font = pygame.font.Font(None, 72)
text = font.render("Hello Wold", 1, (0, 100, 0))
place = text.get_rect(center=(200, 150))
sc.blit(text, place)

pygame.display.update()

while 1:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            exit()

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_LEFT]:
        place.x -= 1
    elif pressed[pygame.K_RIGHT]:
        place.x += 1

    sc.fill((200, 255, 200))
    sc.blit(text, place)

    pygame.display.update()

    pygame.time.delay(20)
