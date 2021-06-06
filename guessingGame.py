import random
n = random.randint(1,9)

chances = 5
print("\n\n\n\n====== GUESS THE NUMBER ======")

while(chances > 0):
    guess = int(input("Enter your guess: "))
    if (guess == n):
        num = str(n)
        print("\n====================\nYou guessed the number :D\nIt was "+num+"\n====================")
        exit()
    elif (guess != n):
        chances = chances - 1
        chances_str = str(chances)
        if(guess > n):
            print("\nYour guess was too high\n"+chances_str+" guesses left\n")
        if(guess < n):
            print("\nYour guess was too low\n"+chances_str+" guesses left\n")

e = str(n)
print("====================\nYou couldn't guess the number :O \n"+"It was "+e+"\n====================")