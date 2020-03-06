#Practice Input Thingy

#name
name = input ("Please enter your name:")
print ("")

#grade input
grade1 = input (name + " please enter your 1st Grade:")
grade2 = input (name + " please enter your 2nd Grade:")
grade3 = input (name + " please enter your 3rd Grade:")
grade4 = input (name + " please enter your 4th Grade:")
grade5 = input (name + " please enter your 5th Grade:")
grade6 = input (name + " please enter your 6th Grade:")
grade7 = input (name + " please enter your 7th Grade:")
grade8 = input (name + " please enter your 8th Grade:")
print ("")

#gradeSum
gradeSum = (int (int (grade1) + int (grade2) + int (grade3) + int (grade4) + int (grade5) + int (grade6) + int (grade7) + int (grade8)))

#grade print and gradeAvg
print ("Here are the sum of all your grades, " + name + ": " + str (gradeSum))
gradeAvg = (int (gradeSum)/8)
print ("")
gradeAvgRound = ("%0.2f" % gradeAvg)
print ("Here is the average of all your grades, " + name + ": " + str (gradeAvgRound))
