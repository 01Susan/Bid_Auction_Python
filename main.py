# blind auction
import json
import os

loop_continue = True
bids = {}

def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with the bid of ${highest_bid}")


while loop_continue:
    Name = input("Enter your Name : ")
    Bid_Price = int(input("Enter the Bid_Price: $"))
    bids[Name] = Bid_Price
    want_to_continue = input("Is there any other users who want to bid\n then type 'Yes' else 'No'").lower()
    if want_to_continue == "no":
        loop_continue = False
        find_highest_bidder(bids)
    elif want_to_continue == "yes":
        os.system('cls')
    else:
        print("Enter Valid Info")

