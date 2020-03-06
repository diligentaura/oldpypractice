import pygame

pygame.init()
screen = pygame.display.set_mode([600,500])
pygame.display.set_caption("My First Game!")

#Set up global variables

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

    # ============================== COLLISION ============================== #

    # ============================== DRAW STUFF ============================= #
    #Moon
    grassX = 0
    screen.fill ((75,75,75))
    pygame.draw.ellipse (screen, (255,255,255),[450,30,110,110]) 
    pygame.draw.ellipse (screen, (75,75,75),[450,30,100,100])
    
    #Buildings
    pygame.draw.rect (screen, (0,0,0),[15,300,20,200])
    pygame.draw.rect (screen, (0,0,0),[50,350,40,150])
    pygame.draw.rect (screen, (0,0,0),[120,290,30,210])
    pygame.draw.rect (screen, (0,0,0),[170,275,50,225])
    pygame.draw.rect (screen, (0,0,0),[240,325,20,175])
    pygame.draw.rect (screen, (0,0,0),[285,285,30,215])
    pygame.draw.rect (screen, (0,0,0),[330,200,50,300])
    pygame.draw.rect (screen, (0,0,0),[390,250,15,250])
    pygame.draw.rect (screen, (0,0,0),[420,460,40,40])
    pygame.draw.rect (screen, (0,0,0),[415,460,50,10])
    pygame.draw.rect (screen, (0,0,0),[490,450,50,50])
    pygame.draw.rect (screen, (0,0,0),[485,450,60,10])
    pygame.draw.rect (screen, (0,0,0),[560,470,30,30])
    pygame.draw.rect (screen, (0,0,0),[555,470,40,10])
    

    #Grass
    pygame.draw.rect (screen, (0,128,0),[0,497,1000,3])
    
    for i in range (1000):
        pygame.draw.rect (screen, (0,128,0), [grassX,493,2,7])
        grassX = grassX + 3
        
    #Building 1 Windows
    windowY = 302
    for i in range (48):
        pygame.draw.rect (screen, (255,255,0), [17,windowY,2,2])
        windowY = windowY + 4
        
    windowY = 302
    for i in range (38):
        pygame.draw.rect (screen, (255,255,0), [21,windowY,2,2])
        windowY = windowY + 4
        
    windowY = 302
    for i in range (30):
        pygame.draw.rect (screen, (255,255,0), [25,windowY,4,2])
        windowY = windowY + 4
        
    windowY = 302
    for i in range (24):
        pygame.draw.rect (screen, (255,255,0), [31,windowY,2,2])
        windowY = windowY + 4

    #Building 2 Windows
    windowY = 352
    for i in range (36):
        pygame.draw.rect (screen, (255,255,0), [53,windowY,4,2])
        windowY = windowY + 4
        
    windowY = 352
    for i in range (32):
        pygame.draw.rect (screen, (255,255,0), [59,windowY,4,2])
        windowY = windowY + 4
        
    windowY = 352
    for i in range (28):
        pygame.draw.rect (screen, (255,255,0), [65,windowY,4,2])
        windowY = windowY + 4
        
    windowY = 352
    for i in range (22):
        pygame.draw.rect (screen, (255,255,0), [71,windowY,4,2])
        windowY = windowY + 4

    windowY = 352
    for i in range (18):
        pygame.draw.rect (screen, (255,255,0), [77,windowY,4,2])
        windowY = windowY + 4
        
    windowY = 352
    for i in range (15):
        pygame.draw.rect (screen, (255,255,0), [83,windowY,4,2])
        windowY = windowY + 4

    #Building 3 Windows
    windowY = 292
    for i in range (50):
        pygame.draw.rect (screen, (255,255,0), [122,windowY,2,2])
        windowY = windowY + 4
        
    windowY = 292    
    for i in range (47):
        pygame.draw.rect (screen, (255,255,0), [126,windowY,2,2])
        windowY = windowY + 4
        
    windowY = 292
    for i in range (39):
        pygame.draw.rect (screen, (255,255,0), [130,windowY,2,2])
        windowY = windowY + 4
        
    windowY = 292
    for i in range (33):
        pygame.draw.rect (screen, (255,255,0), [134,windowY,2,2])
        windowY = windowY + 4
        
    windowY = 292
    for i in range (26):
        pygame.draw.rect (screen, (255,255,0), [138,windowY,2,2])
        windowY = windowY + 4
        
    windowY = 292
    for i in range (19):
        pygame.draw.rect (screen, (255,255,0), [142,windowY,6,2])
        windowY = windowY + 4

    #Building 4 Windows
    windowY = 277
    for i in range (54):
        pygame.draw.rect (screen, (255,255,0), [172,windowY,6,2])
        windowY = windowY + 4
        
    windowY = 277
    for i in range (47):
        pygame.draw.rect (screen, (255,255,0), [180,windowY,6,2])
        windowY = windowY + 4
        
    windowY = 277
    for i in range (40):
        pygame.draw.rect (screen, (255,255,0), [188,windowY,6,2])
        windowY = windowY + 4
        
    windowY = 277
    for i in range (45):
        pygame.draw.rect (screen, (255,255,0), [196,windowY,6,2])
        windowY = windowY + 4
        
    windowY = 277
    for i in range (32):
        pygame.draw.rect (screen, (255,255,0), [204,windowY,6,2])
        windowY = windowY + 4
        
    windowY = 277
    for i in range (26):
        pygame.draw.rect (screen, (255,255,0), [212,windowY,2,2])
        windowY = windowY + 4
        
    windowY = 277
    for i in range (22):
        pygame.draw.rect (screen, (255,255,0), [216,windowY,2,2])
        windowY = windowY + 4

    #Building 5 Windows
    windowY = 327
    for i in range (41):
        pygame.draw.rect (screen, (255,255,0), [242,windowY,2,2])
        windowY = windowY + 4
        
    windowY = 327
    for i in range (36):
        pygame.draw.rect (screen, (255,255,0), [246,windowY,2,2])
        windowY = windowY + 4
        
    windowY = 327
    for i in range (31):
        pygame.draw.rect (screen, (255,255,0), [250,windowY,2,2])
        windowY = windowY + 4
        
    windowY = 327
    for i in range (24):
        pygame.draw.rect (screen, (255,255,0), [254,windowY,4,2])
        windowY = windowY + 4

    #Building 6 Windows
    windowY = 287
    for i in range (52):
        pygame.draw.rect (screen, (255,255,0), [287,windowY,2,2])
        windowY = windowY + 4
        
    windowY = 287
    for i in range (46):
        pygame.draw.rect (screen, (255,255,0), [291,windowY,2,2])
        windowY = windowY + 4
        
    windowY = 287
    for i in range (40):
        pygame.draw.rect (screen, (255,255,0), [295,windowY,2,2])
        windowY = windowY + 4
        
    windowY = 287
    for i in range (32):
        pygame.draw.rect (screen, (255,255,0), [299,windowY,2,2])
        windowY = windowY + 4
        
    windowY = 287
    for i in range (28):
        pygame.draw.rect (screen, (255,255,0), [303,windowY,2,2])
        windowY = windowY + 4
        
    windowY = 287
    for i in range (24):
        pygame.draw.rect (screen, (255,255,0), [307,windowY,6,2])
        windowY = windowY + 4

    #Building 7 Windows
    windowY = 202
    for i in range (73):
        pygame.draw.rect (screen, (255,255,0), [332,windowY,8,2])
        windowY = windowY + 4
        
    windowY = 202
    for i in range (67):
        pygame.draw.rect (screen, (255,255,0), [342,windowY,8,2])
        windowY = windowY + 4
        
    windowY = 202
    for i in range (60):
        pygame.draw.rect (screen, (255,255,0), [352,windowY,8,2])
        windowY = windowY + 4
        
    windowY = 202
    for i in range (52):
        pygame.draw.rect (screen, (255,255,0), [362,windowY,8,2])
        windowY = windowY + 4

    windowY = 202
    for i in range (45):
        pygame.draw.rect (screen, (255,255,0), [372,windowY,2,2])
        windowY = windowY + 4
        
    windowY = 202
    for i in range (39):
        pygame.draw.rect (screen, (255,255,0), [376,windowY,2,2])
        windowY = windowY + 4

    #Building 8 Windows
    windowY = 252
    for i in range (60):
        pygame.draw.rect (screen, (255,255,0), [392,windowY,2,2])
        windowY = windowY + 4
        
    windowY = 252
    for i in range (52):
        pygame.draw.rect (screen, (255,255,0), [396,windowY,3,2])
        windowY = windowY + 4
        
    windowY = 252
    for i in range (44):
        pygame.draw.rect (screen, (255,255,0), [401,windowY,2,2])
        windowY = windowY + 4

    
    
    
    
    

    # ====================== PYGAME STUFF (DO NOT EDIT) ===================== #
    pygame.display.flip()
    pygame.time.delay(20)
