import random
target = random.randint(1,100)
while True:

    userChoice = input("Guess the number: ")
    if(userChoice=="Q"):
        break
    userChoice = int(userChoice)
    if (userChoice == target):
        print("Success: correct Guess!")
        break
    elif(userChoice < target):
        print("your number is too small! Guess bigger")
    else:
        print("your number is too big! Guess smaller")

print("----GAME OVER----")