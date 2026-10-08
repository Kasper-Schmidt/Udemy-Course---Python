bids = {}
bidding_finished = False

def highest_bidder(p_bids):
    highest_bid = 0
    bidder_name = ""
    for key, value in p_bids.items():
        if value > highest_bid:
            highest_bid = value
            bidder_name = key
    print(f"The winner is {bidder_name}, who bid ${highest_bid}")


while not bidding_finished:
    name = input("What is your name?: ")
    bid_amount = float(input("What is your bid amount? $"))
    bids[name] = bid_amount

    more_bidders = input("Any more bidders? (Y/N):  ").upper()

    if more_bidders == "N":
        bidding_finished = True
        highest_bidder(bids)
  

