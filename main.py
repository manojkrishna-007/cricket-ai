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
    
    print()
    print("TOSS")
    oe = input("Odd or Even: ").lower()
    h = get_number("Enter todd number: ")
    ai = random.randint(1, 6)
    t = h+ai
    if t%2 == 0:
        result = "even"
    else:
        result = "odd"
        
    if oe == result:
        toss_winner = "user"
        print("You won the toss!")

        bat_or_bowl = input("Choose Bat or Bowl: ").lower()

    else:
        toss_winner = "ai"
        print("AI won the toss!")

        bat_or_bowl = random.choice(["bat", "bowl"])
        print("AI chooses to", bat_or_bowl)
    

main()