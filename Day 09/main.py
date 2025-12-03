import os
import art

print(art.logo)
print("Welcome to the secret auction program.")

bidders = {}

def add_bidder():
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))
    bidders[name] = bid
    
    more = input("Are there any other bidders? Type 'yes' or 'no': ").lower()
    if more == "yes":
        os.system('cls' if os.name == 'nt' else 'clear')
        add_bidder()
    else:
        highest_bid = 0
        winner = ""
        for bidder in bidders:
            if bidders[bidder] > highest_bid:
                highest_bid = bidders[bidder]
                winner = bidder
        print(f"The winner is {winner} with a bid of ${highest_bid}!")

add_bidder()
