import os
import random
from number_guessing_game_art import logo


def choose_difficult():
    while True:
        difficult = (
            input("Choose a difficulty. Type 'easy' or 'hard': ").strip().lower()
        )
        if difficult in ("easy", "hard"):
            break
        print("Invalid input, type 'easy' or 'hard'.")

    tries = 5 if difficult == "hard" else 10
    return tries


def game_logic(condition, tries_game, number):
    while not condition or tries_game == 0:
        print(f"You have {tries_game} attempts remaining to guess the number.")
        guess = int(input("Make guess:"))
        if guess != number:
            if guess > number:
                print("Too high.")
            else:
                print("Too low.")
            print("Guess again.")
            tries_game -= 1
        else:
            print(f"You got it! The answer was {number}")
            condition = True
            break
        if tries_game == 0:
            print("You've run out of guesses, you lose.")
            condition = True


def game_number_guessing(condition, number_to_guess):
    os.system("cls")
    print(logo)
    print("Welcome to Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    tries = choose_difficult()
    game_logic(condition, tries, number_to_guess)


is_game_over = False
number_to_guess = random.randint(1, 100)
game_number_guessing(is_game_over, number_to_guess)
