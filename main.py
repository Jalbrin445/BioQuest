# Archivo principal del proyecto
import sys
import pygame
import random
import settings 
import player
from enemy import Enemy 
import questions_manager
from menu import show_pause_menu, show_game_over_menu
import buttons
import music
import background_play

pygame.init() # iniciación de pygame
screen = pygame.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT)) #Configuración de la pantalla
pygame.display.set_caption("BioQuest") # Configuración del nombre del videojuego.

# Iniciación de variables a utilizar en este archivo
player1 = player.Player()
enemies = [Enemy() for _ in range(12)]  # Genera 12 enemigos (Rocas)
game_running = True
paused = False
game_over = False

# Estado inicial del juego
states = "menu"  

# Respuestas del usuario
user_answer = ""

# temporizador para preguntas
last_question_time = pygame.time.get_ticks()

# Bucle principal
clock = pygame.time.Clock()
game_running = True

estado_anterior = states # Para inicializar la variable estado_anterior

while game_running:

    current_time = pygame.time.get_ticks()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False

        if states == "menu":

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if buttons.home_button.clicado(event.pos):
                    states = "playing"  # Cambia a estado de juego
                elif buttons.exit_button.clicado(event.pos):
                    game_running = False  # Salir del juego

        elif states == "pregunta" and event.type == pygame.KEYDOWN:
            pygame.mixer.music.stop()
            if event.key == pygame.K_RETURN:
                # Comprobar la respuesta: 
                if user_answer.lower() == questions_manager.current_question["answer"].lower(): 
                    print("¡Respuesta correcta!") # si la respuesta es correcta

                else:
                    print("Respuesta incorrecta, pierdes una vida.") # si la respuesta no es correcta
                    player1.take_damage() 
                    if player1.lives <= 0: # si las vidas llegan a 0 entonces perderá el jugador
                        states = "game_over"
                user_answer = "" 
                states = "playing"
                last_question_time = current_time

            elif event.key == pygame.K_BACKSPACE: # para quitar letras de la respuestas que da el jugador
                user_answer = user_answer[:-1]
            else:
                user_answer += event.unicode
        
        
        elif states == "game_over":
        
            boton_reintentar, boton_salir = show_game_over_menu(screen) # Dibuja los botones en pantalla
            # Esto me ayudará a saber que opción elijo y que se debe ejecutar de acuerdo al botón cliclado (Volver a jugar/ Salir del juego)
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if boton_reintentar.clicado(event.pos):
                        pygame.mixer.music.stop() # pausa a la música
                        # Reiniciar el juego
                        player1.reset()  # Reinicia al jugador (vidas y posición)
                        enemies = [Enemy() for _ in range(12)]  # Generar nuevos enemigos
                        states = "menu"  # Volver al menú principal

                    elif boton_salir.clicado(event.pos):
                        pygame.mixer.music.stop()
                        game_running = False  # Salir del juego

        # Menú de salida y pausa usando letras
        elif event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_p:
                paused = not paused
            elif event.key == pygame.K_q or game_over:
                game_running = False

    # Dibujar pantalla según el estado
    if states == "menu": # Estado menú
        screen.fill(settings.MENU_BACKGROUND_COLOR)
        buttons.DibujarTexto.dibujar_texto("BioQuest", buttons.fuente, (255, 255, 255), screen, settings.SCREEN_WIDTH // 2, 100)
        buttons.DibujarTexto.dibujar_texto("Presione P para pausar el juego y Q", buttons.fuente, (255, 255, 255), screen, 450, 500)
        buttons.DibujarTexto.dibujar_texto("para salir del juego", buttons.fuente, (255, 255, 255), screen, 450, 540)
        buttons.DibujarTexto.dibujar_texto("Responde todas las preguntas en", buttons.fuente, (255, 255, 255), screen, 450, 400)
        buttons.DibujarTexto.dibujar_texto("Mayúscula y sin tildes", buttons.fuente, (255, 255, 255), screen, 450, 440)
        buttons.DibujarTexto.dibujar_texto("Controles:", buttons.fuentem, (255, 255, 255), screen, 750, 100)
        buttons.DibujarTexto.dibujar_texto("W: Arriba, S: Abajo", buttons.fuentem, (255, 255, 255), screen, 750, 120)
        buttons.DibujarTexto.dibujar_texto("A: Izquierda, D: Derecha", buttons.fuentem, (255, 255, 255), screen, 750, 140)
        buttons.home_button.dibujar(screen)
        buttons.exit_button.dibujar(screen)
    
    # Estado pregunta
    elif states == "pregunta":

        buttons.DibujarTexto.dibujar_texto(questions_manager.current_question["question"], buttons.fuente, settings.TEXT_COLOR, screen, 450, 200)
        pygame.draw.rect(screen, settings.PICTURE_COLOR, settings.TEXT_BOX)
        texto_superficie = buttons.fuente.render(user_answer, True, settings.TEXT_COLOR)
        screen.blit(texto_superficie, (settings.TEXT_BOX.x + 10, settings.TEXT_BOX.y + 10))

    # Estado jugando
    elif states == "playing":
        
        # Desplazar el fondo hacia abajo
        background_play.fondo_y += 1 # velocidad del fondo
        if background_play.fondo_y >= settings.SCREEN_HEIGHT:
            background_play.fondo_y = 0 # Reiniciar el fondo
        #Dibujar el fondo
        screen.blit(background_play.fondo, (0, background_play.fondo_y))
        screen.blit(background_play.fondo, (0, background_play.fondo_y - settings.SCREEN_HEIGHT))
        
        # Teclas presionadas para mover al jugador
        keys = pygame.key.get_pressed()
        #movimiento del jugador
        dx = (keys[pygame.K_d] - keys[pygame.K_a]) * settings.PLAYER_SPEED 
        dy = (keys[pygame.K_s] - keys[pygame.K_w]) * settings.PLAYER_SPEED

        # Codigo ejecutable si no esta en el estado de pausa o game over
        if not paused and not states == "game_over":
            
            player1.move(dx, dy)
            player1.draw(screen)

            player.Player.dibujar_vidas(screen, player1) # Dibujar vidas dependiendo la cantidad

            # Actualiza y dibuja enemigos
            for enemy in enemies:
                enemy.move()
                enemy.draw(screen)
                if enemy.check_collision(player1):  # Verifica colisión con el jugador
                    music.sonido_colision.play()
                    player1.take_damage()
                    enemy.reset_position()  # Reinicia la posición del enemigo

                    
                    if player1.lives <= 0:
                        
                        states = "game_over"

            # intervalo de tiempo entre preguntas
            if current_time - last_question_time >= settings.WAITING_TIME:
                questions_manager.current_question = random.choice(questions_manager.questions)
                last_question_time = current_time
                states = "pregunta"
        
        elif paused: # entra a este estado de pausa mediante la letra P
            show_pause_menu(screen)


        # Estado de game_over, se genera un menú en pantalla con dos opciones Volver a jugar/Salir del juego
        elif states == "game_over":
            show_game_over_menu(screen)
        
            
        # Estructura condicional para cambiar musica de acuerdo al estado       
        if states != estado_anterior:
            if states == "menu":
                music.cambiar_musica(music.musica_inicio)
            elif states == "playing":
                music.cambiar_musica(music.musica_juego)
            elif states == "game_over":
                music.cambiar_musica(music.musica_gameover, bucle=False)  
            estado_anterior = states
        
          
    pygame.display.flip()
    clock.tick(settings.FPS)

pygame.quit()
sys.exit()