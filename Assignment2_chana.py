#Assignment 2
#Andy Chan

#Enter Information
print ("Welcome to the Rental Company Program")
name = input (("Enter name:" .ljust (11)) .ljust (15))
address = input (("Enter address:" .ljust (11)) .ljust (15))
city = input  (("Enter city:" .ljust (11)) .ljust (15))
print ("")

#Enter Odometer Readings
beginOdoRead = input (("Beginning Odometer Reading:") .ljust (30))
endOdoRead = input (("Ending Odometer Reading:") .ljust (30))
numDaysRented = input (("Number of days rented:") .ljust (30))
print ("")
print ("")

#Variables
numKmDriven = int (endOdoRead) - int (beginOdoRead)
numKmCharge = 0.12 * numKmDriven
numChargeDays = int (numDaysRented) * 15
subtotal = numKmCharge + numChargeDays
hst = subtotal * 0.13
total = subtotal + hst
roundedTotal = ("%0.2f" % total)

#Title
print (("="*31) .center (52))
print ("" .ljust (10) + "SUMMARY OF CHRAGES")
print (("="*31) .center (52))

#KM Driven
print ("" .ljust (10) + "Number of KM Driven" .ljust (22) + str ("%0.2f" % numKmDriven) .rjust (len (str(roundedTotal))))

#KM Charge
print ("" .ljust (10) + "Charge for KM" .ljust (22) + "$" + str ("%0.2f" % numKmCharge) .rjust (len (str(roundedTotal))))

#Day Charge
print ("" .ljust (10) + "Charge for Days" .ljust (22) + "$" + str ("%0.2f" % numChargeDays) .rjust (len (str(roundedTotal))))
print (("="*31) .center (52))


#Subtotal+HST
print ("" .ljust (10) + "Subtotal" .ljust (22) + "$" + str ("%0.2f" % subtotal) .rjust (len (str(roundedTotal))))
print ("" .ljust (10) + "HST" .ljust (22) + "$" + str ("%0.2f" % hst) .rjust (len (str(roundedTotal))))
print (("="*31) .center (52))


#Total
print ("" .ljust (10) + "TOTAL" .ljust (22) + "$" + str ("%0.2f" % total) .rjust (len (str(roundedTotal))))

