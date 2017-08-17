"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""


def main():
    # get score in percentage and show it as a grade
    score = float(input("Enter score: "))
    print(determine_status(score))


def determine_status(score):
    # find out the grade using the score
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


main()
