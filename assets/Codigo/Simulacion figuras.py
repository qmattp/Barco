import pygame
import sys
import random
import math

# Inicializar Pygame
pygame.init()

# Definir colores
BLANCO = (255, 255, 255)
ROJO = (255, 0, 0)
AMARILLO = (255, 255, 0)  # Color amarillo
AZUL = (0, 0, 255)

# Dimensiones de la pantalla
ANCHO = 800
ALTO = 600

# Crear la pantalla
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Simulación Barco")

# Posición inicial del círculo
x = ANCHO // 2
y = ALTO // 2
radio = 30
velocidad = 2

# Variables para la animación
destino_x = x
destino_y = y
en_movimiento = False

# Lista para almacenar los cuadros
cuadrados = []
NUM_CUADRADOS = 10
CUADRADO_TAM = 50

# Crear cuadrados al azar
for _ in range(NUM_CUADRADOS):
    cuadrado_x = random.randint(0, ANCHO - CUADRADO_TAM)
    cuadrado_y = random.randint(0, ALTO - CUADRADO_TAM)
    cuadrados.append(pygame.Rect(cuadrado_x, cuadrado_y, CUADRADO_TAM, CUADRADO_TAM))

# Variable para almacenar la posición del triángulo
triángulo = None

# Bucle principal
terminado = False
while not terminado:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            terminado = True
        elif evento.type == pygame.MOUSEBUTTONDOWN:  # Capturar clic del ratón
            # Obtener la posición del clic
            destino_x, destino_y = evento.pos
            en_movimiento = True
            # Crear un triángulo en la posición del clic
            triángulo = [(destino_x, destino_y), 
                         (destino_x - 20, destino_y + 40), 
                         (destino_x + 20, destino_y + 40)]

    # Lógica del movimiento del círculo
    if en_movimiento:
        # Calcular distancia
        distancia = math.sqrt((destino_x - x) ** 2 + (destino_y - y) ** 2)
        if distancia > velocidad:  # Mover solo si no ha llegado al destino
            # Dirección
            direccion_x = (destino_x - x) / distancia
            direccion_y = (destino_y - y) / distancia

            # Movimiento del círculo
            nuevo_x = x + direccion_x * velocidad
            nuevo_y = y + direccion_y * velocidad

            # Comprobación de colisiones
            colision = False
            for cuadrado in cuadrados:
                if cuadrado.collidepoint(nuevo_x, nuevo_y):
                    colision = True
                    break

            if colision:
                # Respuesta a la colisión
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
    pantalla.fill(BLANCO)

    # Dibujar cuadros
    for cuadrado in cuadrados:
        pygame.draw.rect(pantalla, AZUL, cuadrado)

    # Dibujar el triángulo (solo el último clic)
    if triángulo:
        pygame.draw.polygon(pantalla, AMARILLO, triángulo)

    # Dibujar el círculo (en rojo)
    pygame.draw.circle(pantalla, ROJO, (int(x), int(y)), radio)

    # Actualizar pantalla
    pygame.display.flip()

    # Controlar la tasa de frames
    pygame.time.Clock().tick(60)

# Salir de Pygame
pygame.quit()
sys.exit()