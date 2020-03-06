import pygame, random

##############################################################################
#                                   CLASSES                                  #
##############################################################################
class Button():
    x = y = w = h = text = colour = 0

class Enemy():
    x = y = w = h = xS = yS = hits = area = 0

class Projectile():
    x = y = w = h = xS = yS= 0

class Animation():
    x = y = w = h = 0

class EnemyArea():
    area = 0

##############################################################################
#                                  FUNCTIONS                                 #
##############################################################################

def collideRectRect (x1,y1,w1,h1,x2,y2,w2,h2):
    return x1 <= x2+w2 and x1+w1 >= x2 and y1 <= y2+h2 and y1+h1 >= y2


##############################################################################
#                      ONE TIME SETUP (GLOBAL VARIABLES)                     #
##############################################################################
pygame.init()
screen = pygame.display.set_mode([1000,750])
pygame.display.set_caption("Tower Defense")

S = 0
W = 0
D = 0
A = 0

proDown = Projectile ()
proDown.x = screen.get_width()/2 - 7
proDown.y = screen.get_height()/2
proDown.w = 15
proDown.h = 15
proDown.yS = 6

clockT = 0

proUp = Projectile ()
proUp.x = screen.get_width()/2 - 7
proUp.y = screen.get_height()/2 - 35
proUp.w = 15
proUp.h = 15
proUp.yS = 6

proLeft = Projectile ()
proLeft.x = screen.get_width()/2 - 25
proLeft.y = screen.get_height()/2 - 17
proLeft.w = 15
proLeft.h = 15
proLeft.xS = 6

proRight = Projectile ()
proRight.x = screen.get_width()/2 + 10
proRight.y = screen.get_height()/2 - 17
proRight.w = 15
proRight.h = 15
proRight.xS = 6


level = 0
enemies = []
area = []
enemiesSpawn = 0

attack = 0
proMoveU = 0
proMoveD = 0
proMoveL = 0
proMoveR = 0

animateD = 0
animateU = 0
animateL = 0
animateR = 0

arrowsUp = []
arrowUp = Animation()
arrowUp.y = screen.get_height()
arrowUp.c = 255
arrowsUp.append (arrowUp)

arrowsDown = []
arrowDown = Animation()
arrowDown.y = 0
arrowDown.c = 255
arrowsDown.append (arrowDown)

arrowsLeft = []
arrowLeft = Animation()
arrowLeft.c = 255
arrowLeft.x = screen.get_width()
arrowsLeft.append (arrowLeft)

arrowsRight = []
arrowRight = Animation()
arrowRight.c = 255
arrowRight.x = 0
arrowsRight.append (arrowRight)

gameState = "Menu"

font1 = pygame.font.SysFont("Helvetica", 40, bold=True, italic=False)

startButton = Button()
startButton.w = 95
startButton.h = 50
startButton.x = screen.get_width()/2 - startButton.w/2
startButton.y = screen.get_height() - 350
startButton.text = "Start"
startButton.colour = 255,255,255

hiButton = Button()
hiButton.w = 150
hiButton.h = 50
hiButton.x = screen.get_width()/2 - hiButton.w/2
hiButton.y = screen.get_height() - 300
hiButton.text = "High Scores"
hiButton.colour = 255,255,255

tutButton = Button()
tutButton.w = 120
tutButton.h = 50
tutButton.x = screen.get_width()/2 - tutButton.w/2
tutButton.y = screen.get_height() - 250
tutButton.text = "Tutorial"
tutButton.colour = 255,255,255

p1w = 50
p1h = 50
p1x = screen.get_width()/2 - p1w/2
p1y = screen.get_height()/2 - p1h/2

