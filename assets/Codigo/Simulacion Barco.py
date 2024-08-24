import pygame
import sys
import random
import math

# Inicializar Pygame
pygame.init()

# Definir colores
BLANCO = (255, 255, 255)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)

# Dimensiones de la pantalla
ANCHO = 1000
ALTO = 800

# Pantalla
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Simulación Barco")
fuente = pygame.font.Font(None, 60)
fuente2 = pygame.font.Font(None, 30)
fuente3 = pygame.font.Font(None, 20)

# Cargar imágenes
barco = pygame.image.load('Barquiño.png')  
Pato = pygame.image.load('Patito_de_Barrio.png')  
Fondo_de_Pantalla = pygame.image.load('Oceano2.png') 
Imagen_Bandera = pygame.image.load('Bandera.png') 
# Posición inicial del barco
x = ANCHO // 2
y = ALTO // 2
velocidad = 2

# Variables para la animación
destino_x = x
destino_y = y
en_movimiento = False
#Musica
sonido = pygame.mixer.Sound('Musiquita.wav')
sonido.play()
# Lista para almacenar los cuadros
cuadrados = []
NUM_CUADRADOS = 10

# Variable para almacenar la posición del clic
Bandera = None

CUADRADO_TAM = 50
#Texto en si
text = "Pulsa espacio para jugar"
mensaje = fuente.render(text, 1, (BLANCO))
pantalla.blit(mensaje, (100, 200))
Version = "V.1.O.Beta"
Version2 = fuente3.render(Version, 1, (255,255,255))
pantalla.blit(Version2, (1060, 630))
texto = "Fin del juego ganaste"
Fin_del_game_papa = fuente.render(texto, 1, (BLANCO))

# Dibujar Patos
for _ in range(NUM_CUADRADOS):
    cuadrado_x = random.randint(0, ANCHO - CUADRADO_TAM)
    cuadrado_y = random.randint(0, ALTO - CUADRADO_TAM)
    cuadrados.append(pygame.Rect(cuadrado_x, cuadrado_y, CUADRADO_TAM, CUADRADO_TAM))

# BUCLE PRINCIPAL NO TOCAR POR FAVOR (esto saca mas errores que windows 8)
terminado = False
while not terminado:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            terminado = True
        elif evento.type == pygame.MOUSEBUTTONDOWN:  # Capturar clic del ratón
            destino_x, destino_y = evento.pos
            en_movimiento = True
            Bandera = evento.pos
    # Lógica del Barquiño mani
    if en_movimiento:
        # distancia del barco
        distancia = math.sqrt((destino_x - x) ** 2 + (destino_y - y) ** 2)
        if distancia > velocidad:  # Mover solo si no ha llegado al destino
            # dirrecion
            direccion_x = (destino_x - x) / distancia
            direccion_y = (destino_y - y) / distancia

            # Barco movimiento
            nuevo_x = x + direccion_x * velocidad
            nuevo_y = y + direccion_y * velocidad

            # COmbpobacion 
            colision = False
            for cuadrado in cuadrados:
                if cuadrado.collidepoint(nuevo_x, nuevo_y):
                    colision = True
                    break

            if colision:
                # Colisison
                direccion_x = random.uniform(-1, 1)
                direccion_y = random.uniform(-1, 1)
                nuevo_x = x + direccion_x * velocidad
                nuevo_y = y + direccion_y * velocidad

            x, y = nuevo_x, nuevo_y

        else:
            # Ha llegado al destino
            x, y = destino_x, destino_y
            en_movimiento = False

    # Limpiar pantalla
    pantalla.blit(Fondo_de_Pantalla,[0,0])

    
    for cuadrado in cuadrados:
        pantalla.blit(Pato, cuadrado)
    
    # Dibujar la forma en la posición del clic
    if Bandera:
        pantalla.blit(Imagen_Bandera, Bandera)
        
    # Dibujar el barco
    pantalla.blit(barco, (x, y))

    # Actualizar pantalla
    pygame.display.flip()

    # Controlar la tasa de frames
    pygame.time.Clock().tick(60)

# Salir de Pygame
pygame.quit()
sys.exit()
