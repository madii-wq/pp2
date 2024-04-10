import pygame
import sys
import random

pygame.init()

# Define colors
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# Define display dimensions
dis_width = 600
dis_height = 400

# Set up the display and caption
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake')

# Set up the clock
clock = pygame.time.Clock()

# Define block size and snake speed
snake_block = 10
snake_speed = 15
accelerator = 1.0
# Set up fonts
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

# Set the score, width, time limit
fruit_width = 1
limit_score = 100
timer = snake_speed*fruit_width*6
# Function to display score
def Your_score(score):
    value = score_font.render("Your Score: " + str(score), True, red)
    dis.blit(value, [0, 0])
def Your_level(score):
    value = score_font.render("level: " + str(int(score/20)), True, red)
    dis.blit(value, [400, 0])
# Function to draw the snake
def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])
def fruit_time(timer):
    if timer == 0:
        return True
    return False
# Function to display messages
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])

# Main game loop
def gameLoop():
    game_over = False
    game_close = False

    x1 = dis_width / 2
    y1 = dis_height / 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1
    
    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
    direction = None
    
    while not game_over:
        #init our globals
        global fruit_width
        global timer
        global snake_speed
        global accelerator
        # Check if the game is over
        while game_close:
            dis.fill(blue)
            message("You Lost! Press C-Play Again or Q-Quit", red)
            Your_score(Length_of_snake - 1)
            Your_level(Length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                # Change direction based on arrow key presses
                if event.key == pygame.K_LEFT and direction != "Right":
                    x1_change = -snake_block
                    y1_change = 0
                    direction = "Left"
                elif event.key == pygame.K_RIGHT and direction != "Left":
                    x1_change = snake_block
                    y1_change = 0
                    direction = "Right"
                elif event.key == pygame.K_UP and direction != "Down":
                    y1_change = -snake_block
                    x1_change = 0
                    direction = "Up"
                elif event.key == pygame.K_DOWN and direction != "Up":
                    y1_change = snake_block
                    x1_change = 0
                    direction = "Down"
        # Check if snake hits boundaries
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        #checking if our food spawns in snake
        for pos in snake_List:
            if (pos[0] == foodx or pos[0] == foodx + fruit_width*snake_block - snake_block) and (pos[1] == foody or pos[1] == foody + fruit_width*snake_block- snake_block):
               foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
               foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
        # Move the snake
        x1 += x1_change
        y1 += y1_change
        dis.fill(blue)
        # Draw the food
        pygame.draw.rect(dis, green, [foodx, foody, fruit_width*snake_block, fruit_width*snake_block])
        # Add snake's head position to snake list
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        # Remove the last segment of the snake if its length exceeds Length_of_snake
        print(len(snake_List))
        if len(snake_List) > Length_of_snake:
            del snake_List[0]
        #collision with itself
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        # Draw the snake
        our_snake(snake_block, snake_List)
        # Display score and level
        Your_score(Length_of_snake - 1)
        Your_level(Length_of_snake - 1)

        pygame.display.update()
        timer -= 1
        # Generate new food when snake eats the current food
        if (x1 == foodx or x1 == foodx + fruit_width*snake_block - snake_block) and (y1 == foody or y1 == foody + fruit_width*snake_block- snake_block):
           foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
           foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
           Length_of_snake += fruit_width
           timer = snake_speed*fruit_width*6
           accelerator += 0.005
           fruit_width = random.randint(1,2)
        #timer 6 second
        if fruit_time(timer) :
           foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
           foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
           timer = snake_speed*fruit_width*6
           fruit_width = random.randint(1,2)
        #ticks
        clock.tick(snake_speed*accelerator)
        # Check if the score limit is reached
        if limit_score == Length_of_snake - 1:
            game_close = True

    pygame.quit()
    quit()

gameLoop()
