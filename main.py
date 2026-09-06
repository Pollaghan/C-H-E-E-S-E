import pygame
import gif_pygame
# Initialisation crap
pygame.init()
pygame.display.set_caption("C H E E S E")
ResolutionX = 1280
ResolutionY = 720
screen = pygame.display.set_mode((ResolutionX, ResolutionY), pygame.RESIZABLE, pygame.WINDOWMAXIMIZED)
icon = pygame.image.load("Cheese.png")
pygame.display.set_icon(icon)
# TOO MANY VARIABLES (yes that was a portal reference. deal with it)
Cheese = gif_pygame.load("CHEESE.gif")
# move
s1 = pygame.Surface((20, 0))
s2 = pygame.Surface((20, 0))
s3 = pygame.Surface((20, 0))
s1.fill((255, 0, 0))
s2.fill((0, 255, 0))
s3.fill((0, 0, 255))
animation_surfs = gif_pygame.GIFPygame([[s1, 1], [s2, 1], [s3, 0.5]])
# the damn game loop
while True :
    # Scaling
    Cheese = pygame.transform.scale(Cheese, (200, 200))
    # RENDERINNNNNNG
    screen.fill((0, 0, 0))
    ResolutionY = pygame.display.get_surface().get_height()
    ResolutionX = pygame.display.get_surface().get_width()
    screen.blit(Cheese,(ResolutionX-200,ResolutionY-200))
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()