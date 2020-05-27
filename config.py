import os

# Definimos el tamaño de la ventana y las imágenes
SCREEN_SIZE = 512
IMAGE_SIZE = 128

# Indicamos el número total de cuadros y el número de cuadros a cada lado
NUM_CUADROS_TOTAL = 16
NUM_CUADROS_POR_LADO = 4

# Definimos el tamaño del margen
MARGEN = 4

# Obtenemos la lista de las imágenes almacenadas en mi_proyecto/assets/animals
ASSET_DIR = 'assets/animals'
ASSET_FILES = []
for img in os.listdir(ASSET_DIR):
    if img[-3:].lower() == 'png':
        ASSET_FILES.append(img)

# También podemos obtener las imágenes de una formas más sugar syntax
# ASSET_FILES = [img for img in os.listdir(ASSET_DIR) if img[-3:].lower() == 'png']
