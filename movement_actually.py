import pygame
import random

pygame.init()
import pygame

pygame.init()
screen = pygame.display.set_mode([550,550])
pygame.display.set_caption("Movement")

#Set up global variables
width = screen.get_width()
height = screen.get_height()
redx = random.randint (70,screen.get_width() - 70)
redy = random.randint (70,screen.get_height() - 70)
redcolour = random.randint (0,255), random.randint (0,255), random.randint (0,255)
redl = random.randint (10,25)
speedredx = 0
speedredy = 0
redjump = 0
blux = random.randint (70,screen.get_width() - 70)
bluy = random.randint (70,screen.get_height() - 70)
redl = random.randint (10,25)
speedblux = 0
speedbluy = 0
blujump = 0
blul = random.randint (10,25)
blucolour = random.randint (0,255), random.randint (0,255), random.randint (0,255)

#Game loop
while True:

    # ===================== HANDLE EVENTS (DO NOT EDIT) ===================== #
    done = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            done = True
            break

    # ==================== KEY DOWN ====================== #
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                speedredy = 2
            elif event.key == pygame.K_a:
                speedredx = -2
            elif event.key == pygame.K_d:
                speedredx = 2
            elif event.key == pygame.K_w:
                speedredy = -2
            elif event.key == pygame.K_DOWN:
                speedbluy = 2
            elif event.key == pygame.K_LEFT:
                speedblux = -2
            elif event.key == pygame.K_RIGHT:
                speedblux = 2
            elif event.key == pygame.K_UP:
                speedbluy = -2
                

    # ==================== KEY UP ======================== #
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                    speedredx = 0
            elif event.key == pygame.K_d:
                    speedredx = 0
            elif event.key == pygame.K_w:
                    speedredy = 0
            elif event.key == pygame.K_s:
                    speedredy = 0
            elif event.key == pygame.K_RIGHT:
                speedblux = 0
            elif event.key == pygame.K_LEFT:
                speedblux = 0
            elif event.key == pygame.K_UP:
                speedbluy = 0
            elif event.key == pygame.K_DOWN:
                speedbluy = 0





    if done == True:
        break

    # ============================== MOVE STUFF ============================= #
    redy = redy + speedredy
    redx = redx + speedredx
    bluy = bluy + speedbluy
    blux = blux + speedblux
    # ============================== COLLISION ============================== #
    
    if redy <= 0:
        speedredy = speedredy * 0
        redy = 0
        
    elif redy + redl >= height:
        speedredy = speedredy * 0
        redy = height - redl

    if redx <= 0:
        speedredx = speedredx * 0
        redx = 0
        
    elif redx + redl >= width:
        speedredx = speedredx * 0
        redx = width - redl

        
    if bluy <= 0:
        speedbluy = speedbluy * 0
        bluy = 0
        
    elif bluy + blul >= height:
        speedbluy = speedbluy * 0
        bluy = height - blul

    if blux <= 0:
        speedblux = speedblux * 0
        blux = 0
        
    elif blux + blul >= width:
        speedblux = speedblux * 0
        blux = width - blul

    # ============================== DRAW STUFF ============================= #
    screen.fill ((255,255,255))
    pygame.draw.rect (screen, (redcolour), [redx,redy,redl,redl])
    pygame.draw.rect (screen, (blucolour), [blux,bluy,blul,blul])

    # ====================== PYGAME STUFF (DO NOT EDIT) ===================== #
    pygame.display.flip()
    pygame.time.delay(5)
    

