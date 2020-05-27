import pygame
import config
from animal import Animal


# Esta función permite identificar al cuadro/figura que fue seleccionado
# en el tablero en función a las coordenadas enviadas como parámetros (click x,y)
def cuadro_seleccionado(x, y):
    fila = y // config.IMAGE_SIZE
    columna = x // config.IMAGE_SIZE
    index = fila * config.NUM_CUADROS_POR_LADO + columna
    return index


pygame.init()
pygame.display.set_caption('ZOOMemoria')
screen = pygame.display.set_mode((512, 512))
running = True

cuadros_animales = [Animal(i) for i in range(0, config.NUM_CUADROS_TOTAL)]

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

        # Eventos Del Mouse
        if e.type == pygame.MOUSEBUTTONDOWN:
            # En caso de presionar el mouse, se captura la posición donde se hizo el mismo
            # para luego identificar al cuadro/figura que corresponde.
            mouse_x, mouse_y = pygame.mouse.get_pos()
            index = cuadro_seleccionado(mouse_x, mouse_y)
            print(mouse_x, mouse_y, 'Figura ->> ' + str(index))

    screen.fill((255, 255, 255))
    for cuadro in cuadros_animales:
        screen.blit(cuadro.imagen,
                    (cuadro.columna * config.IMAGE_SIZE + config.MARGEN,
                     cuadro.fila * config.IMAGE_SIZE + config.MARGEN))

    pygame.display.flip()
print('Fin')