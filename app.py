import random

target = random.randint(1, 20)
print(target)

name = input(str("Tell Me Your Name:"))
guesses = []

def gess():
    guess = 0
    guesses.append(guess)
    if len(guesses) < 2:
        guess = int(input(f"Well, {name}, I am thinking of a number between 1 and 20.\n"))
    else:
        guess = int(input("Try again:\n"))
    

    if guess == target:
        if len(guesses) < 7:
            print("correct! you won")
        else:
            print("correct but you lost!")
    else:
    
        if guess - target > 0:
            if guess - target > 5:
                print("your guess is too high")
                gess()
            elif guess - target <= 5:
                print("your guess is high")
                gess()
        else:
            if target - guess > 5:
                print("your guess is too low")
                gess()
            elif target - guess <= 5:
                print("your guess is low")
                gess()
gess()