import pygame
import random

pygame.init()
screen = pygame.display.set_mode([900,900])
pygame.display.set_caption("My First Game!")

#Set up global variables
class Ball():
    xSpeed=ySpeed=colour=diameter=x=y=0
    
redBall = Ball()
redBall.xSpeed = random.randint (-5,5)
redBall.ySpeed = random.randint (-5,5)
redBall.colour = 255,0,0
redBall.diameter = random.randint (10,70) 
redBall.x = random.randint (70,screen.get_width() - 70)
redBall.y = random.randint (70,screen.get_height() - 70)

greenBall = Ball()
greenBall.xSpeed = random.randint (-5,5)
greenBall.ySpeed = random.randint (-5,5)
greenBall.colour = 0,255,0
greenBall.diameter = random.randint (10,70) 
greenBall.x = random.randint (70,screen.get_width() - 70)
greenBall.y = random.randint (70,screen.get_height() - 70)

blueBall = Ball()
blueBall.xSpeed = random.randint (-5,5)
blueBall.ySpeed = random.randint (-5,5)
blueBall.colour = 0,0,255
blueBall.diameter = random.randint (10,70)
blueBall.x = random.randint (70,screen.get_width() - 70)
blueBall.y = random.randint (70,screen.get_height() - 70)

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
    redBall.y = redBall.y + redBall.ySpeed
    redBall.x = redBall.x + redBall.xSpeed
    greenBall.y = greenBall.y + greenBall.ySpeed
    greenBall.x = greenBall.x + greenBall.xSpeed
    blueBall.y = blueBall.y + blueBall.ySpeed
    blueBall.x = blueBall.x + blueBall.xSpeed
    # ============================== COLLISION ============================== #
    if redBall.y <= 0:
        redBall.ySpeed = redBall.ySpeed * -1
        
    elif redBall.y + redBall.diameter >= screen.get_height():
        redBall.ySpeed = redBall.ySpeed * -1

    if redBall.x <= 0:
        redBall.xSpeed = redBall.xSpeed * -1
        
    elif redBall.x + redBall.diameter >= screen.get_width():
        redBall.xSpeed = redBall.xSpeed * -1
        

    if greenBall.y <= 0:
        greenBall.ySpeed = greenBall.ySpeed * -1
        
    elif greenBall.y + greenBall.diameter >= screen.get_height():
        greenBall.ySpeed = greenBall.ySpeed * -1

    if greenBall.x <= 0:
        greenBall.xSpeed = greenBall.xSpeed * -1
        
    elif greenBall.x + greenBall.diameter >= screen.get_width():
        greenBall.xSpeed = greenBall.xSpeed * -1
        

    if blueBall.y <= 0:
        blueBall.ySpeed = blueBall.ySpeed * -1
        
    elif blueBall.y + blueBall.diameter >= screen.get_height():
        blueBall.ySpeed = blueBall.ySpeed * -1

    if blueBall.x <= 0:
        blueBall.xSpeed = blueBall.xSpeed * -1
        
    elif blueBall.x + blueBall.diameter >= screen.get_width():
        blueBall.xSpeed = blueBall.xSpeed * -1

    # ============================== DRAW STUFF ============================= #
    screen.fill ((255,255,255))
    pygame.draw.ellipse (screen, (redBall.colour), [redBall.x,redBall.y,redBall.diameter,redBall.diameter])
    pygame.draw.ellipse (screen, (greenBall.colour), [greenBall.x,greenBall.y,greenBall.diameter,greenBall.diameter])
    pygame.draw.ellipse (screen, (blueBall.colour), [blueBall.x,blueBall.y,blueBall.diameter,blueBall.diameter])
    # ====================== PYGAME STUFF (DO NOT EDIT) ===================== #
    pygame.display.flip()
    pygame.time.delay(20)
