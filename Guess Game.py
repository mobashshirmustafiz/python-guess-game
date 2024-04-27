import random

num = random.randint(1,10)
guess = int (input ("Guess a number between 1 and 10 :"))

while guess != num:
    if guess < num:
        print("Your number is smaller")
    elif guess > num:
        print("Your number is bigger. ")
    guess = int (input(" Guess the Number"))
