# Fondo móvil del estado jugando (playing)

import pygame
import os
import settings
import utils

# fondo
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
fondo = utils.load_image(os.path.join(BASE_DIR,"\\Users\\Juan\\Desktop\\AVBioquest\\Prototipo7_UsoPygameAndSys\\images\\cielo.png"))
fondo = pygame.transform.scale(fondo, (settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT*2))

#posición inicial del fondo
fondo_y = 0