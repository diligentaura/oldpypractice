def isNumber(s):
    try:
        int(s)
        return True
    except:
        return False
    
print ("")
print ("")
print ("Welcome to the Library Book Reading Club!")

readers = []
class Reader():
    name = numOfBooks = 0

#Option Selection
while True:
    print ("")
    print ("")
    print ("")
    print ("="*29)
    print ("| " + "1: " +"Enter/Edit Book Totals " + "|")
    print ("| " + "2: " +"Display Summary " .ljust (23) + "|")
    print ("| " + "3: " +"Quit " .ljust (23) + "|")
    print ("="*29)

    while True:
        option = input ("Choose an option: ")
        if isNumber (option) == True and (option) == "1" or (option) == "2" or (option) == "3":
            break

        else:
            print ("Invalid option")
            
    #Option 1
    if option == "1":
        count = 0
        print ("")
        readerName = input ("Enter name: ")
        reader = Reader()
        reader.name = readerName
        while True:
            booksRead = input ("Enter number of books " + readerName + " read: ")
            
                
            if isNumber (booksRead) == True and int(booksRead) >= 0:
                break

            else:
                print ("Invalid number of books")
                
        reader.numOfBooks = booksRead
        for i in range (len(readers)):
            if readerName == readers[i].name:
                readers[i].numOfBooks = str(int(booksRead) + int(readers[i].numOfBooks))
                count = count + 1

                


        if count == 0:
            readers.append (reader)
            
    #Option 2
    elif option == "2":
        print ("")
        print ("")
        print ("")
        print ("" .ljust (10) + "-"*29)
        print ("" .ljust (20) + "SUMMARY")
        print ("" .ljust (10) + "-"*29)
        print ("" .ljust(10) + "NAME" .ljust (14) + "BOOKS")
        for i in range (len (readers)):
            print ("" .ljust(10) + readers[i].name .ljust (14) + readers[i].numOfBooks)

        print ("" .ljust (10) + "-"*29)

    #Option 3
    else:
        print ("")
        print ("")
        print ("Thank you for using the Library program")
        print ("")
        input ("<Hit ENTER to exit>")
        break
