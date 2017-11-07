import pygame,sys
pygame.init()
import submenu as dm
from pygame.locals import *
ancho =600
alto =800

reloj1=pygame.time.Clock()
volver=pygame.image.load("Imagenes\Volver.jpg")
class Cursor(pygame.Rect):
        def __init__(self):
                pygame.Rect.__init__(self,0,0,1,1)
        def update(self):
                self.left,self.top=pygame.mouse.get_pos()
class Boton (pygame.sprite.Sprite):
        def __init__ (self,imagen1,x=100,y=700):
                self.imagen_=imagen1
                self.rect=self.imagen_.get_rect()
                self.rect.left,self.rect.top=(x,y)
                
cursor1=Cursor()
boton1=Boton(volver)
salir = True
while salir:
        pygame.init()
        for evento in pygame.event.get():
          if evento.type == QUIT:
             pygame.quit()
             sys.exit()
        
        ventana = pygame.display.set_mode((alto,ancho))
        fondo=pygame.image.load("imagenes/Fondo_Creditos.jpg").convert_alpha()
        ventana.blit(fondo, (0, 0))
        pygame.display.flip()
        
        reloj1.tick(20)
        cursor1.update()
        boton1.update(ventana,cursor1)
        pygame.display.update()

  

quit()
        
