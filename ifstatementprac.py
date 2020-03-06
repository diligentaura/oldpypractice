#If Statement Practice

#Lower Number Calc
number1 = input ("Give me a number:")
number2 = input ("Give me another one:")

if int (number1) > int (number2):
    print ("The number that is the smallest is:" + str (number2))
    
else:
    print ("The number that is the smallest is:" + str (number1))
print ("")
print ("")

#Homework/Chores Check
homeworkdone = input ("Is your homework done?:")
choresdone = input ("And are your chores done?:")

if homeworkdone == "no" and choresdone == "no":
    print ("Then GO AND DO YOUR HOMEWORK AND CHORES!")

elif choresdone == "no":
    print ("GO AND DO YOUR CHORES!")

elif homeworkdone == "no":
    print ("GO AND DO YOUR HOMEWORK!")

else:
    print ("You can go to the party!")
    
print ("")
print ("")

#Odd or Even
numberoe = input ("Give me a number:")
if int (numberoe) % 2 == 0:
    print ("That number is even!")
    
else:
    print ("That number is odd")
    
print ("")
print ("")

#Secret Words
print ("I have three secret words.")
print ("Try to guess them.")
print ("Hints:")
print ("The first is the color of the sky.")
print ("The second is something you put on your face.")
print ("The final is a social occasion with special entertainments or performances.")

secret1 = input ("Type one word:")
secret2 = input ("Type the second word:")
secret3 = input ("Type the last word:")

if secret1 == "blue":
    guess1 = 1
else:
    guess1 = 0
    
if secret1 == "mask":
    guess1 = 1
else:
    guess1 = 0
    
if secret1 == "gala":
    guess1 = 1
else:
    guess1 = 0
    
if secret2 == "blue":
    guess2 = 1
else:
    guess2 = 0

if secret2 == "mask":
    guess2 = 1
else:
    guess2 = 0
    
if secret1 == "gala":
    guess2 = 1
else:
    guess2 = 0
    
if secret1 == "blue":
    guess3 = 1
else:
    guess3 = 0
    
if secret1 == "mask":
    guess3 = 1
else:
    guess3 = 0

if secret3 == "gala":
    guess3 = 1
else:
    guess3 = 0
        
guesssum = guess1 + guess2+ guess3

if guesssum == 3:
    print ("You got: " + str (guesssum))
    print ("Congratulations you got all three!")
elif guesssum == 0:
    print ("You got: " + str (guesssum))
    print ("Try harder!")
else:
    print ("You got: " + str (guesssum))
