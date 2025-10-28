import pygame
import sys

pygame.init()

pantalla = pygame.display.set_mode((1000, 800)) 

pygame.display.set_caption("Mi primer programa gráfico")

COLOR_VERDE = (0, 255, 0)

running = True
while running:
    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
   
    pantalla.fill(COLOR_VERDE)
    
   
    pygame.display.flip()


pygame.quit()
sys.exit()