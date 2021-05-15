#A Number Guessing Game
import random
import time

print("[----------------Number Guessing Game----------------]")
time.sleep(0.5)
print("Hey there! What's your name?")
name = input().capitalize()
time.sleep(1)

def introduction(name):
    print("\nWell, " + name + ", I am thinking of a number between 1 and 20.")
    time.sleep(0.5)
    print("You have 6 guesses to guess it correctly.\n")

def startGame():
    print("Time to start guessing..")
    time.sleep(1)
    for guesses in range(1, 7):
        guess = int(input("Guess -> "))
        if guess > secretNumber:
            print("Too high!\n")
        elif guess < secretNumber:
            print("Too low!\n")
        else:
            if guess == secretNumber:
                print("Congratulations %s!! You guessed the number in %s guesses!" %(name, guesses))
                break
            else:
                print("Aw noo! I was thinking of %s." %(secretNumber))
                break



introduction(name)
secretNumber = random.randint(1, 20)
time.sleep(1.5)
startGame()
time.sleep(2)