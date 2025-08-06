import os
from secret_auction_art import logo


def find_highest_bidder(bids_dictionary):
    winner = ""
    highest_bid = 0
    for bidder in bids_dictionary:
        bid_amount = bids_dictionary[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}.")
    return highest_bid


print(logo)
print("Welcome to the secret auction program.")
other_bidders = True
continue_bidding = True
bids = {}
while other_bidders:
    name = input("What is your name?:")
    bid = int(input("What is your bid?: $"))
    bids[name] = bid
    while continue_bidding:
        bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
        if bidders == "no":
            other_bidders = False
            find_highest_bidder(bids)
            break
        elif bidders == "yes":
            os.system("cls")
            break
        else:
            print("Invalid input. Please type 'yes' or 'no'.")
