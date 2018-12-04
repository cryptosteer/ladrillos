import pygame, os, sys
from pygame.locals import *

# inicializar ventana
pygame.init()
relojFps = pygame.time.Clock()
ventana = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Ladrillos')

# inicializar plataforma

# inicializar bola

# inicializar ladrillos

while True:

    # rellenar el fondo
    ventana.fill(pygame.Color('black'))

    # dibujar elementos

    # control de eventos
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # logica del juego

    # actualizar pantalla
    pygame.display.update()
    relojFps.tick(30)
