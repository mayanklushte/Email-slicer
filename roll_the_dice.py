import random

a = "y"

while a == "y":
    a = input("you want to roll the dice again:")
    print("rolling the dice..")
    r_d = random.randint(1, 6)
    print("The value is:", r_d)
