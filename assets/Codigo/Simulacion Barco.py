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
ALTO = 750

# Pantalla
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Simulación Barco")


# Cargar imágenes
energia = pygame.image.load("Energia 1.png")
barco = pygame.image.load('Barquiño.png')  
Fondo_de_Pantalla = pygame.image.load('Oceano2.png') 
Imagen_Bandera = pygame.image.load('Bandera.png') 
Energia = [
    pygame.image.load("Energia 1.png"),
    pygame.image.load("Energia 2.png"),
    pygame.image.load("Energia 3.png"),
    pygame.image.load("Energia 4.png"),
    pygame.image.load("Energia descargada.png"),
]
Pato = [
    pygame.image.load("Patito_de_Barrio.png"),
    pygame.image.load("Pato feli.png"),
    pygame.image.load("Patito_de_Barrio.png"),
    pygame.image.load("Pato feli.png")
]
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
#Coordenadas
Coor1=150
Coor2=350
CUADRADO_TAM = 50
#Texto en si
font = pygame.font.Font("Retro Gaming.ttf", 36)
text = "Clik para donde quieres que valla"
# Establecer la velocidad de la animación en segundos por frame
velocidad1 = 1
velocidad2 = 1
# Variables para controlar la animación
indic = 0
indice = 0
tiempo_transcurrido2= 0
tiempo_transcurrido1= 0
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
            Coor1 = 3000
            Coor2= 3000
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
    
    
    # Incrementar el tiempo transcurrido
    tiempo_transcurrido1 += 1 / 60
    tiempo_transcurrido2 += 1 / 60
    # Cambiar de sprite según la velocidad Enrgia
    if tiempo_transcurrido1 >= velocidad1:
        tiempo_transcurrido1 = 0
        indic += 1
        if indic >= len(Energia):
            indic = 0
    # Cambiar de sprite según la velocidad Pato
    
    if tiempo_transcurrido2 >= velocidad1:
        tiempo_transcurrido2 = 0
        indice += 1
        if indice >= len(Pato):
            indice = 0
    
    
    
    for cuadrado in cuadrados:
        pantalla.blit(Pato[indice],cuadrado)
    
    # Dibujar la forma en la posición del clic
    if Bandera:
        pantalla.blit(Imagen_Bandera, Bandera)
    #Dibujar Energia 
    pantalla.blit(Energia[indic],(0,0))
    # Dibujar el texto en la ventana
    text_surface = font.render(text, True, (255, 255, 255))
    pantalla.blit(text_surface, (Coor1, Coor2))    
    # Dibujar el barco
    pantalla.blit(barco, (x, y))
    #Dibujar energia
    #pantalla.blit(energia, (0, 0))    
    # Actualizar pantalla
    pygame.display.flip()

    # Controlar la tasa de frames
    pygame.time.Clock().tick(60)

# Salir de Pygame
pygame.quit()
sys.exit()
