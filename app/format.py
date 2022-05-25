import random

FORMAT_MENU = """
Spin the Wheel!
Press Enter to spin the wheel!
"""


def format_menu():

    random_number = random.randint(1, 5)
    answer = ""

    if random_number == 1:
        answer = "Match Play"

    elif random_number == 2:
        answer = "Scramble"

    elif random_number == 3:
        answer = "Stroke Play"

    elif random_number == 4:
        answer = "Bestball"

    elif random_number == 5:
        answer = "Alternate Shot"

    else:
        "Error, please try again"

    return answer
