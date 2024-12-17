# **BIOQUEST** *(Pilotea y responde)*

## **Descripción del Proyecto**
    Es un videojuego donde el jugador 
    debe evitar enemigos y responder preguntas de 
    matemáticas, física, biología y entre otras ramas de la ciencia, 
    este proyecto fue desarrollado con las siguientes librerías: **Pygam**, **Sys** y **Random**.

## **Características principales**

1. Sistema de vidas del jugador.

2. Enemigos dinámicos.

3. Menús interactivos:

    - Menú de inicio de juego.
    - Menú de pausa.
    - Menú de game over (Volver a jugar/salir del juego).

4. Sistema de preguntas aleatorias basado en ciencia.

5. Modularidad para mantener el código organizado.

6. Música dinamica de acuerdo al estado del juego.

## **Requsitos del sistema**

- **Python 3.10** o superior.

- Pygame instalado: `pip install pygame` **(En la consola)**.

## **Instalación y Ejecución**

1. Clona el repositorio: 
    ```bash
        `git clone https://github.com/Jalbrin445/BioQuest.git`

2. Instala las dependencias: 
    ```bash
    `pip install pygame`

3. Ejecuta el juego: 
    python main.py


## **Estructura del Proyecto** (descripción de los módulos).

BioQuest
- |
- |--> main.py (Archivo principal del juego).
- |--> settings.py (Configuraciones globales del juego (no todas se encuentran aquí, hay algunas que están en otros archivos)).
- |--> player.py (Clase del jugador (vidas, movimiento, dibujo)).
- |--> enemy.py (Clase de los enemigos (movimiento y colisiones)).
- |--> questions_manager.py (Módulo para gestionar preguntas y respuestas).
- |--> buttons.py (Gestión y dibujo de botones interactivos).
- |--> menu.py (Funciones para los menús (pausa y game over)).
- |--> music.py (Sistema para cambiar música según estados).
- |--> background_play.py (Manejo del fondo animado).
- |--> assets/ (Recursos visuales y sonoros)
- |   |--> images/
- |   |--> sounds/
- |--> README.md (Este archivo)

## **Visualización del proyecto**

- Menu de inicio de juego: assets\Presentation\estado_menu_iniciodejuego.png
- Estado playing o jugando: assets\Presentation\estado_jugando.png
- Estado de Game over (Volver a jugar/salir del juego): assets\Presentation\estado_game_over.png
- Estado preguntas: assets\Presentation\estado_preguntas.png

## **Próximas mejoras**

- Añadir nuevos niveles de dificultad.
- Añadir dificultad progresiva a lo largo de un nivel.
- Añadir más enemigos.
- Añadir sistema de disparos al jugador.

## **Controles del juego**

- W: mover hacia arriba.
- S: Mover hacia abajo.
- A: Mover hacia la izquierda.
- D: Mover hacia la derecha.
- P: Pausar el juego.
- Q: Salir del juego.

## Autor.

- Nombre: Juan Albrin Meza Guzmán.

- GitHub: https://github.com/Jalbrin445

- Correo: mezaguzmanjuanalbrin@gmail.com

## Licencia

    Este proyecto está bajo la licencia MIT.
