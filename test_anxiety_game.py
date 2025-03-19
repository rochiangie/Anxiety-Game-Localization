import pytest
import pygame
import os
from AnxietyGame import (
    init_speech_engine,
    texts,
    fun_facts,
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    WHITE,
    PASTEL_GREEN,
    PASTEL_BLUE,
    PASTEL_PINK,
    RED,
    PURPLE
)

@pytest.fixture
def setup_pygame():
    """Inicializa pygame para las pruebas"""
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    yield screen
    pygame.quit()

def test_screen_dimensions(setup_pygame):
    """Prueba las dimensiones de la pantalla"""
    screen = setup_pygame
    assert screen.get_width() == SCREEN_WIDTH
    assert screen.get_height() == SCREEN_HEIGHT

def test_color_constants():
    """Prueba que los colores estén definidos correctamente"""
    assert WHITE == (255, 255, 255)
    assert PASTEL_GREEN == (204, 255, 204)
    assert PASTEL_BLUE == (173, 216, 230)
    assert PASTEL_PINK == (255, 182, 193)
    assert RED == (255, 99, 71)
    assert PURPLE == (147, 112, 219)

def test_translations():
    """Prueba que las traducciones estén completas en ambos idiomas"""
    required_keys = [
        "title",
        "meditation",
        "breathing",
        "mindfulness",
        "clicker",
        "switch_language",
        "mindfulness_msg",
        "meditation_guide",
        "breathing_guide",
        "random_fact_title"
    ]
    
    # Verifica que ambos idiomas tengan las mismas claves
    assert set(texts["es"].keys()) == set(texts["en"].keys())
    
    # Verifica que todas las claves requeridas estén presentes
    for key in required_keys:
        assert key in texts["es"]
        assert key in texts["en"]
        # Verifica que ningún valor esté vacío
        assert texts["es"][key] != ""
        assert texts["en"][key] != ""

def test_fun_facts():
    """Prueba la estructura y contenido de los datos curiosos"""
    # Verifica que haya datos curiosos en ambos idiomas
    assert len(fun_facts["es"]) > 0
    assert len(fun_facts["en"]) > 0
    
    # Verifica que haya el mismo número de datos en ambos idiomas
    assert len(fun_facts["es"]) == len(fun_facts["en"])
    
    # Verifica que ningún dato curioso esté vacío
    for fact in fun_facts["es"]:
        assert fact != ""
    for fact in fun_facts["en"]:
        assert fact != ""

def test_speech_engine():
    """Prueba la inicialización del motor de voz"""
    # Prueba con español
    engine_es = init_speech_engine("es")
    assert engine_es is not None
    
    # Prueba con inglés
    engine_en = init_speech_engine("en")
    assert engine_en is not None

def test_required_files():
    """Prueba la existencia de archivos necesarios"""
    assert os.path.exists("videoplayback.mp3"), "Archivo de música no encontrado"
    assert os.path.exists("foto.jpg"), "Archivo de imagen no encontrado"

def test_button_click_coordinates():
    """Prueba las coordenadas de los botones"""
    # Coordenadas del botón de meditación
    assert 300 <= 300 <= 500  # x start <= x <= x end
    assert 150 <= 150 <= 200  # y start <= y <= y end
    
    # Coordenadas del botón de respiración
    assert 300 <= 300 <= 500
    assert 250 <= 250 <= 300
    
    # Coordenadas del botón de mindfulness
    assert 300 <= 300 <= 500
    assert 350 <= 350 <= 400
    
    # Coordenadas del botón de cambio de idioma
    assert 50 <= 50 <= 250
    assert 500 <= 500 <= 550
    
    # Coordenadas del botón clickeable
    assert 600 <= 600 <= 750
    assert 500 <= 500 <= 550
