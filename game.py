"""A number-guessing game."""
import random
# Put your code here
print("Welcome to the Guessing game.")
name = input("What is your name? ")
number = int(input("Guess a nunber between 1 - 100: "))
number_generator = random.randint(1,100)