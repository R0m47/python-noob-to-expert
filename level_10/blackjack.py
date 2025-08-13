from blackjack_art import logo
from random import randint


def play_or_not():
    return input(
        "Do you want to play a game of Blackjack? Type 'y' or any other key to exit: "
    )


def blackjack():
    print(logo)
    five_elevens = False
    my_first_card = randint(1, 11)
    my_second_card = randint(1, 11)
    computer_first_card = randint(1, 11)
    computer_second_card = randint(1, 11)
    my_cards = [my_first_card, my_second_card]
    computer_cards = [computer_first_card, computer_second_card]
    print(f"Your cards:[{my_cards}]")
    print(f"Computer's first card:[{computer_first_card}]")
    if (
        my_first_card + my_second_card >= 21
        or computer_first_card + computer_second_card >= 21
    ):
        print(f"Your final hand:[{my_cards}]")
        print(f"Computer's final hand:[{computer_cards}]")
        if (
            my_first_card + my_second_card == 21
            or computer_first_card + computer_second_card > 21
        ):
            print("You Win")
        elif (
            my_first_card + my_second_card == 21
            and computer_first_card + computer_second_card == 21
        ):
            print("Draw")
        else:
            print("Computer Win")
    else:
        pass_or_not = input("Type 'y' to get another card, type 'n' to pass:")
        if pass_or_not == "y":
            while not five_elevens:
                my_third_card = randint(1, 11)
                if (
                    my_third_card == 11
                    and my_first_card == 11
                    and my_second_card == 11
                    and computer_first_card == 11
                    and computer_second_card == 11
                ):
                    my_third_card = randint(1, 11)
                else:
                    five_elevens = True
            my_cards.append(my_third_card)
        print(f"Your final hand:[{my_cards}]")
        print(f"Computer's final hand:[{computer_cards}]")
        if (
            my_first_card + my_second_card + my_third_card
            == computer_first_card + computer_second_card
        ):
            print("Draw")
        elif (
            my_first_card + my_second_card + my_third_card > 21
            and computer_first_card + computer_second_card == 21
            or computer_first_card + computer_second_card < 21
            or computer_first_card + computer_second_card
            < my_first_card + my_second_card + my_third_card
        ):
            print("You lose")
        else:
            print("You win")


start = play_or_not()
while start == "y":
    blackjack()
    start = play_or_not()
