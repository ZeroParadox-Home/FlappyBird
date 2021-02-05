  
# NABEGHEHA.COM
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - -#
# Github       : https://github.com/NABEGHEHACOM/FlappyBird/
# Youtube      : https://youtu.be/gRDykifQR08
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
background_image = pygame.image.load('assets/img/bg2.png')
background_image = pygame.transform.scale2x(background_image)

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
    main_screen.blit(background_image, (0, 0))
    pygame.display.update()
    # SET GAME SPEED
    clock.tick(90)
