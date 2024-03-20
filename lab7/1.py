import pygame
import math
import datetime

pygame.init()

running = True
clock = pygame.time.Clock()
screen = pygame.display.set_mode((600, 600))
image = pygame.image.load("clock_background.jpg")
def convert_degrees(r, theta):
    y = math.cos(2*math.pi*theta/360)*r
    x = math.sin(2*math.pi*theta/360)*r
    return x+300, 300 - y
    
while running:
    screen.fill((255,255,255))
    current = datetime.datetime.now()
    screen.blit(image, (0,0))

    minite = current.minute
    second = current.second
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
    #minute 
    theta = (minite + second/60)*(360/60)
    r = 120
    pygame.draw.line(screen, (0,0,0), (300,300), convert_degrees(r, theta),6)
    #second
    theta = second
    r = 140
    pygame.draw.line(screen, (255,0,0), (300,300), convert_degrees(r, theta),4)
    clock.tick(60)
    pygame.display.flip() 