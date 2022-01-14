import Utils
import Score
import MemoryGame 
import GuessGame 
import CurrencyRouletteGame 


def welcome(name=None):
  '''
  This function has a person name as an input 
  and returns a string in the following layout:
  Hello <name> and welcome to the World of Games (WoG).
  Here you can find many cool games to play.
  '''
  while name is None or not name.isalnum():
    name = input("\nHello, what is your name? ").casefold()

  Score.add_score(name, 0)
  return (f"Hello {name} and welcome to the World of Games (WoG).\nHere you can find many cool games to play.\n", name)

def load_game(name):
  '''
  - The function gets an input from the user about 
    the game he chose. 
  - After receiving the game number from the user, 
    the function will get the level of difficulty 
    and also save to a variable. 
  - The function will check the input of the chosen game 
    (the input suppose to be a number between 1 to 3), 
    also will check the input of level of difficulty 
    (input should be a number between 1 to 5).
  '''
  CHOOSE_GAME = "Text_files/choose_game.txt"
  CHOOSE_DIFFICULTY = "Text_files/choose_difficulty.txt"
  game = Utils.is_correct_input(CHOOSE_GAME, 3)
  difficulty = Utils.is_correct_input(CHOOSE_DIFFICULTY, 5)
  if game == 1:
    is_win = MemoryGame.play(difficulty)
  elif game == 2:
    is_win = GuessGame.play(difficulty)
  else:
    is_win = CurrencyRouletteGame.play(difficulty)    
  if is_win:
    Score.add_score(name, difficulty)
    print("You are the MAN!")
  else:
    print("Try Again :)")
