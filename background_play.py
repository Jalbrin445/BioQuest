# Fondo móvil del estado jugando (playing)

import pygame
import os
import settings
import utils

# fondo
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
background = utils.load_image(os.path.join(BASE_DIR,"assets\\images\\cielo.png"))
background = pygame.transform.scale(background, (settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT*2))
#posición inicial del fondo
background_y = 0
