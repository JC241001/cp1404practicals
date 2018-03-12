"""Take a score from user input and prints result/message"""


def main():

    score_value = get_users_score()
    print(result_of_score(score_value))


def get_users_score():
    """Obtain and return users score with validity checking"""
    valid_input = False
    while not valid_input:
        try:
            score_value = float(input("Enter a Score between 0 and 100: "))
            if score_value < 0 or score_value > 100:
                print("Invalid score")
                continue
            valid_input = True
        except ValueError:
            print("Invalid input")
    return score_value


def result_of_score(value):
    """Only accepts values between 0 and 100.
    Returns a String."""
    if value >= 90:
        result_string = "Excellent"
    elif value >= 50:
        result_string = "Passable"
    else:
        result_string = "Bad"

    return result_string


if __name__ == '__main__':
    main()
