#Loop Challenges

#First Challenges

print ("Challenge 1,1")
for i in range (20):
        print (i)
print ("")
       
print ("Challenge 1,2")
for i in range (20):
    if i != 5:
        print (i)
print ("")
       
print ("Challenge 1,3")
for i in range (20):
    if i != 5 and i != 9 and i != 11 and i != 15 :
        print (i)
print ("")
       
print ("Challenge 1,4")
for i in range (20):
    if i % 2==0:
        print (i)
print ("")
       
print ("Challenge 1,5")
for i in range (20):
    if i % 2!=0:
        print (i)
print ("")
       
print ("Challenge 1,6")
for i in range (0,20,3):
        print (i)
print ("")
       
print ("Challenge 1,7")        
for i in range (0,20,7):
        print (i)
print ("")
       
#Second Challenges

print ("Challenge 2,1")
loopNum = 0
for loopNum in range (2,10):
        loopNum + 1
print (loopNum)
print ("")

print ("Challenge 2,2")
loopNum = 0
for i in range (2,10):
        loopNum = int(loopNum) + 1
        if loopNum != (5):
                print (i)
        
print ("")

print ("Challenge 2,3")
loopNum = 0
for i in range (2,10):
        loopNum = int(loopNum) + 1
        if loopNum != (3) and loopNum != (7):
                print (i)
print ("")

print ("Challenge 2,4")
iTwo = 0
for i in range (1,2):
       iTwo = i + iTwo
print (iTwo)
        
print ("")

#Third Challenge

print ("Challenge 3")


total1= 0

for i in range (5):
        
        total = input ("Enter your number: ")
        
        if total1 == 0:
                total1 = total
                
        if int (total) > int(total1):
               total1 = total
               
print (total1)
