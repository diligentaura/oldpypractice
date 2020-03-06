import pygame

pygame.init()
screen = pygame.display.set_mode([500,500])
pygame.display.set_caption("Screen Proportions")

#Set up global variables
redx = 250
redy = 250

wall1 = 0
wall2 = 480
collide = 2
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
    if collide == 2:
        redx = redx - 1
        redy = redy -1
    elif collide == 1:
        redx = redx + 1
        redy = redy + 1


    
    # ============================== COLLISION ============================== #
    if redx == wall1 or redy == wall1:
        collide = 1
    elif redx == wall2 or redy -- wall2:
        collide = 2
    # ============================== DRAW STUFF ============================= #
    screen.fill ((225,255,255))
    pygame.draw.rect (screen, (255,0,0), [redx,250,20,500])
    pygame.draw.rect (screen, (255,165,0), [redx,250,20,500])
    pygame.draw.rect (screen, (255,255,0), [0,redy,500,20])
    pygame.draw.rect (screen, (0,0,0), [0,redy,500,20])
    

    # ====================== PYGAME STUFF (DO NOT EDIT) ===================== #
    pygame.display.flip()
    pygame.time.delay(3)
    
