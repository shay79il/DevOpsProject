"""
Score.py
A package that is in charge of managing the scores file.
The scores file at this point will consist of only a number. That number is the accumulation of the winnings of the user.

Amount of points for winning a game is as follows:
POINTS_OF_WINNING = (DIFFICULTY X 3) + 5
Each time the user is winning a game, the points he won will
be added to his current amount of point saved in a file.
"""
import json
from Utils import SCORES_FILE_NAME
from Utils import BAD_RETURN_CODE


def get_scores():
    try:
        with open(SCORES_FILE_NAME, "r") as json_file:
            data = json_file.read()

        db_list = json.loads(data)
        return db_list

    except FileNotFoundError as e:
        print(f"File NOT found! {e.args}")
        return BAD_RETURN_CODE


def get_users_scores_html():
    users_scores = get_scores()
    if users_scores == BAD_RETURN_CODE:
        users_html = f"\n<h1><div id=\"error\" style=\"color:red\">{BAD_RETURN_CODE}</div></h1>\n"
    else:
        users_html = "\n"
        for i, element in enumerate(users_scores):
            username, score = tuple(element.values())
            users_html += f"<h1>The score of {username} is <div id=\"score{i}\">{score}</div></h1>\n"

    return users_html


def add_score(name, difficulty):
    """
    The function’s input is a variable called difficulty.
    The function will try to read the current score in the scores file,
    if it fails it will create a new one and will use it to save the current score.
    """
    try:
        with open(SCORES_FILE_NAME, "r") as json_file:
            data = json_file.read()

        # reconstructing the data as a dictionary
        # Note: db is a list of dictionaries
        db_list = json.loads(data)

        # Find user
        user_found = False
        for item in db_list:
            if item["username"] == name:
                if difficulty != 0:
                    item.update({"score": item["score"] + difficulty * 3 + 5})
                user_found = True
                break

        if not user_found:
            db_list.append({"username": name, "score": 0})

    except FileNotFoundError as e:
        print(f"File NOT found! {e.args}")
        print(f"Creating DB file {SCORES_FILE_NAME} and add name")
        print(name)

        db_list = [{"username": name, "score": 0}]

    finally:
        with open(SCORES_FILE_NAME, "w") as json_file:
            json_file.write(json.dumps(db_list))
