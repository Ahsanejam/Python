from art import logo
# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary
print(logo)

def find_highest_bidder(bidding_record):
    find_highest_bid = 0
    winner = ""
    for key in bidding_record:
        if bidding_record[key] > find_highest_bid:
            find_highest_bid = bidding_record[key]
            winner = key
    print(f"The winner is {winner} with a bid of ${find_highest_bid}.")


    # for key in bidding_record:
    #     if find_highest_bid == bidding_record[key]:
    #         print(f"The winner is {key} with a bid of ${bidding_record[key]}")


Bid = {}
run_loop = True
while run_loop:

    name = input("What is your name?: ")
    price = int(input("What is your bid?: $"))
    Bid[name] = price
    stop = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    if stop == 'no':
        run_loop = False
        find_highest_bidder(Bid)
    elif stop == 'yes':
        print("\n" * 20)

# print(Bid)

# Find_highest_bid = 0
# for key in Bid:
#     if Bid[key] > Find_highest_bid:
#         Find_highest_bid = Bid[key]
# print(Find_highest_bid)
#
# for key in Bid:
#     if Find_highest_bid == Bid[key]:
#         print(f"The winner is {key} with a bid of ${Bid[key]}")
