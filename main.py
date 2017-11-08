import pygame
import submenu as dm
pygame.init()

rojo   = 255,  0,  0
verde=   0,255,  0
fondo=pygame.image.load("imagenes/fondo.jpg")

tamanio= ancho, altura = 800,600
ventana = pygame.display.set_mode(tamanio)
ventana.blit(fondo,(0,0))
pygame.display.update()
pygame.key.set_repeat(500,30)

choose = dm.dumbmenu(ventana, [
                        'Iniciar Juego',
                        'Ayuda',
                        'Creditos',
                        'Salir'], 64,64,None,32,1.5,verde,rojo)  # cordenadas de lugar del menu, tamanio de letra(seguido de entrelineado)

# Prueba por consola

if choose == 0:
    from Clases import* 
elif choose == 1:
    from Manual import*
elif choose == 2:
    from Creditos import*
elif choose == 3:
     print ("Salir")
pygame.quit()
exit()
