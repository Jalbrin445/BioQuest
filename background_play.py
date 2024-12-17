# Fondo móvil del estado jugando (playing)

import pygame
import settings
import utils

# fondo
fondo = utils.load_image("\\Users\\Juan\\Desktop\\AVBioquest\\Prototipo7_UsoPygameAndSys\\images\\cielo.png")
fondo = pygame.transform.scale(fondo, (settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT*2))

#posición inicial del fondo
fondo_y = 0