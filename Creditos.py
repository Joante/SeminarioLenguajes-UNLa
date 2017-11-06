import pygame,sys
pygame.init()
import submenu as dm
ancho =600
alto =800


pygame.init()
ventana = pygame.display.set_mode((alto,ancho))
fondo=pygame.image.load("imagenes/Fondo_Creditos.jpg").convert_alpha()

choose = dm.dumbmenu (ventana,[
                    'Creadores:',
           ' Federico Salvatierra',
           ' Joan Teich',
           ' Santiago Martinez Vila',
           ' Mariana Moline',
           ' Francisco Laperuta'])



if __name__ == '__main__':
	sys.stderr.write("You should import me, not start me...")
	sys.exit()
pygame.quit()
