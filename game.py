"""A number-guessing game."""
import random
# Put your code here
print("Welcome to the Guessing game.")
name = input("What is your name? ")
number_generator = random.randint(1,100)
tries = 1

while True:
    user_guess = int(input("Guess a number between 1 - 100: "))
    if user_guess < number_generator:
        print("Your guess is too low. Try again.")
        tries += 1
    elif user_guess > number_generator:
        print("your guess is too higly, Try again.")    
        tries += 1
    else:
        print("You are rigth, the number is:", number_generator)
        break    