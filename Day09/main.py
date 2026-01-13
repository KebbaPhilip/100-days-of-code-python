# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary

import  art
def find_highest_bidder(bid_catalog):
    highest_bid = 0
    winner = ""
    for bidder in bid_catalog:
        bid_amount = bid_catalog[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
            print(f"The winner is {winner} with a bid of ${highest_bid}")

bid_record = {}
print(art.logo)
while True:
    name = input("What is your name?: ").title()
    price = int(input("What is your bid?: $"))
    another_bidder = input("Are there any other bidders? Type 'yes' or 'no': ")
    bid_record[name] = price

    if another_bidder.lower() == "no":
        find_highest_bidder(bid_record)
        break
    elif another_bidder.lower() == "yes":
        print("\n" * 20)
    else:
        print("Invalid input. Please type 'yes' or 'no'.")
        break





