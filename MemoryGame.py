import Utils
import random
from time import sleep


def generate_sequence(difficulty):
    """
    Will generate a list of random numbers between 1 to 101.
    The list length will be difficulty.
    """
    sequence = [random.randint(1, 101) for _ in range(0, difficulty)]
    print(f"\n{sequence}", end='\r')
    sleep(0.7)
    return sequence


def get_list_from_user(difficulty):
    """
    Will return a list of numbers prompted from the user.
    The list length will be in the size of difficulty.
    """
    with open("Text_files/memory_game.txt", "w") as file:
        file.write(f"Please enter {difficulty} numbers you remember\n")
    func = Utils.is_correct_input
    file_name = "Text_files/memory_game.txt"
    input_range = 101
    return [func(file_name, input_range) for _ in range(0, difficulty)]


def is_list_equal(game_list, user_list):
    """
    A function to compare two lists if they are equal.
    The function will return True / False.
    """
    game_list.sort()
    user_list.sort()
    return game_list == user_list


def play(difficulty):
    """
    Will call the functions above and play the game.
    Will return True / False if the user lost or won.
    """
    game_list = generate_sequence(difficulty)
    user_list = get_list_from_user(difficulty)
    return is_list_equal(game_list, user_list)
