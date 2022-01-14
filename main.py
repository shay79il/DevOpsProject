from Live import load_game, welcome
from Utils import screen_cleaner

screen_cleaner()
(msg, name) = welcome()
print(msg)
load_game(name)
 