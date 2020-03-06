def isNumber (s):
    try:
        int(s)
        return True
    
    except:
        return False

num = input ("Guess my fav number:")

if isNumber (num) == True:
    
    if int(num) == 12:
        print ("NAILED IT!")
        
    elif int(num) == 11 or int (num) == 13:
        print ("So Close")
        
    else:
        print ("Wrong")

else:
    print ("Ha, you didn't eneter a number!")
    
