#Andy Chan
#Assignment 3

#Question 1
print ("=" *33 + " Question 1 " + "=" * 29)
age1 = input ("Enter your age:")
if int (age1) < 50:
    print ("You are young!")
else:
    print ("You are old!")
print ("")

#Question 2
print ("=" *33 + " Question 2 " + "=" * 29)
age2 = input ("Enter your age:")

if int (age2) > 100 or int (age2) < 1:
    print ("Invalid Age")

elif int (age2) <= 13 and int (age2) >= 6:
    print ("Ticket price: $7.00")

elif int (age2) > 65:
    print ("Ticket price: $10.00")

elif int (age2) <= 5:
    print ("Ticket price: FREE!!")

else:
    print ("Ticket price: $12.00")

#Question 3
print ("=" *33 + " Question 3 " + "=" * 29)
number1 = input ("Enter number 1:")
number2 = input ("Enter number 2:")
number3 = input ("Enter number 3:")

if int (number1) > int (number2) and int (number1) > int (number3):
    print (number1)

elif int (number2) > int (number1) and int (number2) > int (number3):
    print (number2)
    
elif int (number3) > int (number1) and int (number3) > int (number2):
    print (number3)

#Question 4
print ("=" *33 + " Question 4 " + "=" * 29)
mondayday = 4
tuesdayday = 3
wednesdayday = 2
thursdayday = 1
fridayday = 0
saturdayday = 6
sundayday = 5
dayofweek = input ("Enter day:")
dayofweekcaps = dayofweek.upper()

if dayofweekcaps == "MONDAY":
    print (str (mondayday) + " days until Friday!!")
    
elif dayofweekcaps == "TUESDAY":
    print (str (tuesdayday) + " days until Friday!!")

elif dayofweekcaps == "WEDNESDAY":
    print (str (wednesdayday) + " days until Friday!!")

elif dayofweekcaps == "THURSDAY":
    print (str (thursdayday) + " days until Friday!!")

elif dayofweekcaps == "FRIDAY":
    print (str (fridayday) + " days until Friday!!")

elif dayofweekcaps == "SATURDAY":
    print (str (saturdayday) + " days until Friday!!")

elif dayofweekcaps == "SUNDAY":
    print (str (sundayday) + " days until Friday!!")

else:
    print ("Invalid Day")

