import pygame
import os
import pyttsx3
import random

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
random_fact = ""
show_fact = False
fact_start_time = 0

# Datos curiosos
fun_facts = [
    "Los delfines tienen nombres únicos y se llaman entre ellos.",
    "La miel nunca caduca.",
    "Los pulpos tienen tres corazones.",
    "Las huellas dactilares de los koalas son casi indistinguibles de las humanas.",
    "Las nutrias marinas se toman de las manos mientras duermen para no separarse.",
    "Las vacas tienen mejores amigas y se estresan cuando están separadas.",
    "Los caracoles pueden dormir hasta tres años seguidos.",
    "Los tiburones han existido por más de 400 millones de años, antes que los dinosaurios."
]

# Inicializa pygame mixer para el audio
pygame.mixer.init()
background_music = "videoplayback.mp3"
if os.path.exists(background_music):
    pygame.mixer.music.load(background_music)
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)
else:
    print("No se encontró la música de fondo.")

# Cargar la imagen de fondo
bg_image_path = "foto.jpg"
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
    """Reproduce un mensaje de texto a voz y silencia la música de fondo temporalmente."""
    pygame.mixer.music.set_volume(0)  
    engine.say(text)
    engine.runAndWait()
    pygame.mixer.music.set_volume(0.5)

def toggle_language():
    """Cambia entre español e inglés."""
    global audio_language, engine
    audio_language = "en" if audio_language == "es" else "es"
    engine = init_speech_engine(audio_language)
    pygame.display.set_caption("Anxiety Game" if audio_language == "en" else "Juego de Ansiedad")
    speak("Language changed to English" if audio_language == "en" else "Idioma cambiado a español")

def show_fact_window():
    """Muestra la ventana del dato curioso."""
    global show_fact, fact_start_time
    fact_window = pygame.Surface((500, 250))
    fact_window.fill(WHITE)

    title_surface = font.render("Dato Curioso", True, BLACK)
    fact_window.blit(title_surface, (20, 20))

    words = random_fact.split()
    lines = []
    current_line = ""

    for word in words:
        test_line = current_line + " " + word if current_line else word
        if small_font.size(test_line)[0] < 460:
            current_line = test_line
        else:
            lines.append(current_line)
            current_line = word
    lines.append(current_line)

    y_offset = 60
    for line in lines:
        message_surface = small_font.render(line, True, BLACK)
        fact_window.blit(message_surface, (20, y_offset))
        y_offset += 30

    screen.blit(fact_window, (SCREEN_WIDTH // 2 - 250, SCREEN_HEIGHT // 2 - 125))
    pygame.display.flip()

# Bucle principal
running = True
while running:
    screen.blit(background_image, (0, 0)) if background_image else screen.fill(WHITE)

    # Dibujar botones
    draw_button("Meditación", 300, 150, 200, 50, PASTEL_GREEN)
    draw_button("Respiración", 300, 250, 200, 50, PASTEL_BLUE)
    draw_button("Atención Plena", 300, 350, 200, 50, PASTEL_PINK)
    draw_button("Cambiar Idioma", 50, 500, 200, 50, PASTEL_BLUE, small=True)
    draw_button("Clickeable", 600, 500, 150, 50, DARK_RED if clicker_pressed else RED)
    draw_button(f"Clics: {counter}", 600, 550, 150, 40, WHITE, small=True)

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
                    speak("Cierra los ojos, respira profundo y relaja tu cuerpo poco a poco.")
                elif 250 <= mouse_y <= 300:
                    speak("Inhala en cuatro tiempos, mantén en cuatro tiempos, exhala en cuatro tiempos.")
                elif 350 <= mouse_y <= 400:
                    speak("Observa a tu alrededor y encuentra 3 cosas nuevas.")
            elif 50 <= mouse_x <= 250 and 500 <= mouse_y <= 550:
                toggle_language()
            elif 600 <= mouse_x <= 750 and 500 <= mouse_y <= 550:
                clicker_pressed = True  
                counter += 1  
                if random.randint(1, 3) == 1:  
                    random_fact = random.choice(fun_facts)
                    show_fact = True
                    fact_start_time = pygame.time.get_ticks()

        if event.type == pygame.MOUSEBUTTONUP:
            clicker_pressed = False  

    if show_fact and pygame.time.get_ticks() - fact_start_time > 3000:
        show_fact = False  

    if show_fact:
        show_fact_window()

    pygame.display.flip()

pygame.quit()
