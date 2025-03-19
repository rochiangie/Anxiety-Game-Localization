import pygame
import os
import pyttsx3

# Inicializa pygame
pygame.init()

# Configuración de la pantalla
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Juego de Ansiedad")

# Colores
WHITE = (255, 255, 255)
PASTEL_GREEN = (204, 255, 204)
PASTEL_BLUE = (173, 216, 230)
PASTEL_PINK = (255, 182, 193)
RED = (255, 99, 71)
DARK_RED = (200, 50, 50)
BLACK = (0, 0, 0)

# Variables de configuración
audio_language = "es"
counter = 0
clicker_pressed = False  

# Traducciones
texts = {
    "es": {
        "title": "Juego de Ansiedad",
        "meditation": "Meditación",
        "breathing": "Respiración",
        "mindfulness": "Atención Plena",
        "clicker": "Clickeable",
        "switch_language": "Cambiar Idioma",
        "mindfulness_msg": "Observa a tu alrededor y encuentra 3 cosas nuevas.",
        "meditation_guide": "Cierra los ojos, respira profundo y relaja tu cuerpo poco a poco.",
        "breathing_guide": "Inhala en cuatro tiempos, mantén en cuatro tiempos, exhala en cuatro tiempos."
    },
    "en": {
        "title": "Anxiety Game",
        "meditation": "Meditation",
        "breathing": "Breathing",
        "mindfulness": "Mindfulness",
        "clicker": "Clickable",
        "switch_language": "Switch Language",
        "mindfulness_msg": "Look around and find 3 new things.",
        "meditation_guide": "Close your eyes, take a deep breath and relax your body gradually.",
        "breathing_guide": "Inhale for four counts, hold for four counts, exhale for four counts."
    }
}

# Inicializa pygame mixer para el audio
pygame.mixer.init()
background_music = "C:\\Users\\rocio\\Documents\\juego_ansiedad\\videoplayback.mp3"
if os.path.exists(background_music):
    pygame.mixer.music.load(background_music)
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)
else:
    print("No se encontró la música de fondo.")

# Cargar la imagen de fondo
bg_image_path = "C:\\Users\\rocio\\Documents\\juego_ansiedad\\foto.jpg"
if os.path.exists(bg_image_path):
    background_image = pygame.image.load(bg_image_path)
    background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
else:
    background_image = None
    print("El archivo de fondo no se encontró.")

# Inicializa el motor de texto a voz
def init_speech_engine(language="es"):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    for voice in voices:
        if (language == "es" and "spanish" in voice.name.lower()) or (language == "en" and "english" in voice.name.lower()):
            engine.setProperty('voice', voice.id)
            break
    return engine

engine = init_speech_engine(audio_language)

# Fuente para los textos
font = pygame.font.Font(None, 36)
small_font = pygame.font.Font(None, 28)

def draw_button(text, x, y, width, height, color, small=False):
    """Dibuja un botón con texto centrado."""
    pygame.draw.rect(screen, color, (x, y, width, height))
    text_surface = small_font.render(text, True, BLACK) if small else font.render(text, True, BLACK)
    screen.blit(text_surface, (x + (width - text_surface.get_width()) // 2, y + (height - text_surface.get_height()) // 2))

def speak(text):
    """Reproduce un mensaje de texto a voz."""
    engine.say(text)
    engine.runAndWait()

def toggle_language():
    """Cambia entre español e inglés."""
    global audio_language, engine
    audio_language = "en" if audio_language == "es" else "es"
    engine = init_speech_engine(audio_language)
    pygame.display.set_caption(texts[audio_language]["title"])
    speak("Language changed to English" if audio_language == "en" else "Idioma cambiado a español")

def mindfulness_game():
    """Muestra un mensaje de mindfulness."""
    show_message(texts[audio_language]["mindfulness"], texts[audio_language]["mindfulness_msg"])

def show_message(title, message):
    """Muestra un cuadro de mensaje por unos segundos."""
    message_window = pygame.Surface((500, 200))
    message_window.fill(WHITE)
    title_surface = font.render(title, True, BLACK)
    message_surface = font.render(message, True, BLACK)
    message_window.blit(title_surface, (20, 20))
    message_window.blit(message_surface, (20, 80))
    screen.blit(message_window, (SCREEN_WIDTH // 2 - 250, SCREEN_HEIGHT // 2 - 100))
    pygame.display.flip()
    pygame.time.delay(3000)

# Bucle principal
running = True
while running:
    # Dibujar la imagen de fondo
    if background_image:
        screen.blit(background_image, (0, 0))
    else:
        screen.fill(WHITE)
    
    clicker_color = DARK_RED if clicker_pressed else RED
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_l:
                toggle_language()

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos
            if 300 <= mouse_x <= 500:
                if 150 <= mouse_y <= 200:
                    speak(texts[audio_language]["meditation_guide"])
                elif 250 <= mouse_y <= 300:
                    speak(texts[audio_language]["breathing_guide"])
                elif 350 <= mouse_y <= 400:
                    mindfulness_game()
            elif 50 <= mouse_x <= 250 and 500 <= mouse_y <= 550:
                toggle_language()
            elif 600 <= mouse_x <= 750 and 500 <= mouse_y <= 550:
                clicker_pressed = True  
                counter += 1  

        if event.type == pygame.MOUSEBUTTONUP:
            clicker_pressed = False  

    draw_button(texts[audio_language]["meditation"], 300, 150, 200, 50, PASTEL_GREEN)
    draw_button(texts[audio_language]["breathing"], 300, 250, 200, 50, PASTEL_BLUE)
    draw_button(texts[audio_language]["mindfulness"], 300, 350, 200, 50, PASTEL_PINK)
    draw_button(texts[audio_language]["switch_language"], 50, 500, 200, 50, PASTEL_BLUE, small=True)
    draw_button(texts[audio_language]["clicker"], 600, 500, 150, 50, clicker_color)
    draw_button(f"Clics: {counter}", 600, 550, 150, 40, WHITE, small=True)
    
    pygame.display.flip()

pygame.quit()
