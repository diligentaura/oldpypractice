#Andy Chan
#Assignment 4


#Is Number Function
def isNumber (s):
    try:
        float(s)
        return True
    
    except:
        return False

#Title and Variables
    
child = 2.00
senior = 1.75
student = 2.25
adult = 2.50

childTotal = 0
seniorTotal = 0
studentTotal = 0
adultTotal = 0

print ("Welcome to the GTC Fare Calculator and Tracker:")
print ("")

#Age Calculator

while True:
    age = input ("Enter age ("'"quit"'" to quit): ")

    if age == "quit":
        print ("Thank you for using the GTC Fare Calculator")
        input ("<Hit ENTER to exit>")
        break

    if isNumber (age) == True:

#Child Calculator
        if float(age) < 13 and float(age) > 0:
            childTotal = float(childTotal) + child
            print ("" .ljust (8) + "Fare (Children): $2.00")
            print ("")
            print ("" .ljust (8) + "TOTALS")
            print ("" .ljust (8) + "-" *16)
            print ("" .ljust (8) + "Children: " + "$" + str (("%0.2f" % childTotal)))
            print ("" .ljust (8) + "Students: " + "$" + str (("%0.2f" % studentTotal)))
            print ("" .ljust (8) + "Adults: " .ljust (10) + "$" + str (("%0.2f" % adultTotal)))
            print ("" .ljust (8) + "Seniors: " .ljust (10) + "$" + str (("%0.2f" % seniorTotal)))
            print ("")

#Student Calculator
        elif float(age) >= 13 and float(age) <= 18:
            studentTotal = float(studentTotal) + student
            print ("" .ljust (8) + "Fare (Student): $2.25")
            print ("")
            print ("" .ljust (8) + "TOTALS")
            print ("" .ljust (8) + "-" *16)
            print ("" .ljust (8) + "Children: " + "$" + str (("%0.2f" % childTotal)))
            print ("" .ljust (8) + "Students: " + "$" + str (("%0.2f" % studentTotal)))
            print ("" .ljust (8) + "Adults: " .ljust (10) + "$" + str (("%0.2f" % adultTotal)))
            print ("" .ljust (8) + "Seniors: " .ljust (10) + "$" + str (("%0.2f" % seniorTotal)))
            print ("")

#Adult Calculator
        elif float(age) > 18 and float(age) < 65:
            adultTotal = float(adultTotal) + adult
            print ("" .ljust (8) + "Fare (Adult): $2.50")
            print ("")
            print ("" .ljust (8) + "TOTALS")
            print ("" .ljust (8) + "-" *16)
            print ("" .ljust (8) + "Children: " + "$" + str (("%0.2f" % childTotal)))
            print ("" .ljust (8) + "Students: " + "$" + str (("%0.2f" % studentTotal)))
            print ("" .ljust (8) + "Adults: " .ljust (10) + "$" + str (("%0.2f" % adultTotal)))
            print ("" .ljust (8) + "Seniors: " .ljust (10) + "$" + str (("%0.2f" % seniorTotal)))
            print ("")
            
#Senior Calculator     
        elif float(age) >= 65 and float(age) <= 100:
            seniorTotal = float(seniorTotal) + senior
            print ("" .ljust (8) + "Fare (Senior): $1.75")
            print ("")
            print ("" .ljust (8) + "TOTALS")
            print ("" .ljust (8) + "-" *16)
            print ("" .ljust (8) + "Children: " + "$" + str (("%0.2f" % childTotal)))
            print ("" .ljust (8) + "Students: " + "$" + str (("%0.2f" % studentTotal)))
            print ("" .ljust (8) + "Adults: " .ljust (10) + "$" + str (("%0.2f" % adultTotal)))
            print ("" .ljust (8) + "Seniors: " .ljust (10) + "$" + str (("%0.2f" % seniorTotal)))
            print ("")
            
        else:
            print ("" .ljust (8) + "Invalid age(age must 1 - 100)")

    if isNumber (age) == False:
        print ("Age must be a number")


        
    
