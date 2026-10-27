from Live import welcome, load_game

name = input("Enter your name: ")
print()
print(welcome(name))
while True:
    keep_going = load_game(name)
    if not keep_going:
        break