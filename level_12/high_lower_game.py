import os
import random
from high_lower_game_art import logo, vs
from high_lower_game_data import data


def pick_different_option(exclude):
    choice = random.choice(data)
    while choice == exclude:
        choice = random.choice(data)
    return choice


def print_compare(label, info):
    print(
        f"Compare {label}: {info['name']}, a {info['description']}, from {info['country']}"
    )


def game_screen(condition, game_score, info_option_a, info_option_b):
    os.system("cls")
    if game_score == 0 and not condition:
        print(logo)
        print_compare("A", info_option_a)
        print(vs)
        print_compare("B", info_option_b)
    elif game_score > 0 and not condition:
        print(logo)
        print(f"You're right! Current score: {game_score}")
        print_compare("A", info_option_a)
        print(vs)
        print_compare("B", info_option_b)
    else:
        print(logo)
        print(f"Sorry, that's wrong. Final score: {game_score}")


def game():
    score = 0
    is_game_over = False
    option_a = random.choice(data)
    option_b = pick_different_option(option_a)
    while not is_game_over:
        game_screen(is_game_over, score, option_a, option_b)
        while True:
            user_answer = (
                input("Who has more followers? Type 'A' or 'B': ").strip().lower()
            )
            if user_answer in ("a", "b"):
                break
            print("Invalid input. Please type 'A' or 'B'.")
        option_a_count = option_a["follower_count"]
        option_b_count = option_b["follower_count"]
        winner_is_a = option_a_count >= option_b_count
        correct = (user_answer == "a" and winner_is_a) or (
            user_answer == "b" and not winner_is_a
        )
        if not correct:
            is_game_over = True
            game_screen(is_game_over, score, option_a, option_b)
            break
        score += 1
        option_a = option_a if winner_is_a else option_b
        option_b = random.choice(data)


if __name__ == "__main__":
    game()
