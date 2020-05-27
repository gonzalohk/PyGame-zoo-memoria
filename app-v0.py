import pygame

# Inicializamos Pygame
pygame.init()
# Asignamos un título al juego
pygame.display.set_caption('ZOOMemoria')
# Establecemos la dimensión de la patalla (512px,512px)
screen = pygame.display.set_mode((512, 512))
# La variable running nos ayudara a crear un ciclo infinito hasta que el juego termine
running = True

# GAME LOOP
while running:
    # Recolectamos todos los eventos que pudieron lanzarse
    for e in pygame.event.get():
        # Eventos Generales
        if e.type == pygame.QUIT:
            # En caso de cerrarse la ventana se lanza el evento pygame.QUIT
            running = False

        # Eventos Del Teclado
        if e.type == pygame.KEYDOWN:
            # Cualquier tecla presionada sera escuchada
            if e.key == pygame.K_ESCAPE:
                # Si la tecla ESC fue presionada se lanza el evento pygame.K_ESCAPE:
                running = False

# En caso de terminar el GAME LOOP mostramos un mensaje en la cosola
print('Fin')
