def welcome(name):
    return (
        "Hello " + name + " and welcome to the World of Games (WoG).\n"
        "Here you can find many cool games to play."
    )

def load_game():
    while True:
        print()
        print("Please choose a game to play:")
        print("1. Memory Game: repeat a sequence of numbers shown for 0.7 seconds")
        print("2. Guess Game: guess the computer's secret number")
        print("3. Currency Roulette: estimate the ILS value of a random USD amount")
        print()
        game_input = input("Your choise: ")
        print()
        try:
            game_choice = int(game_input)
            if game_choice >= 1 and game_choice <=3:
                return game_choice
            else:
                print("Not exists!!!")
        except ValueError:
            print()