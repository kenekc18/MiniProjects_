import random
targetNumber = random.randrange(1,10)
print(targetNumber)

while True:
    guessedNumber = int(input("Enter a number between 1 and 10:"))
    if guessedNumber == targetNumber:
        print("Congratulations you guessed the right number")
    elif guessedNumber < targetNumber:
        print("The number is too low")
        print("Try again")
    elif guessedNumber > targetNumber:
        print("The number is too high")
        print("Try again")
    
    
