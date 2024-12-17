# Menú de pausa o game_over

import pygame
import buttons
import settings
def show_pause_menu(screen):
    font = pygame.font.Font(None, 36)
    text = font.render("PAUSA - Presiona P para continuar", True, (255, 255, 0))
    screen.blit(text, (250, 270))

# Menú de game over
def show_game_over_menu(screen):

    fuente = pygame.font.Font(None, 64)
    texto_game_over = fuente.render("¡Game Over!", True, (255, 0, 0))
    texto_rect = texto_game_over.get_rect(center=(settings.SCREEN_WIDTH // 2, 150))
    screen.blit(texto_game_over, texto_rect)

    boton_reintentar = buttons.Boton(300, 250, 300, 60, "Volver a jugar")
    boton_salir = buttons.Boton(300, 350, 300, 60, "Salir")

    boton_reintentar.dibujar(screen)
    boton_salir.dibujar(screen)

    return boton_reintentar, boton_salir


