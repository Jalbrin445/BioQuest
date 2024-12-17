# Almacen de preguntas/respuestas y de la variable pregunta actual que toma cualquier pregunta del diccionario questions

import random

# esto es para generar las preguntas
questions = [
    {"question": "¿Cuál es la fórmula del agua?", "answer": "H2O"},
    {"question": "¿Cuántos planetas hay en el sistema solar?", "answer": "8"},
    {"question": "¿Qué planeta es conocido como el planeta rojo?", "answer": "MARTE"},
    {"question": "¿Qué es 5 + 3?", "answer": "8"},
    {"question": "¿Cuál es el órgano más grande del cuerpo humano?", "answer": "LA PIEL"},
    {"question": "¿Proceso por el cual las plantas producen su alimento?", "answer": "FOTOSINTESIS"},
    {"question": "Gas más abundante en la atmósfera terrestre", "answer": "NITROGENO"},
    {"question": "¿Qué tipo de animal es un delfín?", "answer": "MAMIFERO"},
    {"question": "¿Cuánto es 8 x 7?", "answer": "56"},
    {"question": "¿Qué nombre tiene un polígono de cinco lados?", "answer": "PENTAGONO"},
    {"question": "¿Qué es mayor: 3/4 o 2/3?", "answer": "3/4"},
    {"question": "¿Cuál es el resultado de 12 al cuadrado?", "answer": "144"},
    {"question": "Valor que se repite más veces en un conjunto de datos", "answer": "MODA"},
    {"question": "¿En qué país se encuentra la Torre Eiffel?", "answer": "FRANCIA"},
    {"question": "¿Cuál es la capital de Francia?", "answer": "PARIS"},
    {"question": "¿Qué océano es el más grande del mundo?", "answer": "OCEANO PACIFICO"},
    {"question": "¿En qué año llegó Cristóbal Colón a América?", "answer": "1492"},
    {"question": "¿Qué país tiene forma de bota?", "answer": "ITALIA"},
    {"question": "¿Cuántos colores tiene el arcoíris?", "answer": "7"},
    {"question": "¿Qué instrumento musical tiene 88 teclas?", "answer": "PIANO"},
    {"question": "¿Cómo se llama la ciencia que estudia los mapas?", "answer": "CARTOGRAFIA"},
    {"question": "¿Qué gas inhalamos para respirar?", "answer": "OXIGENO"},
    {"question": "¿Cuál es el animal terrestre más rápido del mundo?", "answer": "GUEPARDO"},
    {"question": "¿Qué es más rápido: la luz o el sonido?", "answer": "LA LUZ"},
    {"question": "¿Quién desarrolló la teoría de la relatividad?", "answer": "ALBERT EINSTEIN"},
    {"question": "¿Qué parte del ordenador es conocida como el cerebro?", "answer": "EL PROCESADOR"},
    {"question": "¿Cuál es el metal más ligero?", "answer": "LITIO"},
]

current_question = random.choice(questions)
