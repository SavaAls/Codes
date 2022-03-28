import random
x = random.randint(0, 10)
user_number = int(input("Guess the number until it is = x: "))
if user_number == x:
    print("Good Boy")
while user_number != x:
    user_number = int(input("Guess the number until it is = x: "))
    if user_number == x:
        print("Good Boy")
        break