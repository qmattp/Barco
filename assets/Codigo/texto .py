import pygame

# Inicializar pygame
pygame.init()

# Crear una ventana de 640x480 pixels
screen = pygame.display.set_mode((640, 480))

# Establecer el título de la ventana
pygame.display.set_caption("Texto Pixeleado")

# Fuente descargada 
font = pygame.font.Font("Retro Gaming.ttf", 36)

# Texto
text = "Hola, mundo!"

# Dibujar el texto en la ventana
text_surface = font.render(text, True, (255, 255, 255))
screen.blit(text_surface, (100, 100))

# Actualizar la ventana
pygame.display.flip()

# CICLO
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# Cerrar pygame
pygame.quit()