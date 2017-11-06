import pygame,sys
from pygame.locals import *

ancho =600
alto =800

def Creditos ():
    ventana = pygame.display.set_mode((alto,ancho))
    Fondo=pygame.image.load("imagenes/Fondo_Creditos.jpg").convert_alpha()
    ventana.blit(Fondo,(0,0))
    print """
                    Creadores:
            Federico Salvatierra
            Joan Teich
            Santiago Martinez Vila
            Mariana Moline
            Francisco Laperuta

    """
    
    
