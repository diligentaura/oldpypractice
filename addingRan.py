import random

amtPlayed = 0
amtGuessTotal = 0

while True:
    
    amtPlayed = amtPlayed + 1
    
    secret = random.randint (1,10)
    
    amtGuess = 0
    
    while True:
        
        guess = int (input ("Enter Guess:"))
        
        amtGuess = amtGuess + 1

        if guess < secret:
            print ("Too Low!")
            
        elif guess > secret:
            print ("Too High!")
            
        else:
            break

    print ("You Got It!")
    
    print ("The amount of guesses you took is: " + str (amtGuess))
    amtGuessTotal = amtGuessTotal + amtGuess
    playAgain = input ("Do you want to play again?:")
    
    playAgain = playAgain.upper()
    
    if playAgain == "NO":
        amtGuessAvg = (amtGuessTotal)/(amtPlayed)
        print ("You played the game: " + str (amtPlayed) + " times!")
        print ("The average amount of guesses it took for you is: " + str (amtGuessAvg))
        print ("Goodbye!")
        break
    
    else:
        
        print ("Okay, restarting the game!")

