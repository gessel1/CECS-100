print("How to play:")
print("I will pick a secret number")
print("you guees what the number is.")
print("If your guess is too high or too low, I will tell you")
print("See how many turns it take you to win!")

def game():
    import random
    answer=random.randint(1,10)
    guess= int(input("What is your guess?"))
    tries=0
    while tries < 5:
        if answer == guess:
            print("YAY you win.")
        elif answer > guess:
            print("your guess is too low, try again.")
            guess= int(input("What is your guess?"))
        elif answer < guess:
            print("your guess is too high, try again.")
            guess= int(input("What is your guess?"))
        tries +=1
game()
