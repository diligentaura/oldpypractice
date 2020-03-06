def isNumber(s):
    try:
        int(s)
        return True
    except:
        return False


#Challenge 1
myList = []

for i in range (1):
    item = input ("Give me a number: ")
    myList.append (int(item))

print("Your numbers are: ")
for item in myList:
    print(item)
print("")
print("")

print("Your numbers are: ")
for i in range (len(myList)):
    print (myList[i])
print("")
print("")

#Challenge 2
myList = []

for i in range (1):
    item = input ("Give me a number: ")
    myList.append (int(item))
    
for i in range (len(myList)-1,-1,-1):
    print(myList[i])
print("")
print("")

myList = []
for i in range (1):
    item = input ("Give me a number: ")
    myList.insert (0,item)

for i in range (len(myList)):
    print(myList[i])
print("")
print("")

#Challenge 3
myList = []

for i in range (10):
    item = input ("Give me the " + str(i+1) + " item: ")
    myList.append (item)
    
recall = input ("What Items Would You Like to Recall: ")
if recall in myList:
    for item in myList:
        print (item)
        if recall == item:
            break

recall = input ("What Items Would You Like to Recall: ")
if recall in myList:
    for i in range (len(myList)):
        print (myList[i])
        if myList[i] == recall:
            break


#Challenge 4
numbers = []

for i in range (10):
    number = input ("Enter a number: ")
    number = int(number)
    numbers.append (number)
    
cutOff = input ("Enter a cutoff number: ")
cutOff = int(cutOff)

for i in range (len(numbers)-1,-1,-1):
    if (numbers[i]) > cutOff:
        numbers.remove (numbers[i])

for i in range (len(numbers)):
    print(numbers[i])
print("")
print("")

