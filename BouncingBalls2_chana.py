import pygame
import random

pygame.init()
screen = pygame.display.set_mode([900,900])
pygame.display.set_caption("My First Game!")

#Set up global variables
class Ball():
    xSpeed=ySpeed=colour=diameter=x=y=0

balls = []

for i in range (3):
    colourBall = Ball()
    colourBall.xSpeed = random.randint (-5,5)
    colourBall.ySpeed = random.randint (-5,5)
    colourBall.colour = 255,0,0
    colourBall.diameter = random.randint (10,70) 
    colourBall.x = random.randint (70,screen.get_width() - 70)
    colourBall.y = random.randint (70,screen.get_height() - 70)

    balls.append (colourBall)
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
    for i in range (len (balls)-1,-1,-1):
        balls[i].y = balls[i].y + balls[i].ySpeed
        balls[i].x = balls[i].x + balls[i].xSpeed
    # ============================== COLLISION ============================== #
    for i in range (len (balls)-1,-1,-1):
        if balls[i].y <= 0:
            balls[i].ySpeed = balls[i].ySpeed * -1
            
        elif balls[i].y + balls[i].diameter >= screen.get_height():
            balls[i].ySpeed = balls[i].ySpeed * -1

        if balls[i].x <= 0:
            balls[i].xSpeed = balls[i].xSpeed * -1
            
        elif balls[i].x + balls[i].diameter >= screen.get_width():
            balls[i].xSpeed = balls[i].xSpeed * -1

    # ============================== DRAW STUFF ============================= #
    screen.fill ((255,255,255))
    for i in range (len (balls)-1,-1,-1):
        if i == 1:
            balls[i].colour = 0,255,0
        elif i == 2:
            balls[i].colour = 0,0,255
        else:
            balls[i].colour = 255,0,0
        pygame.draw.ellipse (screen, (balls[i].colour), [balls[i].x,balls[i].y,balls[i].diameter,balls[i].diameter])
    # ====================== PYGAME STUFF (DO NOT EDIT) ===================== #
    pygame.display.flip()
    pygame.time.delay(20)
