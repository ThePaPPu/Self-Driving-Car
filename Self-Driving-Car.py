import pygame

pygame.init()

window = pygame.display.set_mode((1200, 400))
track = pygame.image.load('track1.png')
car = pygame.image.load('tesla.png')
car = pygame.transform.scale(car, (30, 60))
car_x = 152
car_y = 280

drive = True

while drive:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drive = False
    window.blit(track, (0, 0))
    window.blit(car, (car_x, car_y))
    pygame.display.update()