for i in range (2000):
    
    if i >= (2):
        
        hasFactors = False
        
        for j in range (2,i):
            
            if i % j == (0):
                
                hasFactors = True
            
                break
            

        if hasFactors == False:
        
            print (i)
