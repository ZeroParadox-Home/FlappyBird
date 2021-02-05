# NABEGHEHA.COM
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - -#
# Github       : https://github.com/NABEGHEHACOM/FlappyBird/
# Youtube      : https://youtu.be/oKPov7IJEjU
# Social Media : https://nabegheha.com/socials/
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - -#
# Python Version : 3.9
# Pygmae Version : 2.0.0
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - -#


import pygame
import sys

# ALL VARIABLE
display_width = 576
display_height = 1024
floor_x = 0
background_image = pygame.transform.scale2x(pygame.image.load('assets/img/bg2.png'))
floor_image = pygame.transform.scale2x(pygame.image.load('assets/img/floor.png'))

# GAME DISPLAY
main_screen = pygame.display.set_mode((display_width, display_height))

# START PYGAME MODULES
pygame.init()

# GAME TIMER
clock = pygame.time.Clock()

# GAME LOGIC
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # END PYGAME MODULES
            pygame.quit()
            # TERMINATE PROGRAM
            sys.exit()
    # DISPLAY BG2.PNG        
    main_screen.blit(background_image, (0, 0))
    # DISPLAY FLOOR.PNG
    floor_x -= 1
    main_screen.blit(floor_image, (floor_x, 900))
    main_screen.blit(floor_image, (floor_x + 576, 900))
    if floor_x <= -576:
        floor_x = 0
    
    pygame.display.update()
    # SET GAME SPEED
    clock.tick(90)
