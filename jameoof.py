import pygame, random

##############################################################################
#                                   CLASSES                                  #
##############################################################################
class Ball():
    x = y = d = xSpeed = ySpeed = colour = 0
    

class Button():
    x = y = w = h = clrInner = clrOuter = text = 0

balls = []



##############################################################################
#                                  FUNCTIONS                                 #
##############################################################################


##############################################################################
#                      ONE TIME SETUP (GLOBAL VARIABLES)                     #
##############################################################################
pygame.init()
screen = pygame.display.set_mode([500,500])
pygame.display.set_caption("Final Draft!")


gameState = "Menu"
clicks = 0

font40 = pygame.font.SysFont("Arial", 40, bold=True, italic=False)
font20 = pygame.font.SysFont("Times New Roman", 20, bold=True, italic=True)

startButton = Button()
startButton.w = 100
startButton.h = 50
startButton.x = screen.get_width()/2 - startButton.w/2
startButton.y = screen.get_height() - 200
startButton.clrInner = (220,120,20)
startButton.clrOuter = (255,255,255)
startButton.text = "GO!"

##############################################################################
#                                 GAME LOOP                                  #
##############################################################################
while True:
    # ========================== HANDLE EVENTS ============================= #
    done = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            done = True
            break
        # ==================== MOUSE DOWN ==================== #
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouseX = pygame.mouse.get_pos()[0]
            mouseY = pygame.mouse.get_pos()[1]
            if gameState == "Menu":
                #clicked on the start button?
                if mouseX >= startButton.x and mouseX <= startButton.x + startButton.w and mouseY >= startButton.y and mouseY <= startButton.y + startButton.h:
                    #reset all variables that might have changed during the game back
                    #to their original values


                    for i in range (2):
                        ball = Ball()
                        ball.d = random.randint(40,70)
                        ball.x = random.randint(70,screen.get_width()-ball.d)
                        ball.y = random.randint(70,screen.get_height()-ball.d)
                        ball.xSpeed = random.randint(-4,4)
                        ball.ySpeed = random.randint(-4,4)
                        ball.colour = (255,0,0)

                        balls.append (ball)
                    
                    clicks = 0
                    
                    gameState = "In Game"
                    
            elif gameState == "In Game":
                clicks = clicks + 1

                for i in range (len (balls)-1,-1,-1):
                    if mouseX >= balls[i].x and mouseX <= balls[i].x + balls[i].d and mouseY >= balls[i].y and mouseY <= balls[i].y + balls[i].d:
                        balls.remove (balls[i])
                    if len (balls) == 0:
                            gameState = "End Game"
        # ==================== MOUSE UP ====================== #
        elif event.type == pygame.MOUSEBUTTONUP:
            mouseX = pygame.mouse.get_pos()[0]
            mouseY = pygame.mouse.get_pos()[1]
        # ==================== KEY DOWN ====================== #
        elif event.type == pygame.KEYDOWN:
            if gameState == "End Game":
                if event.key == pygame.K_SPACE:
                    gameState = "Menu"
        # ==================== KEY UP ======================== #
        elif event.type == pygame.KEYUP:
            1 == 1 #Dummy code

    if done == True:
       break
    
    # ============================== MOVE STUFF ============================ #
    if gameState == "In Game":
        for i in range (len (balls)-1,-1,-1):
            balls[i].x = balls[i].x + balls[i].xSpeed
            balls[i].y = balls[i].y + balls[i].ySpeed

    # ============================== COLLISION ============================= #
    if gameState == "In Game":
        for i in range (len (balls)-1,-1,-1):
                
            if balls[i].y <= 0:
                balls[i].ySpeed = balls[i].ySpeed * -1
                
            elif balls[i].y + balls[i].d >= screen.get_height():
                balls[i].ySpeed = balls[i].ySpeed * -1

            if balls[i].x <= 0:
                balls[i].xSpeed = balls[i].xSpeed * -1
                
            elif balls[i].x + balls[i].d >= screen.get_width():
                balls[i].xSpeed = balls[i].xSpeed * -1

    # ============================== DRAW STUFF ============================ #
    if gameState == "Menu":
        screen.fill ((0,0,0))

        text = font40.render('SUPER FUN GAME!', True, (255,0,0))
        screen.blit(text, [screen.get_width()/2 - 150, screen.get_height()/3])

        pygame.draw.rect(screen, startButton.clrOuter, [startButton.x, startButton.y, startButton.w, startButton.h])
        pygame.draw.rect(screen, startButton.clrInner, [startButton.x+4, startButton.y+4, startButton.w-8, startButton.h-8])
        text = font40.render(startButton.text, True, (255,255,255))
        screen.blit(text, [startButton.x+20, startButton.y])

    elif gameState == "In Game":
        screen.fill((255,255,255))

        text = font40.render('Clicks: ' + str(clicks), True, (220,120,20))
        screen.blit(text, [10, 10])

        for i in range (len (balls)-1,-1,-1):
            if i == 0:
                balls[i].colour = 255,0,0
                color = color + 1
                
            elif i == 1:
                balls[i].colour = 0,0,255
                color = 0
            pygame.draw.ellipse (screen, balls[i].colour, [balls[i].x, balls[i].y, balls[i].d, balls[i].d])
        
    elif gameState == "End Game":
        screen.fill ((255,255,0))
        
        text = font40.render('YOU WIN!', True, (random.randint(0,255),random.randint(0,255),random.randint(0,255)))
        screen.blit(text, [screen.get_width()/2 - 100, screen.get_height()/3])

        text = font40.render('It took you ' + str(clicks) + " click(s)!", True, (20,120,255))
        screen.blit(text, [screen.get_width()/2 - 180, screen.get_height()/2])

        text = font20.render('Hit Spacebar to go to menu', True, (0,0,255))
        screen.blit(text, [30, screen.get_height() - 50])

    # ===================== PYGAME STUFF (NO NOT EDIT) ===================== #
    pygame.display.flip()
    pygame.time.delay(10)
