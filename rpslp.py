import random

game_options = ['Rock', 'Paper', 'Scissors', 'Lizard', 'Spock']

# rock breaks scissors
# rock smushes lizard
# paper disproves spock
# paper covers rock
# scissors decapitates lizard
# scissors cuts paper
# spock smashes scissors
# spock vaporizes rock
# lizard eats paper
# lizard poisions spock


def player_choice():
    player_picked = str(input("Enter Rock (r), Paper (p), Scissors (s), Lizard (l) or Spock (v):  ")).capitalize()
    if player_picked == "R":
        print("You picked: " + game_options[0])
    elif player_picked == "P":
         print("You picked: " + game_options[1])
    elif player_picked == "S":
        print("You picked: " + game_options[2])
    elif player_picked == "L":
        print("You picked: " + game_options[3])
    elif player_picked == "V":
        print("You picked: " + game_options[4])
    else:
        print("Invalid input")
        player_picked = str(input("Enter Rock (r), Paper (p), Scissors (s), Lizard (l) or Spock (v):  ")).capitalize()


def win_conditions(player_choice, ai_choice):
    if player_choice == game_option[0]:
        print("You picked: " + game_options[0])
        if ai_choice == game_option[1]:
            print("Computer picked: " + game_options[1])
            print(game_option[1] + "covers" + game_option[0] + "Computer wins!")
        elif ai_choice == game_option[3]:
    else:
        print("Lost my mind")

# AI picks a choice at random from the player_pieces list
def ai_choice():
    random_choice = random.choice(game_options)
    print("The Computer picked: " + random_choice)


def main():

    print("""
    # Rock, Paper, Scissors, Lizard, Spock!
    \n
    SCISSORS cuts PAPER covers ROCK crushes
    LIZARD poisons SPOCK smashes SCISSORS
    decapitakes LIZARD eats PAPER disproves
    SPOCK vaporizes ROCK crushes SCISSORS.
    """)
    player_choice()
    ai()


if __name__ == "__main__":
    main()