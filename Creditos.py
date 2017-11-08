import pygame,sys
import submenu as dm
from pygame.locals import *
ancho =600
alto =800

pygame.init()
ventana = pygame.display.set_mode((alto,ancho))
fondo = pygame.image.load("imagenes/Fondo_Creditos.jpg").convert_alpha()


ventana.blit(fondo, (0, 0))
pygame.display.flip()

while True:
        # Posibles entradas del teclado y mouse
        for event in pygame.event.get():
                mouse=pygame.mouse.get_pressed()
                if mouse[0] == 1:
                       from main import*

     
