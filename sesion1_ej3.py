

import pygame
import sys

pygame.init()

pantalla = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Ejercicio 3 - Contador de Frames")


contador_frames = 0

running = True
while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    
    contador_frames = contador_frames + 1
    
    
    print(f"Frame: {contador_frames}")
    
    
    if contador_frames >= 300:
        running = False
    
    
    pantalla.fill((0, 0, 50)) 
    
    
    pygame.display.flip()

print("Se terminó después de 300 frames.")
pygame.quit()
sys.exit()