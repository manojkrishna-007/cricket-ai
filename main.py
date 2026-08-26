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
    
    #====================TOSS====================
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
        
    if toss_winner == "user":

        if bat_or_bowl == "bat":
            first_batter = "user"
        else:
            first_batter = "ai"

    else:

        if bat_or_bowl == "bat":
            first_batter = "ai"
        else:
            first_batter = "user"
            
            
    #====================AI DATASET====================
    user_batting = []
    user_bowling = []
    
    #====================FIRST INNINGS====================
    score1 = 0
    out1 = 0

    balls = overs * 6

    for ball in range(balls):
        print()
        print(f"Score: {score1}/{out1}  ||  Ball: {ball + 1}/{balls}")
        
        if out1 == wickets:
            break


        if first_batter == "user":
            user = get_number("Your batting number: ")
            ai = ai_choice(user_batting, False)
            print("AI bowls:", ai)
            user_batting.append(user)
        else:
            user = get_number("Your bowling number: ")
            ai = ai_choice(user_bowling, True)
            print("AI bats:", ai)
            user_bowling.append(user)
            
            
        if user == ai:
            print("OUT!")
            out1 += 1
        else:
            if first_batter == "user":
                score1 += user
                print("You scored", user)
            else:
                score1 += ai
                print("AI scored", ai)
                
        
        #====================SECOND INNINGS====================
        target = score1 + 1
        print("Target:", target)

        if first_batter == "user":
            second_batter = "ai"
        else:
            second_batter = "user"
            
        score2 = 0
        out2 = 0

        for ball in range(balls):
            print()
            print(f"Score: {score2}/{out2}  ||  Ball: {ball + 1}/{balls}")

            if out2 == wickets or score2 >= target:
                break


            if second_batter == "user":
                user = get_number("Your batting number: ")
                ai = ai_choice(user_batting, False)
                print("AI bowls:", ai)
                user_batting.append(user)
            else:
                user = get_number("Your bowling number: ")
                ai = ai_choice(user_bowling, True)
                print("AI bats:", ai)
                user_bowling.append(user)


            if user == ai:
                print("OUT!")
                out2 += 1
            else:
                if second_batter == "user":
                    score2 += user
                    print("You scored", user)
                else:
                    score2 += ai
                    print("AI scored", ai)
                    
        
        
        

main()