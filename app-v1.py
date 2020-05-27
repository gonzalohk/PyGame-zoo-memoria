import pygame
import config
from animal import Animal

pygame.init()
pygame.display.set_caption('ZOOMemoria')
screen = pygame.display.set_mode((512, 512))
running = True

# Definimos un array donde se instancian 16 objetos Animal ordenados de forma aleatoria
cuadros_animales = []
for i in range(config.NUM_CUADROS_TOTAL):
    cuadros_animales.append(Animal(i))
# Sugar Syntax equivalente
# cuadros_animales = [Animal(i) for i in range(0, config.NUM_CUADROS_TOTAL)]

# GAME LOOP
while running:
    for e in pygame.event.get():
        # Eventos Generales
        if e.type == pygame.QUIT:
            running = False

        # Eventos Del Teclado
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_ESCAPE:
                running = False

    # Rellenamos la ventada de color blanco
    screen.fill((255, 255, 255))

    # Dibujamos las 16 figuras/cuadros de animales en el tablero, pero requiere actualizarse para verse
    for cuadro in cuadros_animales:
        screen.blit(cuadro.imagen,
                    (cuadro.columna * config.IMAGE_SIZE + config.MARGEN,
                     cuadro.fila * config.IMAGE_SIZE + config.MARGEN))

    # Actualiza toda la superficie de la ventana, en nuestro caso el tablero
    pygame.display.flip()
print('Fin')
