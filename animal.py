import config

'''
 Creamos un diccionario i.e. {'mapache.png':0,'gato.png':0, 'zorro.png':0, ...}
 Inicialmente el value será 0 para todos los key en el diccionario.
 Permitirá contar cuántas veces un animal fue desbloqueado, es decir si
 value -> 0  No fue desbloqueado, 1  Fue desbloqueado una vez, 2  Fue desbloqueado dos veces y su pareja fue encontrada
'''
contador_animales = {}
for img in config.ASSET_FILES:
    contador_animales[img] = 0
# Sugar syntax equivalente
# contador_animales = dict((img, 0) for img in config.ASSET_FILES)

'''
    El diccionario contador de animales permite saber qué animales encontraron su pareja, 
gracias a ello esta función obtiene a los animales que aún no encontraron su pareja por lo que están disponibles
'''


def animales_disponibles():
    keys = []
    for key, value in contador_animales.items():
        if value < 2:
            keys.append(key)
    return keys
    # Sugar syntax equivalente
    # return [key for key, value in contador_animales.items() if value < 2]


import os
import random
import pygame


class Animal:
    '''
    En el constructor se define atributos para identificar la posición de la figura en función al index
     0   1   2   3
     4   5   6   7
     8   9  10  11
     12 13 14 15

    Adicionalmente permite definir los atributos de la figura del animal
    para luego establecer en ellos la carga de la imagen frontal  y la creación de la imagen reversa
    '''

    def __init__(self, index):
        # identificamos la columna y fila del cuadro en el tablero de acuerdo al index
        self.index = index
        self.fila = index // config.NUM_CUADROS_POR_LADO
        self.columna = index % config.NUM_CUADROS_POR_LADO

        # Obtenemos un animal al azar que no haya sido desbloqueado
        self.nombre = random.choice(animales_disponibles())

        # Indicamos que el animal fue seleccionado
        contador_animales[self.nombre] += 1

        # Cargamos la imagen del animal y establecemos sus dimensiones
        self.imagen = pygame.image.load(os.path.join(config.ASSET_DIR, self.nombre))
        self.imagen = pygame.transform.scale(self.imagen, (
        config.IMAGE_SIZE - 2 * config.MARGEN, config.IMAGE_SIZE - 2 * config.MARGEN))

        # Copiamos la imagen para conservar sus atributos, pero pintamos el cuadro de color plomo
        self.imagen_reversa = self.imagen.copy()
        self.imagen_reversa.fill((200, 200, 200))

        # Esta propiedad bandera ayudará a identificar si el animal fue desbloqueado
        self.desbloqueado = False
