# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary
import art
print(art.logo)
bid = {}
continue_bidding = True
while continue_bidding:
    name = input("What is your name?:   ")
    price = int(input("What is your bid?:$  "))
    bid[name] = price

    bidders = input("Are there any other bidders? Type 'yes or 'no'.")
    print("\n" * 20)
    if bidders == "no":
        continue_bidding = False
highest_bid = 0
winner = " "
for name in bid:
    bid_amount = bid[name]
    if bid_amount > highest_bid:
        highest_bid = bid_amount
        winner = name
print(f"The winner is {winner} with a bid of ${highest_bid} ")



