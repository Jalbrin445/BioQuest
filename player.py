# Características del jugador (mover, cargar imagen, bajar vidas, dibujar el jugador en pantalla y restaurar estado).

import os
import pygame
import settings
import utils 

# Dibujar vidas del jugador
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
HEART_IMAGE = utils.load_image(os.path.join(BASE_DIR, "assets\\images\\heart.png"))
HEART_IMAGE = pygame.transform.scale(HEART_IMAGE, (30, 30))

class Player(pygame.sprite.Sprite): 
    def __init__(self):
        super().__init__()
        self.image = utils.load_image(os.path.join(BASE_DIR,"assets\\images\\avion2.png")).convert_alpha()
        self.image = pygame.transform.smoothscale(self.image, (50, 40))
        self.rect = self.image.get_rect(center=(400, 500))
        self.lives = 3 

    def move(self, dx, dy): # Movimiento del jugador
        self.rect.x += dx
        self.rect.y += dy
        self.rect.x = max(0, min(self.rect.x, 800 - self.rect.width))
        self.rect.y = max(0, min(self.rect.y, 600 - self.rect.height))

    def take_damage(self): # Función que baja las vidas del jugador.
        self.lives -= 1

    def draw(self, screen): # Dibujar al jugador en pantalla
        screen.blit(self.image, self.rect)

    # Dibujar vida
    def dibujar_vidas(screen, player_v):

        for i in range(player_v.lives):
            # Posiciona las vidas en la esquina superior derecha
            x = settings.SCREEN_WIDTH - (i + 1) * 40  # Espaciado entre íconos de vida
            y = 10  # Margen superior
            screen.blit(HEART_IMAGE, (x, y))
    
    # Reiniciar el estado del jugador al inicial
    def reset(self):
        self.lives = 3 # Restablecer las vidas
        self.rect.center = (settings.SCREEN_WIDTH // 2, settings.SCREEN_HEIGHT - 50) # Posición inicial
        


