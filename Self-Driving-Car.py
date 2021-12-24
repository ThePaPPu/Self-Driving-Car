import pygame

pygame.init()

window = pygame.display.set_mode((1200, 400))
track = pygame.image.load('track6.png')
car = pygame.image.load('tesla.png')
car = pygame.transform.scale(car, (30, 60))
car_x = 152
car_y = 280
camera_x_offset = 0
camera_y_offset = 0
focal_distance = 25
direction = 'upper'
drive = True
clock = pygame.time.Clock()

while drive:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drive = False
    
    camera_x = car_x + camera_x_offset + 15
    camera_y = car_y + camera_y_offset + 15
    
    #detect road
    upper_pixel = window.get_at((camera_x, camera_y - focal_distance))[0]
    right_pixel = window.get_at((camera_x + focal_distance, camera_y))[0]
    down_pixel = window.get_at((camera_x , camera_y + focal_distance))[0]
    print(upper_pixel, right_pixel, down_pixel)
    
    #take turn or change direction
    if direction == 'upper' and upper_pixel != 255 and right_pixel == 255:
        direction = 'right'
        camera_x_offset = 30
        car = pygame.transform.rotate(car, -90)
    
    elif direction == 'right' and right_pixel != 255 and down_pixel == 255:
        direction = 'down'
        car_x = car_x + 30
        camera_x_offset = 0
        camera_y_offset = 30
        car = pygame.transform.rotate(car, -90)
        
    elif direction == 'down' and down_pixel != 255 and right_pixel == 255:
        direction = 'right'
        car_y = car_y + 30
        camera_x_offset = 30
        camera_y_offset = 0
        car = pygame.transform.rotate(car, 90)
    
    elif direction == 'right' and right_pixel != 255 and upper_pixel ==255:
        direction = 'upper'
        car_x = car_x + 30
        camera_x_offset = 0
        car = pygame.transform.rotate(car, 90)
        
        
    #drive
    if direction == 'upper' and upper_pixel == 255:
        car_y = car_y - 2
        
    elif direction == 'right' and right_pixel == 255:
        car_x = car_x + 2
    
    elif direction == 'down' and down_pixel == 255:
        car_y = car_y + 2 
        
    window.blit(track, (0, 0))
    window.blit(car, (car_x, car_y))
    pygame.draw.circle(window, (0, 255, 0), (camera_x, camera_y), 5, 5)
    pygame.display.update()