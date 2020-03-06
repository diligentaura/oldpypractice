import pygame, random

##############################################################################
#                                   CLASSES                                  #
##############################################################################
class Button():
    x = y = w = h = text = colour = 0

class Enemy():
    x = y = w = h = xS = yS = split = color = 0

class Projectile():
    x = y = w = h = xS = yS = dir = 0

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
pygame.display.set_caption("Slider Asteroids")

proj = []
whiteSquare = Projectile ()
whiteSquare.w = 15
whiteSquare.h = 15
whiteSquare.x = screen.get_width()/2 - whiteSquare.w
whiteSquare.y = screen.get_height()/2 - whiteSquare.h
whiteSquare.yS = 5
whiteSquare.xS = 5

projStopDown = 0
projStopUp = 0
projStopLeft = 0
projStopRight = 0

level = 0
enemies = []
area = []
enemySpawn = 0

attack = 0

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

font1 = pygame.font.SysFont("fluentcalibri", 40, bold=True, italic=False)

font2 = pygame.font.SysFont("fluentcalibri", 40, bold=True, italic=True)

font3 = pygame.font.SysFont("Arial", 40, bold=True, italic=False)

startButton = Button()
startButton.w = 110
startButton.h = 50
startButton.x = screen.get_width()/2 - startButton.w/2
startButton.y = screen.get_height() - 350
startButton.text = "Start"
startButton.colour = 255,255,255

hiButton = Button()
hiButton.w = 270
hiButton.h = 50
hiButton.x = screen.get_width()/2 - hiButton.w/2
hiButton.y = screen.get_height() - 300
hiButton.text = "High Scores"
hiButton.colour = 255,255,255

tutButton = Button()
tutButton.w = 175
tutButton.h = 50
tutButton.x = screen.get_width()/2 - tutButton.w/2
tutButton.y = screen.get_height() - 250
tutButton.text = "Tutorial"
tutButton.colour = 255,255,255

menuButton = Button()
menuButton.w = 165
menuButton.h = 50
menuButton.x = screen.get_width()/2 - menuButton.w/2
menuButton.y = screen.get_height() - 230
menuButton.text = "Menu"
menuButton.colour = 255,255,255

menuButton2 = Button()
menuButton2.w = 165
menuButton2.h = 50
menuButton2.x = screen.get_width()/2 - menuButton.w/2 - 10
menuButton2.y = screen.get_height() - 150
menuButton2.text = "Menu"
menuButton2.colour = 255,255,255

p1w = 15
p1h = 15
p1x = screen.get_width()/2 - p1w/2
p1y = screen.get_height()/2 - p1h/2
p1xS = 0
p1yS = 0
p1c = 255

slowHori = 0
slowVert = 0

lives = 0

runOnce = 0
runOnceAppend = 0

placeHoldy = 0
placeHoldx = 0
splitOccured = 0

numberEnemies = 3
rounds = 1

score = 0
name = []
roundEdit = 0
invincibility = 0
timer = 0
adding = 0
subtracting = 0
trueName = 0
powerUpWallBounce = 0
powerUpLife = 0
powerUpTime = 0
powerUpInv = 0

score1 = 12000
score2 = 5000
score3 = 2500
score4 = 1000
score5 = 500

name1 = "Expert"
name2 = "Hard"
name3 = "Medium"
name4 = "Easy"
name5 = "Simple"

