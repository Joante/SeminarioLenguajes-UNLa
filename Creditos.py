import pygame,sys


ancho =600
alto =800

def Creditos ():
    pygame.init()
    ventana = pygame.display.set_mode((alto,ancho))
    Fondo=pygame.image.load("imagenes/Fondo_Creditos.jpg").convert_alpha()
    print """
                    Creadores:
            Federico Salvatierra
            Joan Teich
            Santiago Martinez Vila
            Mariana Moline
            Francisco Laperuta

    """

if __name__ == '__main__':
	sys.stderr.write("You should import me, not start me...")
	sys.exit()
    
