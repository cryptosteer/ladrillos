import pygame, os, sys
from pygame.locals import *

# inicializar ventana
pygame.init()
relojFps = pygame.time.Clock()
ventana = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Ladrillos')

# inicializar plataforma
superficie = pygame.image.load('superficie.png').convert_alpha()
superficieRect = superficie.get_rect()
playerY = 540
mousex, mousey = 24, playerY

# inicializar bola

# inicializar ladrillos

while True:

    # rellenar el fondo
    ventana.fill(pygame.Color('black'))

    # dibujar elementos
    ventana.blit(superficie, superficieRect)

    # control de eventos
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == MOUSEMOTION:
            mousex, mousey = event.pos
            if mousex < 800 - 55:
                superficieRect.topleft = (mousex, playerY)
            else:
                superficieRect.topleft = (800 - 55, playerY)

    # logica del juego

    # actualizar pantalla
    pygame.display.update()
    relojFps.tick(30)
