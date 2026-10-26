def welcome(name):
    return (
        "Hello " + name + " and welcome to the World of Games (WoG).\n"
        "Here you can find many cool games to play."
    )

def load_game():
    # Starting a loop
    while True:
        print()
        # Loading game menu to choose a game:
        print("Please choose a game to play:")
        print("1. Memory Game: repeat a sequence of numbers shown for 0.7 seconds")
        print("2. Guess Game: guess the computer's secret number")
        print("3. Currency Roulette: estimate the ILS value of a random USD amount")
        print()

        # Player input choice
        game_input = input("Your choise: ")
        print()

        # Check if the choice is correct
        try:
            game_choice = int(game_input)
            if game_choice >= 1 and game_choice <=3:
                break
            else:
                print("Not exists!!!")
        except ValueError:
            print()

    # Next we print the game the player chose
    if game_choice == 1:
        print("Welcome to Memory Game")
    elif game_choice == 2:
        print("Welcome to Guess Game")
    else:
        print("Welcome to Currency Roulette")

    # Now comes the game difficulty prompt
    while True:
        print()
        difficulty_input = input("Choose a difficulty level from 1 to 5: ")
        try:
            difficulty_choice = int(difficulty_input)
            if difficulty_choice >=1 and difficulty_choice <= 5:
                break
            else:
                print()
        except ValueError:
            print()