import random

number = input ("Your Number:")
x = 0
while True:
    num = random.randint (1,100000)
    print (num)
    x=x+1

    print 
    if num == int (number):
        break
print ("Number of Times:")
print ("")
print (x)
