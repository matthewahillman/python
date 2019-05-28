import random

random_number = random.randint(1, 10)

user = int(input("Guess the number: "))

while user != random_number:
    if user > random_number:
        print("Try again number was too high!")
    else:
        print("Try again number was too low!")
    user = int(input("Guess the number: "))
print("Well done!")