nameString = 0
##############################################################################
#                                 GAME LOOP                                  #
##############################################################################
while True:
    # ========================== HANDLE EVENTS ============================= #
    if gameState == "Menu" or gameState == "hiScore" or gameState == "tutorial":
        mouseX = pygame.mouse.get_pos()[0]
        mouseY = pygame.mouse.get_pos()[1]

    if gameState == "inGame" and attack == 1 and runOnce == 0:
        enemySpawn = 1
        runOnce = runOnce + 1

    if gameState == "inGame" and invincibility == 1:
        timer = timer + 1
        p1c = random.randint (0,255),random.randint (0,255),random.randint (0,255)

    if powerUpTime != 0:
        p1c = 0,0,255

    if invincibility == 0 and p1c != (255,255,255) and powerUpTime == 0 and gameState == "inGame":
        p1c = 255,255,255

    if timer >= 500 and gameState == "inGame":
        invincibility = 0
        timer = 0

    if powerUpInv == 5 and gameState == "inGame":
        invincibility = 1
        powerUpInv = 0

    if powerUpLife == 5 and gameState == "inGame" and lives != 3:
        lives = lives + 1

    if powerUpWallBounce == 5 or powerUpTime != 0:
        powerUpTime = powerUpTime + 1

    if powerUpTime >= 750 and gameState == "inGame":
        powerUpTime = 0
        powerUpWallBounce = 0
        
    if lives <= 0 and gameState == "inGame":
        powerUpTime = 0
        powerUpLife = 0
        powerUpInv = 0
        powerUpWallBounce = 0
        timer = 0
        invincibility = 0
        roundEdit = 0
        numberEnemies = 3
        splitOccured = 0
        placeHoldy = 0
        placeHoldx = 0
        slowHori = 0
        slowVert = 0
        p1xS = 0
        p1yS = 0
        p1x = screen.get_width()/2 - p1w/2
        p1y = screen.get_height()/2 - p1h/2
        p1c = 255,255,255
        runOnceAppend = 0
        runOnce = 0
        rounds = 1
        
        proj = []
        whiteSquare = Projectile ()
        whiteSquare.w = 15
        whiteSquare.h = 15
        whiteSquare.x = screen.get_width()/2 - whiteSquare.w
        whiteSquare.y = screen.get_height()/2 - whiteSquare.h
        whiteSquare.yS = 5
        whiteSquare.xS = 5

        projStopDown = 0
        projStopUp = 0
        projStopLeft = 0
        projStopRight = 0

        level = 0
        enemies = []
        area = []
        enemySpawn = 0

        attack = 0

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

        gameState = "name"
        
        for i in range (len(enemies) -1,-1,-1):
            enemies.remove (enemies[i])

    if enemySpawn == 1 and runOnceAppend == 0 and gameState == "inGame":
        for i in range (numberEnemies):
            enemy = Enemy()
            enemy.x = random.randint (0,1000)
            enemy.y = random.randint (0,750)
            enemy.yS = random.randint (-2,2)
            enemy.xS = random.randint (-2,2)
            enemy.color = random.randint (100,255), random.randint (100,255), random.randint (100,255)
            enemy.w = 50

            enemies.append (enemy)
        numberEnemies = numberEnemies + 1
            

    if len(enemies) == 0 and attack == 1 and gameState == "inGame":
        rounds = rounds + 1
        attack = 0
        if lives < 3:
            lives = lives + 1

        animateD = 0
        animateU = 0
        animateL = 0
        animateR = 0
        invincibility = 1

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

        roundEdit = 1

        p1xS = 0
        p1yS = 0
        p1x = screen.get_width()/2 - p1w/2
        p1y = screen.get_height()/2 - p1h/2

    for i in range (len(enemies) -1,-1,-1):
        if enemies[i].split == 1 and enemies[i].w == 50:
            enemies[i].split = 0
            placeHoldx = enemies[i].x
            placeHoldy = enemies[i].y
            enemies.remove (enemies[i])
            for i in range (2):
                enemy = Enemy()
                enemy.x = placeHoldx
                enemy.y = placeHoldy
                enemy.yS = random.randint (-3,3)
                enemy.xS = random.randint (-3,3)
                enemy.color = random.randint (0,255), random.randint (0,255), random.randint (0,255)
                enemy.w = 30
                enemy.split = 0
                
                enemies.append (enemy)
            

    for i in range (len(enemies) -1,-1,-1):
        if enemies[i].split == 1 and enemies[i].w == 30:
            enemies[i].split = 0
            placeHoldx = enemies[i].x
            placeHoldy = enemies[i].y
            enemies.remove (enemies[i])
            for i in range (2):
                enemy = Enemy()
                enemy.x = placeHoldx
                enemy.y = placeHoldy
                enemy.yS = random.randint (-4,4)
                enemy.xS = random.randint (-4,4)
                enemy.color = random.randint (0,255), random.randint (0,255), random.randint (0,255)
                enemy.w = 15
                enemy.split = 0
                
                enemies.append (enemy)
            
        runOnceAppend = runOnceAppend + 1

    done = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            done = True
            break

        # ==================== MOUSE DOWN ==================== #
        #Tutorial
        if event.type == pygame.MOUSEBUTTONDOWN:
            if gameState == "Menu":
                if mouseX >= startButton.x and mouseX <= startButton.x + startButton.w and mouseY >= startButton.y and mouseY <= startButton.y + startButton.h:
                    gameState = "inGame"
                    lives = 3
                    invincibility = 1

                if mouseX >= hiButton.x and mouseX <= hiButton.x + hiButton.w and mouseY >= hiButton.y and mouseY <= hiButton.y + hiButton.h:
                    gameState = "hiScore"

                if mouseX >= tutButton.x and mouseX <= tutButton.x + tutButton.w and mouseY >= tutButton.y and mouseY <= tutButton.y + startButton.h:
                    gameState = "tutorial"

            elif gameState == "hiScore":
                if mouseX >= menuButton.x and mouseX <= menuButton.x + menuButton.w and mouseY >= menuButton.y and mouseY <= menuButton.y + menuButton.h:
                    gameState = "Menu"

            elif gameState == "tutorial":
                if mouseX >= menuButton2.x and mouseX <= menuButton2.x + menuButton2.w and mouseY >= menuButton2.y and mouseY <= menuButton2.y + menuButton2.h:
                    gameState = "Menu"
                    
        # =================== KEY DOWN ========================== #
        #In Game Projectiles
        if event.type == pygame.KEYDOWN and gameState == "inGame":
                    
            if event.key == pygame.K_s:
                whiteSquare = Projectile ()
                whiteSquare.w = 4
                whiteSquare.h = 4
                whiteSquare.x = p1x + p1w/2 - whiteSquare.w/2 + 1
                whiteSquare.y = p1y + p1h/2 - whiteSquare.h/2 + 1
                whiteSquare.yS = 5
                whiteSquare.xS = 5
                whiteSquare.dir = "Down"
                proj.append (whiteSquare)

            elif event.key == pygame.K_w:
                whiteSquare = Projectile ()
                whiteSquare.w = 4
                whiteSquare.h = 4
                whiteSquare.x = p1x + p1w/2 - whiteSquare.w/2 + 1
                whiteSquare.y = p1y + p1h/2 - whiteSquare.h/2 + 1
                whiteSquare.yS = 5
                whiteSquare.xS = 5
                whiteSquare.dir = "Up"
                proj.append (whiteSquare)

            elif event.key == pygame.K_a:
                whiteSquare = Projectile ()
                whiteSquare.w = 4
                whiteSquare.h = 4
                whiteSquare.x = p1x + p1w/2 - whiteSquare.w/2 + 1
                whiteSquare.y = p1y + p1h/2 - whiteSquare.h/2 + 1
                whiteSquare.yS = 5
                whiteSquare.xS = 5
                whiteSquare.dir = "Left"
                proj.append (whiteSquare)

            elif event.key == pygame.K_d:
                whiteSquare = Projectile ()
                whiteSquare.w = 4
                whiteSquare.h = 4
                whiteSquare.x = p1x + p1w/2 - whiteSquare.w/2 + 1
                whiteSquare.y = p1y + p1h/2 - whiteSquare.h/2 + 1
                whiteSquare.yS = 5
                whiteSquare.xS = 5
                whiteSquare.dir = "Right"
                proj.append (whiteSquare)

            elif event.key == pygame.K_DOWN:
                p1yS = 2
                slowVert = "Yes"
            elif event.key == pygame.K_LEFT:
                p1xS = -2
                slowHori = "Yes"
            elif event.key == pygame.K_RIGHT:
                p1xS = 2
                slowHori = "Yes"
            elif event.key == pygame.K_UP:
                p1yS = -2
                slowVert = "Yes"

        if event.type == pygame.KEYDOWN and gameState == "name":
            if event.key == pygame.K_a and len(name) != 4:
                name.append("A")

            elif event.key == pygame.K_b and len(name) != 4:
                name.append("B")

            elif event.key == pygame.K_c and len(name) != 4:
                name.append("C")

            elif event.key == pygame.K_d and len(name) != 4:
                name.append("D")

            elif event.key == pygame.K_e and len(name) != 4:
                name.append("E")
                
            elif event.key == pygame.K_f and len(name) != 4:
                name.append("F")

            elif event.key == pygame.K_g and len(name) != 4:
                name.append("G")

            elif event.key == pygame.K_h and len(name) != 4:
                name.append("H")

            elif event.key == pygame.K_i and len(name) != 4:
                name.append("I")

            elif event.key == pygame.K_j and len(name) != 4:
                name.append("J")

            elif event.key == pygame.K_k and len(name) != 4:
                name.append("K")

            elif event.key == pygame.K_l and len(name) != 4:
                name.append("L")

            elif event.key == pygame.K_m and len(name) != 4:
                name.append("M")

            elif event.key == pygame.K_n and len(name) != 4:
                name.append("N")

            elif event.key == pygame.K_o and len(name) != 4:
                name.append("O")

            elif event.key == pygame.K_p and len(name) != 4:
                name.append("P")

            elif event.key == pygame.K_q and len(name) != 4:
                name.append("Q")

            elif event.key == pygame.K_r and len(name) != 4:
                name.append("R")

            elif event.key == pygame.K_s and len(name) != 4:
                name.append("S")

            elif event.key == pygame.K_t and len(name) != 4:
                name.append("T")

            elif event.key == pygame.K_u and len(name) != 4:
                name.append("U")

            elif event.key == pygame.K_v and len(name) != 4:
                name.append("V")

            elif event.key == pygame.K_w and len(name) != 4:
                name.append("W")

            elif event.key == pygame.K_x and len(name) != 4:
                name.append("X")

            elif event.key == pygame.K_y and len(name) != 4:
                name.append("Y")

            elif event.key == pygame.K_z and len(name) != 4:
                name.append("Z")

            elif event.key == pygame.K_BACKSPACE:
                name = []

            if event.key == pygame.K_RETURN:
                for i in range (len(name)):
                    if trueName != 0:
                        trueName = trueName + name[i]
                    else:
                        trueName = name[i]
                        
                if score >= score1:
                    score1 = score
                    name1 = trueName
                    trueName = 0
                    score = 0
                    name = []
                    gameState = "hiScore"

                elif score1 >= score >= score2:
                    score2 = score
                    name2 = trueName
                    trueName = 0
                    score = 0
                    name = []
                    gameState = "hiScore"
                    
                elif score1 >= score2 >= score >= score3:
                    score3 = score
                    name3 = trueName
                    trueName = 0
                    score = 0
                    name = []
                    gameState = "hiScore"
                    
                elif score1 >= score2 >= score3 >= score >= score4:
                    score4 = score
                    name4 = trueName
                    trueName = 0
                    score = 0
                    name = []
                    gameState = "hiScore"
                    
                elif score1 >= score2 >= score3 >= score4 >= score >= score5:
                    score5 = score
                    name5 = trueName
                    trueName = 0
                    score = 0
                    name = []
                    gameState = "hiScore"

                else:
                    trueName = 0
                    score = 0
                    name = []
                    gameState = "hiScore"
                


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
                if roundEdit == 1:
                    enemySpawn = 1
                    runOnceAppend = 0
                    roundEdit = 0
                
    #In Game Moving Projectiles
    if gameState == "inGame" and attack == 1:
        for i in range (len(proj) -1,-1,-1):
            if proj[i].dir == "Down":
                proj[i].y = proj[i].y + proj[i].yS

            if proj[i].dir == "Up":
                proj[i].y = proj[i].y - proj[i].yS

            if proj[i].dir == "Left":
                proj[i].x = proj[i].x - proj[i].xS

            if proj[i].dir == "Right":
                proj[i].x = proj[i].x + proj[i].xS
    
        p1x = p1x + p1xS
        p1y = p1y + p1yS

        if slowHori == "Yes" and p1xS != 0:
            if p1xS > 0.01:
                p1xS = p1xS - 0.01
                
            elif p1xS < -0.01:
                p1xS = p1xS + 0.01

            elif -0.01 <= p1xS <= 0.01 and p1xS != 0:
                p1xS = 0
                
        elif p1xS == 0:
            slowHori = 0
            
        if slowVert == "Yes" and p1yS != 0:
            if p1yS > 0.01:
                p1yS = p1yS - 0.01
                
            elif p1yS < -0.01:
                p1yS = p1yS + 0.01

            elif -0.01 <= p1yS <= 0.01 and p1yS != 0:
                p1yS = 0
                
        elif p1yS == 0:
            slowVert = 0

    if gameState == "inGame" and enemySpawn == 1:
        for i in range (len(enemies) -1,-1,-1):
            enemies[i].y = enemies[i].y + enemies[i].yS
            enemies[i].x = enemies[i].x + enemies[i].xS
        
    # ============================== COLLISION ============================= #
    #Game Collison
    if gameState == "inGame":
        if p1x >= 1015:
            p1x = -15

        if p1x <= -20:
            p1x = 1000

        if p1y >= 765:
            p1y = -15

        if p1y <= -20:
            p1y = 750

        for i in range (len(enemies) -1,-1,-1):
            if enemies[i].x >= 1000 + enemies[i].w:
                enemies[i].x = 0 - enemies[i].w
                
            if enemies[i].x <= -10 - enemies[i].w:
                enemies[i].x = 1000

            if enemies[i].y >= 750 + enemies[i].w:
                enemies[i].y = 0 - enemies[i].w

            if enemies[i].y <= -10 - enemies[i].w:
                enemies[i].y = 750
                
        for enemy in enemies:
            for whiteSquare in proj:
                if collideRectRect (enemy.x,enemy.y,enemy.w,enemy.w,whiteSquare.x,whiteSquare.y,whiteSquare.h,whiteSquare.w) == True:
                    proj.remove (whiteSquare)
                    if enemy.w == 30 or enemy.w == 50:
                        enemy.split = 1
                        powerUpLife = random.randint (1,30)
                        powerUpWallBounce = random.randint (1,40)
                        powerUpInv = random.randint (1,20)
                        score = score + 50
                        
                    else:
                        powerUpLife = random.randint (1,30)
                        powerUpWallBounce = random.randint (1,40)
                        powerUpInv = random.randint (1,20)
                        enemies.remove (enemy)
                        score = score + 150
                        break

        for enemy in enemies:
            if collideRectRect (enemy.x,enemy.y,enemy.w,enemy.w,p1x,p1y,p1w,p1w) == True and invincibility == 0:
                p1x = screen.get_width()/2 - p1w/2
                p1y = screen.get_height()/2 - p1h/2
                p1xS = 0
                p1yS = 0
                lives = lives - 1
                invincibility = 1

        if powerUpTime != 0:
            for i in range (len(proj) -1,-1,-1):
                if proj[i].y <= 0:
                    proj[i].yS = proj[i].yS * -1
                    
                elif proj[i].y + proj[i].w >= screen.get_height():
                    proj[i].yS = proj[i].yS * -1

                if proj[i].x <= 0:
                    proj[i].xS = proj[i].xS * -1
                    
                elif proj[i].x + proj[i].w >= screen.get_width():
                    proj[i].xS = proj[i].xS * -1

        elif powerUpTime == 0:
            for i in range (len(proj) -1,-1,-1):
                if proj[i].y <= 0:
                    proj.remove (proj[i])
                    break
                    
                elif proj[i].y + proj[i].w >= screen.get_height():
                    proj.remove (proj[i])
                    break

                if proj[i].x <= 0:
                    proj.remove (proj[i])
                    break
                    
                elif proj[i].x + proj[i].w >= screen.get_width():
                    proj.remove (proj[i])
                    break

    # ============================== DRAW STUFF ============================ #
    #Menu
    if gameState == "Menu":
        screen.fill ((0,0,0))

        pygame.draw.rect (screen, (255,255,255),[193,140,620,450])
        pygame.draw.rect (screen, (0,0,0),[203,150,600,430])

        text = font1.render("Slider Asteroids", True, (255,255,255))
        screen.blit(text, [screen.get_width()/2 - 180, screen.get_height()/4])

        text = font1.render(startButton.text, True, (startButton.colour))
        screen.blit(text, [startButton.x, startButton.y])

        text = font1.render(hiButton.text, True, (hiButton.colour))
        screen.blit(text, [hiButton.x, hiButton.y])

        text = font1.render(tutButton.text, True, (tutButton.colour))
        screen.blit(text, [tutButton.x, tutButton.y])



        if mouseX >= startButton.x and mouseX <= startButton.x + startButton.w and mouseY >= startButton.y and mouseY <= startButton.y + startButton.h:
            pygame.draw.polygon (screen, (255,255,255), [(startButton.x - 16, startButton.y + 23), (startButton.x - 16,startButton.y + 13), (startButton.x - 11,startButton.y + 18)])

        elif mouseX >= hiButton.x and mouseX <= hiButton.x + hiButton.w and mouseY >= hiButton.y and mouseY <= hiButton.y + hiButton.h:
            pygame.draw.polygon (screen, (255,255,255), [(hiButton.x - 16, hiButton.y + 22), (hiButton.x - 16,hiButton.y + 12), (hiButton.x - 11,hiButton.y + 17)])

        elif mouseX >= tutButton.x and mouseX <= tutButton.x + tutButton.w and mouseY >= tutButton.y and mouseY <= tutButton.y + tutButton.h:
            pygame.draw.polygon (screen, (255,255,255), [(tutButton.x - 16, tutButton.y + 23), (tutButton.x - 16,tutButton.y + 13), (tutButton.x - 11,tutButton.y + 18)])

    #In Game
    elif gameState == "inGame":
        screen.fill ((0,0,0))
        pygame.draw.rect (screen, (p1c), [p1x,p1y,p1w,p1h])
        text = font1.render("Score:" + str(score), True ,(255,255,255))
        screen.blit(text, [0,0])

        text = font1.render("Lives:", True ,(255,255,255))
        screen.blit(text, [0,40])

        text = font1.render("Round:" + str(rounds), True ,(255,255,255))
        screen.blit(text, [0,80])
        
        if lives == 3:
            pygame.draw.rect (screen, (255,255,255), [150,40,30,30])
            pygame.draw.rect (screen, (255,255,255), [200,40,30,30])
            pygame.draw.rect (screen, (255,255,255), [250,40,30,30])

        if lives == 2:
            pygame.draw.rect (screen, (255,255,255), [150,40,30,30])
            pygame.draw.rect (screen, (255,255,255), [200,40,30,30])

        if lives == 1:
            pygame.draw.rect (screen, (255,255,255), [150,40,30,30])
        
        for i in range (len (arrowsDown)-1,-1,-1):
            text = font1.render("↓", True ,(arrowsDown[i].c,arrowsDown[i].c,arrowsDown[i].c))
            screen.blit(text, [screen.get_width()/2 - 18,arrowsDown[i].y])
            animateD = 1

        for i in range (len (arrowsLeft) -1,-1,-1):
            if len(arrowsDown) == 0:
                text = font1.render("←", True ,(arrowsLeft[i].c,arrowsLeft[i].c,arrowsLeft[i].c))
                screen.blit(text, [arrowsLeft[i].x, screen.get_height()/2 - 19])
                animateL = 1
                
        for i in range (len (arrowsUp)-1,-1,-1):
            if len(arrowsDown) == 0 and len(arrowsLeft) == 0:
                text = font1.render("↑", True ,(arrowsUp[i].c,arrowsUp[i].c,arrowsUp[i].c))
                screen.blit(text, [screen.get_width()/2 - 18, arrowsUp[i].y])
                animateU = 1
                        
        for i in range (len (arrowsRight) -1,-1,-1):
            if len(arrowsDown) == 0 and len (arrowsUp) == 0 and len(arrowsLeft) == 0:
                text = font1.render("→", True ,(arrowsRight[i].c,arrowsRight[i].c,arrowsRight[i].c))
                screen.blit(text, [arrowsRight[i].x, screen.get_height()/2 - 19])
                animateR = 1
                    
        for i in range (len(proj) -1,-1,-1):
            pygame.draw.rect (screen, (255,255,255), [proj[i].x,proj[i].y,proj[i].w,proj[i].h])

        if enemySpawn == 1:
            for i in range (len(enemies) -1,-1,-1):
                pygame.draw.rect (screen, (enemies[i].color), [enemies[i].x,enemies[i].y,enemies[i].w,enemies[i].w])

    elif gameState == "hiScore":
        screen.fill ((0,0,0))

        pygame.draw.rect (screen, (255,255,255),[193,140,620,470])
        pygame.draw.rect (screen, (0,0,0),[203,150,600,450])
        
        text = font1.render("High Scores", True ,(255,255,255))
        screen.blit(text, [370,180])
        
        text = font1.render(menuButton.text, True, (menuButton.colour))
        screen.blit(text, [menuButton.x + 32, menuButton.y + 20])
        
        if mouseX >= menuButton.x and mouseX <= menuButton.x + menuButton.w and mouseY >= menuButton.y and mouseY <= menuButton.y + menuButton.h:
            pygame.draw.polygon (screen, (255,255,255), [(menuButton.x + 13, menuButton.y + 43), (menuButton.x + 13,menuButton.y + 33), (menuButton.x + 18,menuButton.y + 38)])

        text = font2.render("Score", True ,(255,255,255))
        screen.blit(text, [335,230])
        
        text = font2.render("Name", True ,(255,255,255))
        screen.blit(text, [570,230])
        
        text = font1.render(str(score1), True ,(255,255,255))
        screen.blit(text, [330,280])
        
        text = font1.render(str(score2), True ,(255,255,255))
        screen.blit(text, [330,330])
        
        text = font1.render(str(score3), True ,(255,255,255))
        screen.blit(text, [330,380])

        text = font1.render(str(score4), True ,(255,255,255))
        screen.blit(text, [330,430])

        text = font1.render(str(score5), True ,(255,255,255))
        screen.blit(text, [330,480])
        
        text = font1.render(name1, True ,(255,255,255))
        screen.blit(text, [560,280])
        
        text = font1.render(name2, True ,(255,255,255))
        screen.blit(text, [560,330])
        
        text = font1.render(name3, True ,(255,255,255))
        screen.blit(text, [560,380])

        text = font1.render(name4, True ,(255,255,255))
        screen.blit(text, [560,430])

        text = font1.render(name5, True ,(255,255,255))
        screen.blit(text, [560,480])
        
    elif gameState == "tutorial":
        screen.fill ((0,0,0))
        pygame.draw.rect (screen, (255,255,255),[0,0,1000,750])
        pygame.draw.rect (screen, (0,0,0),[20,20,960,710])

        text = font1.render("Tutorial", True ,(255,255,255))
        screen.blit(text, [410,100])
        
        text = font3.render("1. Use W A S D Keys To Move", True ,(255,255,255))
        screen.blit(text, [35,200])
        text = font3.render("You will Slide Around.", True ,(255,255,255))
        screen.blit(text, [35,250])
        text = font3.render("2. Use Arrow Keys To Shoot.", True ,(255,255,255))
        screen.blit(text, [35,300])
        text = font3.render("3. Shoot the colored squares to gain points.", True ,(255,255,255))
        screen.blit(text, [35,350])
        text = font3.render("4. Certain Powerups Are Collected From Enemies", True ,(255,255,255))
        screen.blit(text, [35,400])
        text = font3.render("When Killed. Flashing Colors Square = Invincible", True ,(255,255,255))
        screen.blit(text, [35,450])
        text = font3.render("Blue Square = Wall Bounce Pellets", True ,(255,255,255))
        screen.blit(text, [35,500])
        text = font3.render("6. Survive Until You Are Out Of Lives.", True ,(255,255,255))
        screen.blit(text, [35,550])

        text = font1.render(menuButton2.text, True, (menuButton2.colour))
        screen.blit(text, [menuButton2.x + 32, menuButton2.y + 20])

        if mouseX >= menuButton2.x and mouseX <= menuButton2.x + menuButton2.w and mouseY >= menuButton2.y and mouseY <= menuButton2.y + menuButton2.h:
            pygame.draw.polygon (screen, (255,255,255), [(menuButton2.x + 13, menuButton2.y + 43), (menuButton2.x + 13,menuButton2.y + 33), (menuButton2.x + 18,menuButton2.y + 38)])

    elif gameState == "name":
        screen.fill ((0,0,0))
        pygame.draw.rect (screen, (255,255,255),[193,140,620,450])
        pygame.draw.rect (screen, (0,0,0),[203,150,600,430])
        text = font1.render("Enter Your Name:", True ,(255,255,255))
        screen.blit(text, [300,200])
        nameString = 450
        for i in range (len(name)):
            text = font3.render(name[i], True ,(255,255,255))
            screen.blit(text, [nameString,275])
            nameString = nameString + 30
            
    # ===================== PYGAME STUFF (NO NOT EDIT) ===================== #
    pygame.display.flip()
    pygame.time.delay(8)
