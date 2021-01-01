# NABEGHEHA.COM
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - -#
# Github       : https://github.com/NABEGHEHACOM/FlappyBird/
# Youtube      : https://youtu.be/9ru0S4hXeNM
# Social Media : https://nabegheha.com/socials/
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - -#
# Python Version : 3.9
# Pygmae Version : 2.0.0
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - -#


import pygame
import sys

pygame.init()


main_screen = pygame.display.set_mode((576, 1024))
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()        
    clock.tick(90)    
    
