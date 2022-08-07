"""A number-guessing game."""
import random
# Put your code here
print("Welcome to the Guessing game.")
name = input("What is your name? ")
number_generator = random.randint(1,100)
tries = 1
print("The correct number is:", number_generator)

while True:
    user_guess = input("Guess a number between 1 - 100: ")
    if not user_guess.isdecimal():        
        print("just positive numbers allow")
        tries += 1
        continue
    user_guess_int = int(user_guess)
    if user_guess_int < 0 or user_guess_int > 100:
        print("Your guess is out of range. Enter a number beetween 1 and 100.")
        tries += 1         
    elif user_guess_int < number_generator:
        print("Your guess is too low. Try again.")
        tries += 1
    elif user_guess_int > number_generator:
        print("your guess is too higly, Try again.")    
        tries += 1
    else:
        print("You are rigth, the number is:", number_generator)
        break    