##############################################################################
#                                 GAME LOOP                                  #
##############################################################################
while True:
    # ========================== HANDLE EVENTS ============================= #
    if gameState == "Menu":
        mouseX = pygame.mouse.get_pos()[0]
        mouseY = pygame.mouse.get_pos()[1]
    
    done = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            done = True
            break

        if level == 1 and enemiesSpawn == 0:
            for i in range (20):
                eArea = EnemyArea ()
                eArea.area = random.randint (1,4)
                area.append (eArea)
                
            for i in range (len(area)):
                if area[i].area == 1:
                    enemy = Enemy()
                    enemy.x = screen.get_width()/2 - 14
                    enemy.yS = random.randint (1,1)
                    enemy.w = 30
                    enemy.area = 1

                    enemies.append (enemy)

                if area[i].area == 2:
                    enemy = Enemy()
                    enemy.x = screen.get_width()
                    enemy.y = screen.get_height()/2 - 15
                    enemy.xS = random.randint (1,1)
                    enemy.w = 30
                    enemy.area = 2

                    enemies.append (enemy)

                if area[i].area == 3:
                    enemy = Enemy()
                    enemy.x = screen.get_width()/2 - 14
                    enemy.y = screen.get_height()
                    enemy.yS = random.randint (1,1)
                    enemy.w = 30
                    enemy.area = 3

                    enemies.append (enemy)

                if area[i].area == 4:
                    enemy = Enemy()
                    enemy.y = screen.get_height()/2 - 15
                    enemy.xS = random.randint (1,1)
                    enemy.w = 30
                    enemy.area = 4

                    enemies.append (enemy)
                    
                enemiesSpawn = 1

        clockT = clockT + 1
                
        if (proDown) == 0:
            S = 0

        if (proUp) == 0:
            W = 0

        if (proLeft) == 0:
            A = 0

        if (proRight) == 0:
            D = 0

        # ==================== MOUSE DOWN ==================== #
        #Tutorial
        if event.type == pygame.MOUSEBUTTONDOWN:
            if gameState == "Menu":
                if mouseX >= startButton.x and mouseX <= startButton.x + startButton.w and mouseY >= startButton.y and mouseY <= startButton.y + startButton.h:
                    gameState = "inGame"

                if mouseX >= hiButton.x and mouseX <= hiButton.x + hiButton.w and mouseY >= hiButton.y and mouseY <= hiButton.y + hiButton.h:
                    gameState = "hiScore"

                if mouseX >= tutButton.x and mouseX <= tutButton.x + tutButton.w and mouseY >= tutButton.y and mouseY <= tutButton.y + startButton.h:
                    gameState = "tutorial"

        # =================== KEY DOWN ========================== #
        #In Game Projectiles
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s and proDown == 0:

                proDown = Projectile ()
                proDown.x = screen.get_width()/2 - 7
                proDown.y = screen.get_height()/2
                proDown.w = 15
                proDown.h = 15
                proDown.yS = 6
                
                if gameState == "inGame":
                    proMoveD = 1

            if event.key == pygame.K_w and proUp == 0:
                
                proUp = Projectile ()
                proUp.x = screen.get_width()/2 - 7
                proUp.y = screen.get_height()/2 - 35
                proUp.w = 15
                proUp.h = 15
                proUp.yS = 6
                
                if gameState == "inGame":
                    proMoveU = 1

            if event.key == pygame.K_a and proLeft == 0:
                
                proLeft = Projectile ()
                proLeft.x = screen.get_width()/2 - 25
                proLeft.y = screen.get_height()/2 - 17
                proLeft.w = 15
                proLeft.h = 15
                proLeft.xS = 6
                
                if gameState == "inGame":
                    proMoveL = 1

            if event.key == pygame.K_d and proRight == 0:
                
                proRight = Projectile ()
                proRight.x = screen.get_width()/2 + 10
                proRight.y = screen.get_height()/2 - 17
                proRight.w = 15
                proRight.h = 15
                proRight.xS = 6
                
                if gameState == "inGame":
                    proMoveR = 1

    if done == True:
        break
    
    # ============================== MOVE STUFF ============================ #
    #In Game (Animating Arrows)
    if gameState == "inGame" and animateD == 1:
        for i in range (len (arrowsDown) -1,-1,-1):
            arrowsDown[i].y = arrowsDown[i].y + 3
            if arrowsDown[i].c != 0:
                arrowsDown[i].c = arrowsDown[i].c - 3
            else:
                arrowsDown.remove (arrowsDown[i])

    if gameState == "inGame" and animateL == 1:
        for i in range (len (arrowsLeft) -1,-1,-1):
            arrowsLeft[i].x = arrowsLeft[i].x - 3
            if arrowsLeft[i].c != 0:
                arrowsLeft[i].c = arrowsLeft[i].c - 3
            else:
                arrowsLeft.remove (arrowsLeft[i])

    if gameState == "inGame" and animateU == 1:
        for i in range (len (arrowsUp) -1,-1,-1):
            arrowsUp[i].y = arrowsUp[i].y - 3
            if arrowsUp[i].c != 0:
                arrowsUp[i].c = arrowsUp[i].c - 3
            else:
                arrowsUp.remove (arrowsUp[i])

    if gameState == "inGame" and animateR == 1:
        for i in range (len (arrowsRight) -1,-1,-1):
            arrowsRight[i].x = arrowsRight[i].x + 3
            if arrowsRight[i].c != 0:
                arrowsRight[i].c = arrowsRight[i].c - 3
            else:
                arrowsRight.remove (arrowsRight[i])
                attack = 1
                level = level + 1
                
    #In Game Moving Projectiles
            proMoveD = 1
            proMoveU = 1
            proMoveL = 1
            proMoveR = 1
    
    if gameState == "inGame" and proMoveD == 1 and attack == 1 and proDown != 0:
        for i in range (1):
            proDown.y = proDown.y + proDown.yS

    if gameState == "inGame" and proMoveU == 1 and attack == 1 and proUp != 0:
        for i in range (1):
            proUp.y = proUp.y - proUp.yS

    if gameState == "inGame" and proMoveL == 1 and attack == 1 and proLeft != 0:
        for i in range (1):
            proLeft.x = proLeft.x - proLeft.xS

    if gameState == "inGame" and proMoveR == 1 and attack == 1 and proRight != 0:
        for i in range (1):
            proRight.x = proRight.x + proRight.xS
            
    if gameState == "inGame" and level == 1:
        for i in range (len(enemies) -1,-1,-1):
            
            if enemies[i].area == 1:
                enemies[i].y = enemies[i].y + enemies[i].yS
                
            elif enemies[i].area == 2:
                enemies[i].x = enemies[i].x - enemies[i].xS
                
            elif enemies[i].area == 3:
                enemies[i].y = enemies[i].y - enemies[i].yS
                
            elif enemies[i].area == 4:
                enemies[i].x = enemies[i].x + enemies[i].xS
        
    # ============================== COLLISION ============================= #
    #Game Collison
    for i in range (1):
        if gameState == "inGame" and proDown != 0:
            if proDown.y >= 750:
                proDown = 0
            
    for i in range (1):
        if gameState == "inGame" and proUp != 0:
            if proUp.y <= 0:
                proUp = 0

    for i in range (1):
        if gameState == "inGame" and proLeft != 0:
            if proLeft.x <= 0:
                proLeft = 0

    for i in range (1):
        if gameState == "inGame" and proRight != 0:
            if proRight.x >= 1000:
                proRight = 0

    

    for i in range (len(enemies) -1,-1,-1):
        if enemies[i].area == 1 and proUp != 0 and collideRectRect (enemies[i].x,enemies[i].y,enemies[i].w,enemies[i].w,proUp.x,proUp.y,proUp.w,proUp.w) == True:
            proUp = 0
            enemies.remove (enemies[i])
                
        elif enemies[i].area == 2 and proRight != 0 and collideRectRect (enemies[i].x,enemies[i].y,enemies[i].w,enemies[i].w,proRight.x,proRight.y,proRight.w,proRight.w) == True:
            proRight = 0
            enemies.remove (enemies[i])
                
        elif enemies[i].area == 3 and proDown != 0 and collideRectRect (enemies[i].x,enemies[i].y,enemies[i].w,enemies[i].w,proDown.x,proDown.y,proDown.w,proDown.w) == True:
            proDown = 0
            enemies.remove (enemies[i])
            
        elif enemies[i].area == 4 and proLeft != 0 and collideRectRect (enemies[i].x,enemies[i].y,enemies[i].w,enemies[i].w,proLeft.x,proLeft.y,proLeft.w,proLeft.w) == True:
            proLeft = 0
            enemies.remove (enemies[i])
 
        #if len(enemies) != 0 and collideRectRect (enemies[i].x,enemies[i].y,enemies[i].w,enemies[i].w,p1x,p1y,p1w,p1w) == True:
            #enemies.remove (enemies[i])

            
            

    # ============================== DRAW STUFF ============================ #
    #Menu
    if gameState == "Menu":
        screen.fill ((53,163,49))

        text = font1.render('Tower Defense', True, (255,255,255))
        screen.blit(text, [screen.get_width()/2 - 105, screen.get_height()/4])

        text = font1.render(startButton.text, True, (startButton.colour))
        screen.blit(text, [startButton.x + 20, startButton.y])

        text = font1.render(hiButton.text, True, (hiButton.colour))
        screen.blit(text, [hiButton.x - 10, hiButton.y])

        text = font1.render(tutButton.text, True, (tutButton.colour))
        screen.blit(text, [tutButton.x + 10, tutButton.y])

        if mouseX >= startButton.x and mouseX <= startButton.x + startButton.w and mouseY >= startButton.y and mouseY <= startButton.y + startButton.h:
            pygame.draw.polygon (screen, (255,255,255), [(startButton.x, startButton.y + 30), (startButton.x,startButton.y + 20), (startButton.x + 5,startButton.y + 25)])

        elif mouseX >= hiButton.x and mouseX <= hiButton.x + hiButton.w and mouseY >= hiButton.y and mouseY <= hiButton.y + hiButton.h:
            pygame.draw.polygon (screen, (255,255,255), [(hiButton.x - 30, hiButton.y + 30), (hiButton.x - 30,hiButton.y + 20), (hiButton.x - 25,hiButton.y + 25)])

        elif mouseX >= tutButton.x and mouseX <= tutButton.x + tutButton.w and mouseY >= tutButton.y and mouseY <= tutButton.y + tutButton.h:
            pygame.draw.polygon (screen, (255,255,255), [(tutButton.x - 5, tutButton.y + 30), (tutButton.x - 5,tutButton.y + 20), (tutButton.x,tutButton.y + 25)])

    #In Game
    elif gameState == "inGame":
        screen.fill ((0,0,0))
        pygame.draw.rect (screen, (255,255,255), [p1x,p1y,p1w,p1h])

        for i in range (len (arrowsDown)-1,-1,-1):
            text = font1.render("↓", True ,(arrowsDown[i].c,arrowsDown[i].c,arrowsDown[i].c))
            screen.blit(text, [screen.get_width()/2 - 9,arrowsDown[i].y])
            animateD = 1

        for i in range (len (arrowsLeft) -1,-1,-1):
            if len(arrowsDown) == 0:
                text = font1.render("←", True ,(arrowsLeft[i].c,arrowsLeft[i].c,arrowsLeft[i].c))
                screen.blit(text, [arrowsLeft[i].x, screen.get_height()/2 - 25])
                animateL = 1
                
        for i in range (len (arrowsUp)-1,-1,-1):
            if len(arrowsDown) == 0 and len(arrowsLeft) == 0:
                text = font1.render("↑", True ,(arrowsUp[i].c,arrowsUp[i].c,arrowsUp[i].c))
                screen.blit(text, [screen.get_width()/2 - 9, arrowsUp[i].y])
                animateU = 1
                        
        for i in range (len (arrowsRight) -1,-1,-1):
            if len(arrowsDown) == 0 and len (arrowsUp) == 0 and len(arrowsLeft) == 0:
                text = font1.render("→", True ,(arrowsRight[i].c,arrowsRight[i].c,arrowsRight[i].c))
                screen.blit(text, [arrowsRight[i].x, screen.get_height()/2 - 25])
                animateR = 1
                    
        if proMoveD == 1 and proDown != 0:
            for i in range (1):
                pygame.draw.rect (screen, (255,255,255), [proDown.x,proDown.y + 10,proDown.w,proDown.h])
      
        if proMoveU == 1 and proUp != 0:
            for i in range (1):
                pygame.draw.rect (screen, (255,255,255), [proUp.x,proUp.y + 10,proUp.w,proUp.h])

        if proMoveL == 1 and proLeft != 0:
            for i in range (1): 
                pygame.draw.rect (screen, (255,255,255), [proLeft.x,proLeft.y + 10,proLeft.w,proLeft.h])

        if proMoveR == 1 and proRight != 0:
            for i in range (1):
                pygame.draw.rect (screen, (255,255,255), [proRight.x,proRight.y + 10,proRight.w,proRight.h])

        if level == 1:
            for i in range (len(enemies)):
                pygame.draw.rect (screen, (255,0,0), [enemies[i].x,enemies[i].y,enemies[i].w,enemies[i].w])

    elif gameState == "hiScore":
        screen.fill ((53,163,49))

    elif gameState == "tutorial":
        screen.fill ((0,0,0))
    # ===================== PYGAME STUFF (NO NOT EDIT) ===================== #
    pygame.display.flip()
    pygame.time.delay(10)
