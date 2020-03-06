import pygame

pygame.init()
screen = pygame.display.set_mode([400,400])
pygame.display.set_caption("My First Game!")

#Set up global variables

#Game loop
while True:

    # ===================== HANDLE EVENTS (DO NOT EDIT) ===================== #
    done = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            done = True
            break

    if done == True:
        break

    # ============================== MOVE STUFF ============================= #

    # ============================== COLLISION ============================== #

    # ============================== DRAW STUFF ============================= #
    screen.fill ((244,194,194))
    pygame.draw.ellipse (screen, (0,0,0),[250,250,110,110]) 
    pygame.draw.ellipse (screen, (255,255,255),[255,255,100,100])
    

    # ====================== PYGAME STUFF (DO NOT EDIT) ===================== #
    pygame.display.flip()
    pygame.time.delay(20)
