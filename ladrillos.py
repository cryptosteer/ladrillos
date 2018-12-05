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
ladrillo = pygame.image.load('ladrillo.png')
ladrillos = []
for y in range(5):
    ladrilloY = (y * 24) + 100
    for x in range(10):
        ladrilloX = (x * 31) + 245
        ladrillos.append(Rect(ladrilloX, ladrilloY, ladrillo.get_width(), ladrillo.get_height()))

while True:

    # rellenar el fondo
    ventana.fill(pygame.Color('black'))

    # dibujar elementos
    ventana.blit(superficie, superficieRect)
    ventana.blit(bola, bolaRect)
    for l in ladrillos:
        ventana.blit(ladrillo, l)

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
    # bola golpea superficie
    if bolaRect.colliderect(superficieRect):
        by = playerY - 8
        vy *= -1
    # golpea limite izquierdo
    if bx <= 0:
        bx = 0
        vx *= -1
    # golpea limite derecho
    if bx >= 800 - 8:
        bx = 800 - 8
        vx *= -1
    # golpea limite superior
    if by <= 0:
        by = 0
        vy *= -1
    # golpea limite inferior
    if by >= 600 - 8:
        bolaServida = False
        bx, by = (24, 200)
        bolaRect.topleft = (bx, by)

    # actualizar pantalla
    pygame.display.update()
    relojFps.tick(30)
