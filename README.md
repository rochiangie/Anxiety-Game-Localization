# Juego de Ansiedad / Anxiety Game

Un juego interactivo bilingüe (Español/Inglés) diseñado para ayudar a manejar la ansiedad a través de diferentes técnicas de relajación.

An interactive bilingual game (Spanish/English) designed to help manage anxiety through different relaxation techniques.

## Características / Features

- 🎯 **Meditación / Meditation**: Guía de meditación con instrucciones por voz
- 🫁 **Respiración / Breathing**: Ejercicios de respiración controlada
- 👀 **Atención Plena / Mindfulness**: Ejercicios de observación consciente
- 🔄 **Cambio de Idioma / Language Switch**: Soporte completo para español e inglés
- 🎵 **Música de Fondo / Background Music**: Música relajante de fondo
- 🎮 **Botón Clickeable / Clickable Button**: Elemento interactivo con datos curiosos

## Requisitos / Requirements

- Python 3.x
- Pygame
- pyttsx3
- pytest (para pruebas / for testing)

## Archivos Necesarios / Required Files

- `videoplayback.mp3`: Música de fondo / Background music
- `foto.jpg`: Imagen de fondo / Background image

## Cómo Ejecutar / How to Run

1. Asegúrate de tener Python instalado / Make sure you have Python installed
2. Instala las dependencias / Install dependencies:
   ```
   pip install pygame pyttsx3 pytest
   ```
3. Ejecuta el juego / Run the game:
   ```
   python AnxietyGame.py
   ```

## Pruebas / Testing

Para ejecutar las pruebas unitarias / To run unit tests:
```
pytest test_anxiety_game.py -v
```

Las pruebas verifican / Tests verify:
- Dimensiones de pantalla / Screen dimensions
- Constantes de colores / Color constants
- Traducciones / Translations
- Datos curiosos / Fun facts
- Motor de voz / Speech engine
- Archivos requeridos / Required files
- Coordenadas de botones / Button coordinates

## Controles / Controls

- **Click Izquierdo / Left Click**: Interactuar con botones / Interact with buttons
- **Tecla L / L Key**: Cambiar idioma / Switch language
- **ESC**: Salir del juego / Exit game
