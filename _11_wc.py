from re import I
import time
from _01_akp import any_key_proceed


def welcome_note():
    print("=========================================")
    print("=========================================")
    print(">>> Welcome to the Number Guessing game")
    time.sleep(2)
    print("=========================================")
    print("================ RULES ==================")
    time.sleep(2)
    print("The rules are simple. Two players play against"
    " each other. Each takes turn and sets a number, which"
    " the other player tries to guess. Player taking fewer"
    " guesses wins.\n")
    time.sleep(2)
    print("It can also be played 1-player mode. In 1-player"
    " mode, the second player is the computer.")
    print("=========================================")
    time.sleep(2)
    any_key_proceed()