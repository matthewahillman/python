import random

user = ""


def easy():
    print("""
    # The Guess of Doooooom #\n
    The worst guessing game you\'ve ever played.
    By Matthew Hillman \n
    Can you beat Doom mode?
    """)
    print("Easy mode...\n")
    random_number_easy = random.randint(1, 10)
    user_easy = int(input("Guess the number between 1 and 10: "))
    while user_easy != random_number_easy:
        if user_easy > random_number_easy:
            print("Try again number was too high!")
        else:
            print("Try again number was too low!")
        user_easy = int(input("I think the number is: "))
    print("Well done!")


def choice():
    user_choice = input("Continue to certain doom? Yes/No ").upper()
    if user_choice == "YES":
        print("Walking the corridors... \n" )
    else:
        print("Going home... \n")
        exit()


def hard():
    print("Hard Mode...")
    random_number_hard = random.randint(1, 50)
    user_hard = int(input("Guess the number from 1 to 50: "))

    while user_hard != random_number_hard:
        if user_hard > random_number_hard:
            print("Try again number was too high!")
        else:
            print("Try again number was too low!")
        user_hard = int(input("I think the number is: "))
    else:
        print("Well done! Next level")


def expert():
    print("""
    Expert mode...\n
    Getting smart are we? Try this.
    """)
    random_number_expert = random.randint(1, 10000)
    user_expert = int(input("Guess the number from 1 to 10,000: "))

    while user_expert != random_number_expert:
        if user_expert > random_number_expert:
            print("Too high")
        else:
            print("Too low")
        user_expert = int(input("I think the number is: "))
    print("Congrats!")


def doom():
    print("Activating Doom Mode...")
    random_number_doom = random.randint(1, 100000)
    user_doom = int(input("Guess the number from 1 to 100,000: "))

    while user_doom != random_number_doom:
        if user_doom > random_number_doom:
            print("Too high")
        else:
            print("Too low")
        user_doom = int(input("Guess the number: "))
    print("You must be the Devil himself. Well done.")


def main():
    easy()
    choice()
    hard()
    choice()
    expert()
    choice()
    doom()


if __name__ == "__main__":
    main()
