# Contenedor de la música


import pygame
import os

pygame.init()
pygame.mixer.init() # Carga de sonidos

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Función para cambiar musica
def change_music(new_song, bucle=True):
    pygame.mixer.music.stop()
    pygame.mixer.music.load(new_song)
    pygame.mixer.music.play(-1 if bucle else 0)

# Musica
music_start = os.path.join(BASE_DIR,"assets\\sounds\\A_Binary_Collision.mp3") # sonido menú de inicio de juego
music_game = os.path.join(BASE_DIR,"assets\\sounds\\pantera_rosa.mp3") # sonido en el estado playing
# sonido_colision = pygame.mixer.Sound("\\Users\\Juan\\Desktop\\AVBioquest\\Prototipo6_UsoPygameAndSys\\Game_Over_Sound_Effect.mp3") # sonido de colisión
music_gameover = os.path.join(BASE_DIR,"assets\\sounds\\Game_Over_Sound_Effect.mp3") # sonido game over
sonido_colision = pygame.mixer.Sound(os.path.join(BASE_DIR, "assets\\sounds\\collision.mp3"))

