import pygame
import threading
# Initialisation crap
pygame.init()
pygame.display.set_caption("C H E E S E")
ResolutionX = 1280
ResolutionY = 720
screen = pygame.display.set_mode((ResolutionX, ResolutionY), pygame.RESIZABLE, pygame.WINDOWMAXIMIZED)
icon = pygame.image.load("Cheese.png")
pygame.display.set_icon(icon)
# TOO MANY VARIABLES (yes that was a portal reference. deal with it)
frame = 1
Player = pygame.image.load("PLAYER.png")
Player = pygame.transform.scale(Player, (250, 250))
PlayerY = (ResolutionY / 2) - Player.get_height() / 2
# Functions n stuff
def ImageSequence(SequenceFolder,FrameName, Destination, EndFrame):
    Cheese = pygame.image.load(SequenceFolder + "/" + FrameName + "1" + ".png")
    Cheese = pygame.transform.scale(Cheese, (300, 300))
    if frame < EndFrame+1:
        Cheese = pygame.image.load(SequenceFolder+"/"+FrameName+str(round(frame))+".png")
        Cheese = pygame.transform.scale(Cheese, (300, 300))
        screen.blit(Cheese, Destination)
    else:
        screen.blit(Cheese, Destination)
    Cheese = pygame.transform.scale(Cheese, (300, 300))
def Jump(Height) :
    JumpHeight = 300
    return JumpHeight
# the damn game loop
while True :
    # RENDERINNNNNNG
    screen.fill((0, 0, 0))
    ResolutionY = pygame.display.get_surface().get_height()
    ResolutionX = pygame.display.get_surface().get_width()
    if frame < 48 :
        CheeseRendering = threading.Thread(target=ImageSequence("CHESEE","ches", (ResolutionX-300, ResolutionY-300), 48))
    else:
        # where we now live THIS IS OUR NEW HOME
        screen.blit(Player, ((ResolutionX/2)-Player.get_width()/2,PlayerY))
        if PlayerY < 720 :
            PlayerY += 1
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    PlayerY -= Jump(300)

        # bye
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    frame += 0.2