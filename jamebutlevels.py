import pygame, random

##############################################################################
#                                   CLASSES                                  #
##############################################################################
class Ball():
    x = y = d = xSpeed = ySpeed = colour = 0

class Button():
    x = y = w = h = clrInner = clrOuter = text = 0

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
ball = Ball()
clicks = 0
level = 1
timer = 200

font40 = pygame.font.SysFont("Arial", 40, bold=True, italic=False)
font20 = pygame.font.SysFont("Times New Roman", 20, bold=True, italic=True)

startButton = Button()
startButton.w = 100
startButton.h = 50
startButton.x = screen.get_width()/2 - startButton.w/2
startButton.y = screen.get_height() - 200
startButton.clrInner = (220,120,20)
startButton.clrOuter = (255,255,255)
startButton.text = "GO"


##############################################################################
#                                 GAME LOOP                                  #
##############################################################################
while True:
    if gameState == "In Game":
        timer = timer - 1
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

                    ball.d = random.randint(40,70)
                    ball.x = random.randint(0,screen.get_width()-ball.d)
                    ball.y = random.randint(0,screen.get_height()-ball.d)
                    ball.xSpeed = random.randint(-4,4)
                    ball.ySpeed = random.randint(-4,4)
                    ball.colour = (random.randint(0,255),random.randint(0,255),random.randint(0,255))

                    clicks = 0
                    level = 1
                    
                    gameState = "In Game"
                    
            elif gameState == "In Game":
                clicks = clicks + 1
                if mouseX >= ball.x and mouseX <= ball.x + ball.d and mouseY >= ball.y and mouseY <= ball.y + ball.d:

                    #once they click the ball, increase the level.  The higher the level, the faster the ball!  But end with level 4
                    level = level + 1

                    ball.d = random.randint(40,70)
                    ball.x = random.randint(0,screen.get_width()-ball.d)
                    ball.y = random.randint(0,screen.get_height()-ball.d)
                    ball.colour = (random.randint(0,255),random.randint(0,255),random.randint(0,255))

                    if level == 2:
                        ball.xSpeed = random.randint(-8,8)
                        ball.ySpeed = random.randint(-8,8)     
                    elif level == 3:
                        ball.xSpeed = random.randint(-10,10)
                        ball.ySpeed = random.randint(-10,10)
                    elif level == 4:
                        ball.xSpeed = random.randint(-15,15)
                        ball.ySpeed = random.randint(-15,15)
                    elif level == 5:
                        ball.xSpeed = random.randint(-20,20)
                        ball.ySpeed = random.randint(-20,20)
                    elif level == 6:
                        ball.xSpeed = random.randint(-100,100)
                        ball.ySpeed = random.randint(-100,100)
                        
                    elif level == 7:
                        gameState = "End Game"

                    if timer <= 0:
                        gameState = "Lose"
                    
        # ==================== KEY DOWN ====================== #
        elif event.type == pygame.KEYDOWN:
            if gameState == "End Game":
                if event.key == pygame.K_SPACE:
                    gameState = "Menu"
        
    if done == True:
       break
    
    # ============================== MOVE STUFF ============================ #
    if gameState == "In Game":
        ball.x = ball.x + ball.xSpeed
        ball.y = ball.y + ball.ySpeed

    # ============================== COLLISION ============================= #
    if gameState == "In Game":    
        if ball.x <= 0 :
            ball.xSpeed = ball.xSpeed * -1
        elif ball.x + ball.d >= screen.get_width():
            ball.xSpeed = ball.xSpeed * -1

        if ball.y <= 0 :
            ball.ySpeed = ball.ySpeed * -1
        elif ball.y + ball.d >= screen.get_height():
            ball.ySpeed = ball.ySpeed * -1

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
        if level == 1:
            screen.fill((255,255,255)) #white
        elif level == 2:
            screen.fill((0,255,255)) #teal
        elif level == 3:
            screen.fill((0,255,0)) #green
        elif level == 4:
            screen.fill((0,0,0))
        elif level == 5:
            screen.fill((165,255,0))
        elif level == 6:
            screen.fill((25,255,100))

        times = timer/50
        

        text = font40.render('Clicks: ' + str(clicks), True, (220,120,20))
        screen.blit(text, [10, 10])

        text = font40.render('Level: ' + str(level), True, (220,120,20))
        screen.blit(text, [10, 50])

        text = font40.render('Time: ' + str(times), True, (220,120,20))
        screen.blit(text, [10, 90])
        
        pygame.draw.ellipse (screen, ball.colour, [ball.x, ball.y, ball.d, ball.d])

    elif gameState == "End Game":
        screen.fill ((255,255,0))
        
        text = font40.render('YOU WIN!', True, (random.randint(0,255),random.randint(0,255),random.randint(0,255)))
        screen.blit(text, [screen.get_width()/2 - 100, screen.get_height()/3])

        text = font40.render('It took you ' + str(clicks) + " click(s)!", True, (20,120,255))
        screen.blit(text, [screen.get_width()/2 - 180, screen.get_height()/2])

        text = font20.render('Hit Spacebar to go to menu', True, (0,0,255))
        screen.blit(text, [30, screen.get_height() - 50])

    elif gameState == "End Game":
        screen.fill ((255,255,0))
        
        text = font40.render('You Lose!', True, (random.randint(0,255),random.randint(0,255),random.randint(0,255)))
        screen.blit(text, [screen.get_width()/2 - 100, screen.get_height()/3])

        text = font20.render('Hit Spacebar to go to menu', True, (0,0,255))
        screen.blit(text, [30, screen.get_height() - 50])

    # ===================== PYGAME STUFF (NO NOT EDIT) ===================== #
    pygame.display.flip()
    pygame.time.delay(10)
