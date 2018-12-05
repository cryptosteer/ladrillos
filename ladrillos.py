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
bolaServida = False
bx, by = (24, 200)
vx, vy = (6, 6)
bola = pygame.image.load('bola.png')
bolaRect = bola.get_rect()
bolaRect.topleft = (bx, by)

# inicializar ladrillos

while True:

    # rellenar el fondo
    ventana.fill(pygame.Color('black'))

    # dibujar elementos
    ventana.blit(superficie, superficieRect)
    ventana.blit(bola, bolaRect)

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
        elif event.type == MOUSEBUTTONUP:
            if not bolaServida:
                bolaServida = True

    # logica del juego
    # movimiento de la bola
    if bolaServida:
        bx += vx
        by += vy
        bolaRect.topleft = (bx, by)

    # actualizar pantalla
    pygame.display.update()
    relojFps.tick(30)
