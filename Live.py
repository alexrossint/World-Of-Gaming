import MemoryGame

def welcome(name):
    return (
        "Hello " + name + " and welcome to the World of Games (WoG).\n"
        "Here you can find many cool games to play."
    )

def load_game(name):
    # Starting a loop
    while True:
        print()
        # Loading game menu to choose a game:
        print("Please choose a game to play:")
        print("1. Memory Game: repeat a sequence of numbers shown for 0.7 seconds")
        print("2. Guess Game: guess the computer's secret number")
        print("3. Currency Roulette: estimate the ILS value of a random USD amount")
        print("4. Exit")
        print()

        # Player input choice
        game_input = input("Your choice: ")
        print()

        # Check if the choice is correct
        try:
            chosen_game = int(game_input)
            if chosen_game >= 1 and chosen_game <=4:
                break
            else:
                print("Not exists!!!")
        except ValueError:
            print()

    # Next we print the game the player chose
    if chosen_game == 1:
        print("Welcome to Memory Game")
    elif chosen_game == 2:
        print("Welcome to Guess Game")
    elif chosen_game == 3:
        print("Welcome to Currency Roulette")
    else:
        print()
        print(f"Thank you {name} for playing! See you again!")
        print()
        return False

    # Now comes the game difficulty prompt
    while True:
        difficulty_input = input("Choose a difficulty level from 1 to 5: ")
        try:
            chosen_difficulty = int(difficulty_input)
            if chosen_difficulty >=1 and chosen_difficulty <= 5:
                break
            else:
                print()
        except ValueError:
            print()

    if chosen_game == 1:
        result = MemoryGame.play(chosen_difficulty)
        if result:
            print("Correct!")
        else:
            print("Sorry. Try again!")
    return True