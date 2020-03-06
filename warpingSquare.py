import pygame

pygame.init()
import pygame

pygame.init()
screen = pygame.display.set_mode([550,550])
pygame.display.set_caption("Screen Proportions")

#Set up global variables
width = screen.get_width()
height = screen.get_height()
redx = 250
redy = 250
redw = 20
redh = 20
yellowx = 250
yellowy = 250
yelloww = 20
yellowh = 20
speedredx = -0.3
speedredy = -0.7
speedyellowx = -0.3
speedyellowy = -0.7
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
    redy = redy + speedredy
    redx = redx + speedredx
    yellowy = yellowy + speedyellowy
    yellowx = yellowx + speedyellowx
    # ============================== COLLISION ============================== #
    if redy <= 0:
        speedredy = speedredy * -1.5
        
    elif redy + redh >= height:
        speedredy = speedredy * -1.5

    if redx <= 0:
        speedredx = speedredx * -1.5
        
    elif redx + redw >= width:
        speedredx = speedredx * -1.5

    if yellowy <= 0:
        speedyellowy = speedyellowy * -1.05
        
    elif yellowy + redh >= height:
        speedyellowy = speedyellowy * -1.05

    if yellowx <= 0:
        speedyellowx = speedyellowx * -1.05
        
    elif yellowx + redw >= width:
        speedyellowx = speedyellowx * -1.05








    
    # ============================== DRAW STUFF ============================= #
    screen.fill ((255,255,255))
    pygame.draw.rect (screen, (255,0,0), [redx,redy,redw,redh])
    pygame.draw.rect (screen, (255,255,0), [yellowx,yellowy,yelloww,yellowh])
    

    # ====================== PYGAME STUFF (DO NOT EDIT) ===================== #
    pygame.display.flip()
    pygame.time.delay(4)
    

