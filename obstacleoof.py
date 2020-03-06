import pygame,random

pygame.init()
import pygame

pygame.init()
screen = pygame.display.set_mode([550,550])
pygame.display.set_caption("Screen Proportions")

#Set up global variables
def collideRectRect (x1,y1,w1,h1,x2,y2,w2,h2):
    return x1 <= x2+ w2 and x1 + w1 >= x2 and y1 <= y2 + h2 and y1 + h1 >= y2

def collideRectRectLocation (x1,y1,w1,h1,x2,y2,w2,h2):
    if x1 <= x2+w2 and x1+w1 >= x2 and y1 <= y2+h2 and y1+h1 >= y2:
        collisionLeft = x2 + w2 - x1
        collisionRight = x1 + w1 - x2
        collisionTop = y2 + h2 - y1
        collisionBottom = y1 + h1 - y2
        if (collisionLeft <= collisionBottom and collisionLeft <= collisionTop and collisionLeft <= collisionRight):
            return "left" 
        elif (collisionRight <= collisionBottom and collisionRight <= collisionTop and collisionRight <= collisionLeft):
            return "right" 
        elif (collisionTop <= collisionBottom and collisionTop <= collisionLeft and collisionTop <= collisionRight): 
            return "top" 
        elif (collisionBottom <= collisionTop and collisionBottom <= collisionLeft and collisionBottom <= collisionRight): 
            return "bottom" 
    else:
        return "none"
    
width = screen.get_width()
height = screen.get_height()

blues = []
reds = []

class Obstacle ():
    x=y=w=h=clr=0

class Man():
    x=t=w=h=xS=yS=clr=0

for i in range (5):
    red = Man()
    red.x = random.randint (0,width)
    red.y = random.randint (0,height)
    red.w = random.randint (10,70)
    red.h = random.randint (10,70)
    red.xS = random.randint (1,9)
    red.yS = -random.randint (1,9)
    red.clr = (255,0,0)
    reds.append (red)
    
for i in range (10):
    blue = Obstacle()
    blue.x = random.randint (0,width)
    blue.y = random.randint (0,height)
    blue.w = random.randint (10,70)
    blue.h = random.randint (10,70)
    blue.clr = (0,0,255)
    blues.append (blue)

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
    for i in range (len(reds) -1,-1,-1):
        reds[i].y = reds[i].y + reds[i].yS
        reds[i].x = reds[i].x + reds[i].xS
    # ============================== COLLISION ============================== #
    for i in range (len(reds) -1,-1,-1):
        if reds[i].y <= 0:
            reds[i].yS = reds[i].yS * -1
            
        elif reds[i].y + reds[i].h >= height:
            reds[i].yS = reds[i].yS * -1

        if reds[i].x <= 0:
            reds[i].xS = reds[i].xS * -1
            
        elif reds[i].x + reds[i].w >= width:
            reds[i].xS = reds[i].xS * -1
        

    for i in range (len(blues) -1,-1,-1):
        collisionResult = collideRectRectLocation (red.x,red.y,red.w,red.h,blues[i].x,blues[i].y,blues[i].w,blues[i].h)
        if collisionResult != "none" :
            if collisionResult == "left" :
                for i in range (len(reds) -1,-1,-1):
                    reds[i].xS = reds[i].xS * -1
                reds[i].x = blues[i].x + blues[i].w
            elif collisionResult == "right" :
                for i in range (len(reds) -1,-1,-1):
                    reds[i].xS = reds[i].xS * -1
                reds[i].x = blues[i].x - reds[i].w
            elif collisionResult == "top" :
                for i in range (len(reds) -1,-1,-1):
                    reds[i].yS = reds[i].yS * -1
                reds[i].yS = blues[i].y + blues[i].h
            elif collisionResult == "bottom" :
                for i in range (len(reds) -1,-1,-1):
                    reds[i].yS = reds[i].yS * -1
                reds[i].y = blues[i].y - reds[i].h
        
    # ============================== DRAW STUFF ============================= #
    screen.fill ((255,255,255))

    for i in range (len(reds) -1,-1,-1):
        pygame.draw.rect (screen, red.clr, [red.x,red.y,red.w,red.h])

    for i in range (len(blues) -1,-1,-1):
        pygame.draw.rect (screen, blues[i].clr, [blues[i].x,blues[i].y,blues[i].w,blues[i].h])
    

    # ====================== PYGAME STUFF (DO NOT EDIT) ===================== #
    pygame.display.flip()
    pygame.time.delay(10)
    

