import pygame
import sys
import random
import time
from pygame.locals import *

# Initializing
pygame.init()

# Setting up FPS
FPS = 60
FramePerSec = pygame.time.Clock()

# Creating colors
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Other Variables for use in the program
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
SCORE = 0

# Setting up Fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)

background = pygame.image.load("lab8/photos/AnimatedStreet.png")
pygame.mixer.music.load("lab8/photos/Voice-003.wav")
# Create a white screen
DISPLAYSURF = pygame.display.set_mode((400, 600))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")

#CLasses of objects
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("lab8/photos/Enemy.png")
        self.rect = self.image.get_rect()
        # (random.randint(40, SCREEN_WIDTH - 40), 0)
        self.spawn = random.randint(1,3)
        if self.spawn == 2:
               self.rect.center = (205,0)
        elif self.spawn == 3:
               self.rect.center = (330,0)
        else:
               self.rect.center = (80,0)

    def move(self):
        global SCORE
        self.rect.move_ip(0, SPEED + random.randint(0,3))
        if self.rect.top > 600:
            self.decide = random.randint(1,3)
            SCORE += 1
            self.rect.top = 0
            if self.decide == 2:
               self.rect.center = (205,0)
            elif self.decide == 3:
               self.rect.center = (330,0)
            else:
               self.rect.center = (80,0)
        
    

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("lab8/photos/Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-7, 0)
        if self.rect.right < SCREEN_WIDTH:
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(7, 0)


class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("lab8/photos/coin.png").convert_alpha()  # Load coin image
        self.image = pygame.transform.scale(self.image, (20,20))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(50, 350)
        self.rect.y = 0  # Start coin from top of the screen

    def update(self):
        self.rect.y += SPEED  # Move the coin down the screen

    def draw(self, surface):
        surface.blit(self.image, self.rect)
class superCoin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("lab8/photos/bonus coin.png").convert_alpha()  # Load coin image
        self.image = pygame.transform.scale(self.image, (30,30))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(50, 350)
        self.rect.y = 0  # Start coin from top of the screen
    def update(self):
        self.rect.y += SPEED  # Move the coin down the screen

    def draw(self, surface):
        surface.blit(self.image, self.rect)
class Background():
      def __init__(self):
            self.bgimage = pygame.image.load("lab8/photos/AnimatedStreet.png")
            self.rectBGimg = self.bgimage.get_rect()
 
            self.bgY1 = 0
            self.bgX1 = 0
 
            self.bgY2 = -self.rectBGimg.height
            self.bgX2 = 0
 
            self.moving_speed = 3
         
      def update(self):
        self.bgY1 += self.moving_speed
        self.bgY2 += self.moving_speed
        if self.bgY1 >= self.rectBGimg.height:
            self.bgY1 = -self.rectBGimg.height
        if self.bgY2 >= self.rectBGimg.height:
            self.bgY2 = -self.rectBGimg.height
             
      def render(self):
         DISPLAYSURF.blit(self.bgimage, (self.bgX1, self.bgY1))
         DISPLAYSURF.blit(self.bgimage, (self.bgX2, self.bgY2))
        
# Setting up Sprites
P1 = Player()
E1 = Enemy()
back_ground = Background()

# Creating Sprites Groups
enemies = pygame.sprite.Group()
enemies.add(E1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)

# Creating Coins Sprite Group
coins_group = pygame.sprite.Group()
bonus_coin_group = pygame.sprite.Group()
# Adding a new User event
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

# Game Loop
while True:
    for event in pygame.event.get():
        if event.type == INC_SPEED:
            SPEED += 0.1
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
            
            
    back_ground.update()
    back_ground.render()
    
    scores = font_small.render(str(SCORE), True, BLACK)
    DISPLAYSURF.blit(scores, (10, 10))
    if not pygame.mixer.music.get_busy():
       pygame.mixer.music.play()
    
    # Generate new coins randomly
    if random.randint(0, 100) < 2:  # Adjust probability as needed
        new_coin = Coin()
        coins_group.add(new_coin)
    if random.randint(0,100) < 1:
        bonus_coin = superCoin()
        bonus_coin_group.add(bonus_coin)
    bonus_coin_group.update()
    bonus_coin_group.draw(DISPLAYSURF)
    coins_group.update()  # Update the positions of coins
    coins_group.draw(DISPLAYSURF)  # Draw coins on the screen
     
    # Remove coins that have gone off-screen
    for coin in coins_group:
        if coin.rect.y > SCREEN_HEIGHT:
            coin.kill()

    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.move()

    # Handle collision between player and coins
    if pygame.sprite.spritecollide(P1,coins_group,True):
        SCORE += 1
        
        pygame.mixer.Sound('lab8/photos/coin_music.wav').play()
    if pygame.sprite.spritecollide(P1, bonus_coin_group, True):
        SCORE += 3
        
        pygame.mixer.Sound('lab8/photos/bonus coin_misic.wav').play()
    collected_coins = pygame.sprite.spritecollide(P1, coins_group, True)
        
    # To be run if collision occurs between Player and Enemy
    if pygame.sprite.spritecollideany(P1, enemies):
        pygame.mixer.music.stop()
        pygame.mixer.Sound('lab8/photos/Voice-004.wav').play()
        time.sleep(0.5)
        DISPLAYSURF.fill(RED)
        DISPLAYSURF.blit(game_over, (30, 250))
        pygame.display.update()
        for entity in all_sprites:
            entity.kill()
        time.sleep(2)
        pygame.quit()
        sys.exit()

    pygame.display.update()
    FramePerSec.tick(FPS)
