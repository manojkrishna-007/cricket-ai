import random
from collections import Counter


def get_number(message):
    while True:
        try:
            n = int(input(message))
            if 1 <= n <= 6:
                return n
            print("Enter a number from 1 to 6.")
        except ValueError:
            print("Enter a valid number.")