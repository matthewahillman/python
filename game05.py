import random


def choice():
    user_choice = input("Continue to certain doom? Yes/No ").upper()
    if user_choice == "YES" or user_choice == 'Y':
        print("Walking the corridors... \n")
        return True
    else:
        print("Going home... \n")
        return False


def guess_loop(limit):
    random_number = random.randint(1, limit)

    while True:
        try:
            guess = int(input("Guess the number: "))
            break
        except BaseException as err:
            print("\nInvalid character found, please try again\n")
            continue
    while guess != random_number:
        if guess > random_number:
            print("\nTry again number was too high!")
        else:
            print("\nTry again number was too low!")
        guess = int(input("I think the number is: "))


def main():
    all_levels = [
        {
            'name': 'Easy mode...',
                    'limit': 10
        },
        {
            'name': 'Hard mode...',
                    'limit': 100
        },
        {
            'name': 'expert mode...',
                    'limit': 1000
        },
        {
            'name': 'DOOM mode...',
                    'limit': 10000
        },
        {
            'name': 'DEATH mode...',
            'limit': 100000
        }
    ]

    print("""
# The Guess of Doooooom #\n
The worst guessing game you\'ve ever played.
By Matthew Hillman \n
Will it be impossible to beat? Find out.
\nOpening doors to possible death...please wait...
""")

    for level in all_levels:
        # print 'level name 1 to level limit
        print('{} 1 to {}'.format(level['name'], level['limit']))
        guess_loop(level['limit'])
        print('\nCongratulations; you beat {}!\n'.format(level['name']))
        if choice() != True:
            break


if __name__ == "__main__":
    main()
