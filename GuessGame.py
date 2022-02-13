import random
import Utils


def generate_number(difficulty):
    """
    Will generate number between 1 to difficulty
    and save it to secret_number.
    """
    return random.randint(1, difficulty + 1)


def get_guess_from_user(difficulty):
    """
    Will prompt the user for a number between 1 to
    difficulty and return the number.
    """
    with open("Text_files/guess_game.txt", "w") as file:
        file.write(f"Enter a number between 1 to {difficulty}\n")

    return Utils.is_correct_input("Text_files/guess_game.txt", difficulty)


def compare_results(secret_number, user_guess):
    """
    Will compare the the secret generated number to
    the one prompted by the get_guess_from_user.
    """
    return secret_number == user_guess


def play(difficulty):
    """
    Will call the functions above and play the game.
    Will return True / False if the user lost or won.
    """
    secret_number = generate_number(difficulty)
    user_guess = get_guess_from_user(difficulty)
    return compare_results(secret_number, user_guess)
