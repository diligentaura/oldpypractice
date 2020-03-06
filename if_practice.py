#if_practice

age = input ("Enter age:")
age = int (age)

if age < 10:
    print ("Child")
    print ("Let's Play a Game")
    rps = input ("Rock, Paper or Scissors?")
    if rps == ("paper"):
        print ("Scissors")
        print ("I Win")
    if rps == ("rock"):
        print ("Paper")
        print ("I Win")
    if rps == ("scissors"):
        print ("Rock")
        print ("I Win")
elif age < 20:
    print ("Teen")
    print ("Let's Play a Game")
    rps = input ("Rock, Paper or Scissors?")
    if rps == ("paper"):
        print ("Scissors")
        print ("I Win")
    if rps == ("rock"):
        print ("Paper")
        print ("I Win")
    if rps == ("scissors"):
        print ("Rock")
        print ("I Win")
elif age < 50:
    print ("Adult")
    print ("Let's Play a Game")
    rps = input ("Rock, Paper or Scissors?")
    if rps == ("paper"):
        print ("Scissors")
        print ("I Win")
    if rps == ("rock"):
        print ("Paper")
        print ("I Win")
    if rps == ("scissors"):
        print ("Rock")
        print ("I Win")
else:
    print ("Senior")
    print ("Let's Play a Game")
    rps = input ("Rock, Paper or Scissors?")
    if rps == ("paper"):
        print ("Scissors")
        print ("I Win")
    if rps == ("rock"):
        print ("Paper")
        print ("I Win")
    if rps == ("scissors"):
        print ("Rock")
        print ("I Win")
