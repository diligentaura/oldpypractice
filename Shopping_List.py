def isNumber(s):
    try:
        int(s)
        return True
    except:
        return False

myList = []

while True:
    print ("")
    print ("".ljust(10) + "-"*50)
    print ("".ljust(10) + "1 - Print list")
    print ("".ljust(10) + "2 - Append item")
    print ("".ljust(10) + "3 - Insert item to slot")
    print ("".ljust(10) + "4 - Remove item by name")
    print ("".ljust(10) + "5 - Remove item by slot")
    print ("".ljust(10) + "-"*50)
    print ("")

    while True:        
        choice = input ("Choice: ")
        if choice == "1" or choice == "2" or choice=="3" or choice =="4" or choice =="5":
            break
        print ("Invalid choice")


    if choice == "1":
        print (myList)


    elif choice == "2":
        item = input ("Item to append: ")
        if (item) in (myList):
            myList.append (item)  
        else:
            print ("Invaild Item")


    elif choice == "3":
        slot = input("Enter slot: ")
        item = input("Enter item: ")
        if(item) in (myList):
            if isNumber (slot) == True:
                myList.insert (int(slot) , item)
            
            else:
                print("No you can't do that.")
        else:
            print ("No")

            
    elif choice == "4":
        item = input ("Item name to remove: ")
        if isNumber (item) == False:
            myList.remove (item)
        else:
            print("No you can't do that.")
            
        
    elif choice == "5":
        slot = input ("Slot to remove: ")
        if isNumber (slot) == True:
            myList.pop(int(slot))
        else:
            print("No you can't do that.")
