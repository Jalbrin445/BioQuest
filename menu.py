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

    font = pygame.font.Font(None, 64)
    text_game_over = font.render("¡Game Over!", True, (255, 0, 0))
    text_rect = text_game_over.get_rect(center=(settings.SCREEN_WIDTH // 2, 150))
    screen.blit(text_game_over, text_rect)

    retry_button = buttons.Boton(300, 250, 300, 60, "Volver a jugar")
    exit_button = buttons.Boton(300, 350, 300, 60, "Salir")

    retry_button.dibujar(screen)
    exit_button.dibujar(screen)

    return retry_button, exit_button


