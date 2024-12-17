# Menú de inicio de juego.


import pygame
import settings
# Caracterísitcas de los botones usados en este videojuego.
pygame.init()

fuente = pygame.font.Font(None, 48) # Texto más grande
fuentem = pygame.font.Font(None, 28) # Texto menos grande

class DibujarTexto:
    def dibujar_texto(texto, fuente, color, superficie, x, y):
        texto_superficie = fuente.render(texto, True, color)
        texto_rect = texto_superficie.get_rect(center=(x, y))
        superficie.blit(texto_superficie, texto_rect)

class Boton:
    def __init__(self, x, y, ancho, alto, texto):
        self.rect = pygame.Rect(x, y, ancho, alto)
        self.texto = texto

    def dibujar(self, superficie):
        pygame.draw.rect(superficie, settings.COLOR_BOTON, self.rect)
        DibujarTexto.dibujar_texto(self.texto, fuente, settings.TEXT_COLOR, superficie, self.rect.centerx, self.rect.centery)

    def clicado(self, pos):
        return self.rect.collidepoint(pos)

# Botones del menú
home_button = Boton(300, 200, 300, 60, "Iniciar Juego")
exit_button = Boton(300, 290, 300, 60, "Salir")