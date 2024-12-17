"""Almacen de variables usadas en el juego (No todas están definidas aquí, hay algunas que por facilidad están definidas
otros archivos.py)"""
import pygame

pygame.init()

SCREEN_WIDTH = 900 #ancho de la ventana
SCREEN_HEIGHT = 600 #altura de la ventana
FPS = 60 #número de fotogramas por segundo
PLAYER_SPEED = 7 #velocidad del jugador
INITIAL_LIVES = 3
BACKGROUND_COLOR = ((0, 100, 200)) #Color de fondo para cuando se este jugando.

# Configuración de colores Para el menú de inicio:
MENU_BACKGROUND_COLOR = (0, 150, 200) # Azul fondo del menu inicio de juego
COLOR_BOTON = (255, 255, 0)  # Amarillo
TEXT_COLOR = (0, 0, 0) # Negro
PICTURE_COLOR = (255, 255, 255) # Blanco 

TEXT_BOX = pygame.Rect(300, 250, 300, 60)#cuadro de texto

WAITING_TIME = 27000 # tiempo de espera entre preguntas

