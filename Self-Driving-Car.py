import pygame

pygame.init()

window = pygame.display.set_mode((1200, 400))
track = pygame.image.load('track2.png')
car = pygame.image.load('tesla.png')
car = pygame.transform.scale(car, (30, 60))
car_x = 152
car_y = 280
focal_distance = 25
drive = True
clock = pygame.time.Clock()

while drive:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drive = False
    
    camera_x = car_x + 15
    camera_y = car_y + 15
    
    #detect road
    upper_pixel = window.get_at((camera_x, camera_y - focal_distance))[0]
    print(upper_pixel)
    
    if upper_pixel == 255:
        car_y = car_y - 2
        
    window.blit(track, (0, 0))
    window.blit(car, (car_x, car_y))
    pygame.draw.circle(window, (0, 255, 0), (camera_x, camera_y), 5, 5)
    pygame.display.update()