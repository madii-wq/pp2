import pygame

pygame.init()

my_music = ["merey-betperde-speed-up_(muzzonas.ru).mp3",
"Kazybek_Kuraiysh_-_Taptym-au_sen_(musmore.com).mp3",
"Kazybek Kuraiysh - Alystama Menen.mp3"]

running = True
has_ever_played = False
queue = 0
pygame.mixer.music.load(my_music[queue])

screen = pygame.display.set_mode((300, 300))
caption = pygame.display.set_caption("PLAYER")
icon = pygame.display.set_icon(pygame.image.load("background_for_music.jpg"))
background = pygame.image.load("background_for_music.jpg")
stoping = False
while running:
    screen.blit(background, (0,0))
    if not pygame.mixer.music.get_busy() and has_ever_played and not stoping:
        queue += 1
        if queue >= len(my_music):
            queue = 0
        pygame.mixer.music.load(my_music[queue])
        pygame.mixer.music.play()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                stoping = not stoping
            if event.key == pygame.K_UP:
                has_ever_played = True
                pygame.mixer.music.play()
            if event.key == pygame.K_LEFT:
                queue += 1
                if queue >= len(my_music):
                   queue = 0
                pygame.mixer.music.load(my_music[queue])
                pygame.mixer.music.play()
            if event.key == pygame.K_RIGHT:
                   queue -= 1
                   if queue < 0:
                      queue = len(my_music) - 1
                   pygame.mixer.music.load(my_music[queue])
                   pygame.mixer.music.play()
    if stoping:
        pygame.mixer.music.pause()
    else:
        pygame.mixer.music.unpause()
    pygame.display.update()

pygame.quit()
