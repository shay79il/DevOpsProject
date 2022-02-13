from Live import load_game, welcome
from Utils import screen_cleaner

while True:
    screen_cleaner()
    (msg, name) = welcome()
    print(msg)
    load_game(name)
    answer = input("Another Game? (y/n)")
    if answer == "n":
        break

 