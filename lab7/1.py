import pygame
import sys
import datetime

pygame.init()

window = pygame.display.set_mode((500, 500))

current_time = datetime.datetime.now()

left = pygame.image.load('lab7/background/left.jpg')
left = pygame.transform.scale(left, (300, 300))

right = pygame.image.load('lab7/background/right.jpg')
right = pygame.transform.scale(right, (200, 200))

mickie = pygame.image.load('lab7/background/mickie.jpg')

left_rect = left.get_rect()
center_l = left_rect.center

left.set_colorkey((0, 0, 0))

right_rect = right.get_rect()
center_r = right_rect.center

right.set_colorkey((0, 0, 0))

second = current_time.second

minute = current_time.minute

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    second -= 6
    minute -= 0.5
    rleft = pygame.transform.rotate(left, second)
    left_rect = rleft.get_rect(center=center_l)
    left_rect.move_ip(100, 100)

    rright = pygame.transform.rotate(right, minute)
    right_rect = rright.get_rect(center=center_r)
    right_rect.move_ip(150, 150)

    window.blit(mickie, (0, 0))
    window.blit(rright, right_rect.topleft)
    window.blit(rleft, left_rect.topleft)
    pygame.display.update()
    clock.tick(1)