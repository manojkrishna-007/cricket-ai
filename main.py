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


def ai_choice(history, batting):
    if len(history) < 3:
        return random.randint(1, 6)

    count = Counter(history)

    if batting:
        weights = []

        for n in range(1, 7):
            weights.append(max(1, 10 - count[n] * 2))

    else:
        weights = []

        for n in range(1, 7):
            weights.append(1 + count[n] * 2)

    return random.choices(range(1, 7), weights=weights)[0]


def main():
    wickets = int(input("Number of wickets: "))
    overs = int(input("Number of overs: "))
    

main()