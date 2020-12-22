# NABEGHEHA.COM
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - -#
# Github       : https://github.com/NABEGHEHACOM/FlappyBird/
# Youtube      : https://youtu.be/_ct9S6b73Ak
# Social Media : https://nabegheha.com/socials/
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - -#
# Python Version : 3.9
# Pygmae Version : 2.0.0
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - -#


import pygame
import sys

pygame.init()


main_screen = pygame.display.set_mode((576, 1024))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
