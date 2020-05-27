import pygame
import config
from animal import Animal
from time import sleep


def cuadro_seleccionado(x, y):
    fila = y // config.IMAGE_SIZE
    columna = x // config.IMAGE_SIZE
    index = fila * config.NUM_CUADROS_POR_LADO + columna
    return index


msg_pareja = pygame.image.load('assets/mensaje-par.png')
msg_ganaste = pygame.image.load('assets/mensaje-ganaste.png')

pygame.init()
pygame.display.set_caption('ZOOMemoria')
screen = pygame.display.set_mode((512, 512))
running = True

cuadros_animales = [Animal(i) for i in range(0, config.NUM_CUADROS_TOTAL)]
cuadros_animales_selecionados = []

# GAME LOOP
while running:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_ESCAPE:
                running = False
        if e.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            index = cuadro_seleccionado(mouse_x, mouse_y)

            if index not in cuadros_animales_selecionados:
                cuadros_animales_selecionados.append(index)
            if len(cuadros_animales_selecionados) > 2:
                cuadros_animales_selecionados = cuadros_animales_selecionados[1:]
    screen.fill((255, 255, 255))

    total_desbloqueados = 0
    for i, cuadro in enumerate(cuadros_animales):
        imagen_a_mostrar = cuadro.imagen if i in cuadros_animales_selecionados else cuadro.imagen_reversa
        if not cuadro.desbloqueado:
            screen.blit(imagen_a_mostrar, (
                cuadro.columna * config.IMAGE_SIZE + config.MARGEN, cuadro.fila * config.IMAGE_SIZE + config.MARGEN))
        else:
            total_desbloqueados += 1
    pygame.display.flip()

    if len(cuadros_animales_selecionados) == 2:
        idx1, idx2 = cuadros_animales_selecionados
        if cuadros_animales[idx1].nombre == cuadros_animales[idx2].nombre:
            cuadros_animales[idx1].desbloqueado = True
            cuadros_animales[idx2].desbloqueado = True
            cuadros_animales_selecionados = []
            sleep(0.35)
            screen.blit(msg_pareja, (0, 0))
            pygame.display.flip()
            sleep(0.35)

    if total_desbloqueados == len(cuadros_animales):
        running = False
        screen.blit(msg_ganaste, (0, 0))
        pygame.display.flip()
        sleep(10.5)

print('Fin')
