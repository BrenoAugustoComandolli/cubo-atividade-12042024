import pygame
import sys

# Inicialização do Pygame
pygame.init()

# Definição da largura e altura da tela
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Cubo Colorido")

# Definindo as cores
CYAN = (0, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
MAGENTA = (255, 0, 255)
ORANGE = (255, 165, 0)

# Definindo as coordenadas e o tamanho do cubo
cube_size = 100
cube_x = (width - cube_size) // 2
cube_y = (height - cube_size) // 2

# Loop principal
running = True
while running:
    # Eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Desenhar a tela de fundo
    screen.fill(CYAN)

    # Desenhar o cubo
    pygame.draw.rect(screen, RED, (cube_x, cube_y, cube_size, cube_size))  # Face frontal
    pygame.draw.polygon(screen, GREEN, [(cube_x, cube_y), (cube_x + cube_size, cube_y), 
                                         (cube_x + cube_size*1.5, cube_y + cube_size*0.5), 
                                         (cube_x + cube_size*0.5, cube_y + cube_size*0.5)])  # Lado esquerdo
    pygame.draw.polygon(screen, BLUE, [(cube_x + cube_size, cube_y), 
                                        (cube_x + cube_size, cube_y + cube_size), 
                                        (cube_x + cube_size*1.5, cube_y + cube_size*1.5), 
                                        (cube_x + cube_size*1.5, cube_y + cube_size*0.5)])  # Topo
    pygame.draw.polygon(screen, YELLOW, [(cube_x, cube_y), (cube_x, cube_y + cube_size), 
                                          (cube_x + cube_size*0.5, cube_y + cube_size*1.5), 
                                          (cube_x + cube_size*0.5, cube_y + cube_size*0.5)])  # Lado direito
    pygame.draw.polygon(screen, MAGENTA, [(cube_x, cube_y + cube_size), 
                                           (cube_x + cube_size, cube_y + cube_size), 
                                           (cube_x + cube_size*1.5, cube_y + cube_size*1.5), 
                                           (cube_x + cube_size*0.5, cube_y + cube_size*1.5)])  # Face traseira
    pygame.draw.polygon(screen, ORANGE, [(cube_x + cube_size, cube_y + cube_size), 
                                          (cube_x, cube_y + cube_size), 
                                          (cube_x + cube_size*0.5, cube_y + cube_size*1.5), 
                                          (cube_x + cube_size*1.5, cube_y + cube_size*1.5)])  # Base

    # Atualizar a tela
    pygame.display.flip()

# Finalizando o Pygame
pygame.quit()
sys.exit()