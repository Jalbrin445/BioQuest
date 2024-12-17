# Archivo para las características del enemigo


import pygame
import random

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("assets\\images\\roca2.png")
        self.image = pygame.transform.smoothscale(self.image, (50, 40))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, 800 - self.rect.width)  # Ubicación aleatoria en el eje x
        self.rect.y = random.randint(-100, -40)  # Aparece por encima de la pantalla

    def move(self):
        self.rect.y += 4  # Velocidad de movimiento vertical hacia abajo
        if self.rect.top > 600:  # Si sale de la pantalla
            self.reset_position()

    def reset_position(self):
        self.rect.x = random.randint(0, 800 - self.rect.width)
        self.rect.y = random.randint(-100, -40)  # Reinicia la posición por encima de la pantalla

    def check_collision(self, player):
        return self.rect.colliderect(player.rect)
    
    def draw(self, screen):
        screen.blit(self.image, self.rect)