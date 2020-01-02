import random

print("welcome in the number guessing game...!")
number = random.randint(1, 50)

tries = 0

while tries <= 10:
    guess = int(input("Enter your guess(choose number in between 1 to 50): "))
    if guess == number:
        print("your guess is correct")
        break
    elif guess < number:
        print("your guess is to low..!")
    elif guess > number:
        print("your guess is to high..!")
    tries += 1

print("better luck next time..!")
