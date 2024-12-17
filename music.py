# Contenedor de la música


import pygame
import os

pygame.init()
pygame.mixer.init() # Carga de sonidos

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Función para cambiar musica
def cambiar_musica(nueva_cancion, bucle=True):
    pygame.mixer.music.stop()
    pygame.mixer.music.load(os.path.join(BASE_DIR, nueva_cancion))
    pygame.mixer.music.play(-1 if bucle else 0)

# Musica
musica_inicio = "assets\\sounds\\A_Binary_Collision.mp3" # sonido menú de inicio de juego
musica_juego = "assets\\sounds\\pantera_rosa.mp3" # sonido en estado playing
# sonido_colision = pygame.mixer.Sound("\\Users\\Juan\\Desktop\\AVBioquest\\Prototipo6_UsoPygameAndSys\\Game_Over_Sound_Effect.mp3") # sonido de colisión
musica_gameover = "assets\\sounds\\Game_Over_Sound_Effect.mp3" # sonido game over
sonido_colision = pygame.mixer.Sound(os.path.join(BASE_DIR, "assets\\sounds\\collision.mp3"))

