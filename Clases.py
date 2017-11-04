import pygame,sys
from pygame.locals import *
from random import randint   # numero aleatorios

ancho =600
alto =800
listaEnemigo = []
####  PLAYER  #####
class nave (pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.nave = pygame.image.load("imagenes/nave2.png")
        self.rect = self.nave.get_rect()
        self.rect.centerx = ancho/2
        self.rect.centery= alto-250
    

        self.listaDisparo = [ ]
        self.vida= True
        self.velocidad= 20  # velocidad nave
    def movimientoDerecha(self):
        self.rect.right += self.velocidad
        self.__movimiento()
    def movimientoIzquierda (self):
        self.rect.left -=self.velocidad
        self.__movimiento()
    def __movimiento(self):
        if self.vida == True:
            if self.rect.left<=0:
                self.rect.left=0
            elif self.rect.right>801:
               self.rect.right = 800
            

    def disparar(self, x, y):
        mibala= Disparo(x,y, "imagenes/bala.png", True)
        self.listaDisparo.append(mibala)

    def dibujar (self, superficie):
        superficie.blit(self.nave, self.rect)
########    DISPARO    ########
class Disparo(pygame.sprite.Sprite):
    def  __init__(self , posx , posy, ruta, personaje):
        pygame.sprite.Sprite.__init__(self)
        self.bala = pygame.image.load(ruta)
        self.rect = self.bala.get_rect()
        self.velocidadDisparo = 1
        self.rect.top = posy
        self.rect.left = posx
        self.disparoPersonaje = personaje
        
    def trayectoria (self ):
        if self.disparoPersonaje == True:
           self .rect.top = self.rect.top - self.velocidadDisparo
        else:
             self .rect.top = self.rect.top + self.velocidadDisparo

    def dibujar (self, superficie):
        superficie.blit(self.bala, self.rect)
######### ENEMIGO ######
        
class Enemigo(pygame.sprite.Sprite):
    def  __init__(self , posx , posy, distancia , imagenUno, imagenDos):
        pygame.sprite.Sprite.__init__(self)
        self.marcianoA = pygame.image.load(imagenUno)
        self.marcianoB = pygame.image.load(imagenDos)
        self.listaImagenes= [self.marcianoA,self.marcianoB]
        self.posImagen=0
        
        self.imagenEnemigo = self.listaImagenes[self.posImagen]
    
        self.rect = self.imagenEnemigo.get_rect()
        self.listaDisparo = []
        self.velocidad = 10
        self.rect.top = posy
        self.rect.left = posx
        self.rangoDisparo= 3
        self.tiempoCambio = 1
  
        self.derecha= True   # movimiento del Enemigo
        self.contador = 0
        self.maxdescenso = self.rect.top+ 20

        self.limiteDerecha= posx + distancia
        self.limiteIzquierda= posy - distancia
         
    def dibujar (self, superficie):
        self.imagenEnemigo = self.listaImagenes[self.posImagen]
        superficie.blit(self.imagenEnemigo, self.rect)

    def comportamiento (self, tiempo):
        self.__movimientos()
        
        self.__ataque()
        if self.tiempoCambio == tiempo:
          self.posImagen +=1
          self.tiempoCambio +=1

          if self.posImagen >len (self.listaImagen)-1:
              self.posImagen=0

    def  __movimientos (self):
            if self.contador < 3:
                self.__movimientoLateral()
            else:
                self.__descenso()
                
    def __descenso (self):
       if self.maxdescenso == self.rect.top:
          self.contador=0
          self.maxdescenso= self.rect.top+ 40
       else:
            self.rect.top +=1
            
    def __movimientoLateral (self):
        if self.derecha == True:
             self.rect.left = self.rect.left + self.velocidad
             if self.rect.left >self.limiteDerecha:
                 self.derecha = False
                 self.contador +=1                
        else:
           self.rect.left = self.rect.left - self.velocidad
        if self.rect.left <  self.limiteIzquierda:
            self.derecha = True
        
    def __ataque(self):
       if (randint (0,100)<self.rangoDisparo):
           self.__disparo()
    def __disparo(self):
        x,y = self.rect.center
        piedra = Disparo(x,y,"Imagenes/piedra.png", False)
        self.listaDisparo.append(piedra)
    
def cargarEnemigos():
   Marciano = Enemigo (100,100,40,"imagenes/marcianoA.png","imagenes/marcianoB.png")
   listaEnemigo.append(Marciano)

    
def Juego():
 pygame.init()
ventana = pygame.display.set_mode((alto,ancho))
pygame.display.set_caption("Prototipo 1")
Fondo=pygame.image.load("imagenes/fondo1.jpg").convert_alpha()
Jugador= nave()
cargarEnemigos()
inGame = True
reloj = pygame.time.Clock()
while True :
 
    reloj.tick(100)    #velocidad de frame por segundo
    tiempo = pygame.time.get_ticks() /1000
    
    for evento in pygame.event.get():
          if evento.type == QUIT:
             pygame.quit()
             sys.exit()
          if inGame == True:
              if evento.type == pygame.KEYDOWN:   # comandos de movimiento de la nave
                  if evento.key ==K_LEFT:
                   Jugador.movimientoIzquierda()
                  elif evento.key == K_RIGHT:
                   Jugador.movimientoDerecha()
                  elif evento.key == K_SPACE:   # tecla para disparar 
                    x,y = Jugador.rect.center
                    Jugador.disparar(x,y)
                    
    ventana.blit(Fondo,(0,0))
    Jugador.dibujar(ventana)

    if len (Jugador.listaDisparo)>0:  # eliminar bala de la ventana cuando llege a su recorrido
        for x in Jugador.listaDisparo:
             x.dibujar(ventana)
             x.trayectoria()
             if x.rect.top<10:
                Jugador.listaDisparo.remove(x)
    if len (listaEnemigo)>0:
         for Marciano in listaEnemigo:
             Marciano.comportamiento(tiempo)
             Marciano.dibujar(ventana)
             
             if len (Marciano.listaDisparo)>0:  # eliminar bala de la ventana cuando llege a su recorrido
                for x in Marciano.listaDisparo:
                   x.dibujar(ventana)
                   x.trayectoria()
                   if x.rect.top<10:
                      Marciano.listaDisparo.remove(x)
               
    
pygame.display.update()
juego()



