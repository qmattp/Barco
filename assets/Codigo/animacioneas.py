import pygame
import sys

# Inicializar Pygame
pygame.init()

# Crear una ventana de 640x480
screen = pygame.display.set_mode((640, 480))

# Establecer el título de la ventana
pygame.display.set_caption("Animación de sprites")

# Cargar las imágenes de la animación
imagenes = [
    pygame.image.load("Patito_de_Barrio.png"),
    pygame.image.load("Patito enojao.png"),
    pygame.image.load("Patito_de_Barrio.png"),
    pygame.image.load("Patito enojao.png")
]

# Establecer la velocidad de la animación en segundos por frame
velocidad = 0.1

# Variables para controlar la animación
indice = 0
tiempo_transcurrido = 0

# Bucle principal
while True:
    # Manejar eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Dibujar el fondo
    screen.fill((255, 255, 255))

    # Incrementar el tiempo transcurrido
    tiempo_transcurrido += 1 / 60

    # Cambiar de sprite según la velocidad
    if tiempo_transcurrido >= velocidad:
        tiempo_transcurrido = 0
        indice += 1
        if indice >= len(imagenes):
            indice = 0

    # Dibujar la imagen actual de la animación
    screen.blit(imagenes[indice], (100, 100))

    # Actualizar la pantalla
    pygame.display.flip()
    pygame.time.Clock().tick(60)
