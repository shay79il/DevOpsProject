'''
Utils.py
A general purpose python file. 
This file will contain general information 
and operations we need for our game.
'''
import os


# A number representing a bad return code for a function
BAD_RETURN_CODE = 0xffff
SCORES_FILE_NAME = "Text_files/Scores.txt"

def screen_cleaner():
  '''
  A function to clear the screen 
  (useful when playing memory game or 
  before a new game starts)
  '''
  os.system('clear')
  

def is_correct_input(file_name, range_input):
  while True:
    with open(file_name, "r") as my_file:
      for line in my_file.readlines():
        print(line,end='')
    user_input = input("Answer: ")
    if not user_input.isdigit() or \
        int(user_input) not in range(1, range_input + 1):
      screen_cleaner()
      print("Wrong input\n")
      continue
    else:
      return int(user_input)


def is_digit(output):
  while True:
    print(output)
    user_input = input("Answer: ")
    if not user_input.isdigit():
      print("Wrong input\n")
      continue
    else:
      return int(user_input)      
