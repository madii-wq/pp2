import pygame

pygame.init()
w = 800
h = 400
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Circle_motion")
run = True
x_axis = 800 // 2
y_axis = 400 // 2
r = 25
velocity = 20
clock = pygame.time.Clock()
while run:
    clock.tick(60)
    screen.fill((255, 255, 255))
    circle = pygame.draw.circle(screen, (255,0,0), (x_axis, y_axis), r)
    pygame.display.update()
    for evelocityent in pygame.event.get():
        if evelocityent.type == pygame.QUIT:
            run = False
            pygame.quit()
    button = pygame.key.get_pressed()
    if button[pygame.K_LEFT] and x_axis > r:
        x_axis -= velocity
    if button[pygame.K_RIGHT] and x_axis < w - r:
        x_axis += velocity
    if button[pygame.K_UP] and y_axis > r:
        y_axis -= velocity
    if button[pygame.K_DOWN] and y_axis < h - r:
        y_axis += velocity
