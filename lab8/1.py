import pygame
import sys
from random import randint
from pygame.math import Vector2

pygame.init()

velocity = 1
score = 0
Game_Over = False

BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

screen = pygame.display.set_mode((800, 800))
font_style = pygame.font.SysFont("arial", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

class Fruit:
    def __init__(self):
        self.x = randint(0, cell_number - 1)
        self.y = randint(0, cell_number - 1)
        self.pos = Vector2(self.x,self.y)

    def draw_fruit(self):
        fruit_rect = pygame.Rect(int(self.pos.x * cell_size), int(self.pos.y * cell_size), cell_size, cell_size)
        pygame.draw.rect(screen,(126,166,114),fruit_rect)

class Snake:
    def __init__(self):
        self.body =  [Vector2(5, 10), Vector2(6,10), Vector2(7,10)]
        self.direction = Vector2(1, 0)

    def draw_snake(self):
        for block in self.body:
            block_rect = pygame.Rect(int(block.x * cell_size), int(block.y * cell_size), cell_size, cell_size)
            pygame.draw.rect(screen, (183,111,122), block_rect)

    def move(self):
        new_head = self.body[0] + self.direction
        
        self.body.insert(0, new_head)
        
        self.body.pop()

    def grow(self):

        self.body.append(self.body[-1])

    def change_direction(self, new_direction):
        if new_direction != -self.direction:
            self.direction = new_direction
def show_score(score):
    value = score_font.render("Your Score: " + str(score), True, RED)
    screen.blit(value, [0, 0])

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    text_rect = mesg.get_rect(center=(800 / 2, 800 / 2))
    screen.blit(mesg, text_rect)
    
def game_over():
    message("Game Over!", RED)
    pygame.display.flip()
    pygame.time.wait(2000)
    pygame.quit()
    sys.exit()
cell_size = 20
cell_number = 20

fruit = Fruit()
snake = Snake()
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snake.change_direction(Vector2(0, -1))
            elif event.key == pygame.K_DOWN:
                snake.change_direction(Vector2(0, 1))
            elif event.key == pygame.K_LEFT:
                snake.change_direction(Vector2(-1, 0))
            elif event.key == pygame.K_RIGHT:
                snake.change_direction(Vector2(1, 0))
            
    screen.fill((175,215,70))
    fruit.draw_fruit()
    snake.move()
    snake.draw_snake()
    show_score(score)
    
    if fruit.pos == snake.body[0]:
        fruit = Fruit()
        snake.grow()
        velocity += 1
        score += 10
    if snake.body[0].x > 40 or snake.body[0].y > 40 or snake.body[0].x < 0 or snake.body[0].y < 0:
        game_over()
    for block in range(1,len(snake.body)-1):
        if(snake.body[0] == snake.body[block]):
            game_over()
    pygame.display.update()
    clock.tick(10)
    
