#from replit import clear
import os
#HINT: You can call clear() to clear the output in the console.
from art import logo
os.system('clear')
print(logo)

The_bid = {}

#new = input('Is there another bid: \n')

def highest_bid(bid_val):
    # "bid_val" = {"Alejo": 123, "Tom": 345} Key = Alejo and Tom, Value = 123 and 345
    top_bid = 0
    ganador = ""
    for bidder in bid_val:
        bid_am = bid_val[bidder] # We pass the 'Value' of the Dictionary: 'bid'
        if bid_am > top_bid:
            top_bid = bid_am
            ganador = bidder # We assign the 'Key' to 'ganador'.
    print(f"The winner is {ganador} with a bid of ${top_bid} \n")


last_bid = False
while not last_bid:
    name = input("What is your name: \n")
    bid = int(input("Enter your bid price: $\n"))
    #name_bid['name'] = name  # 
    The_bid[name] = bid    # Key = 'name' and Value = 'bid' for our Dictionary
    conti = input("Any more bidders? 'y' or 'n' ")
    if conti == 'n':
        last_bid = True
        highest_bid(The_bid) # Passing all the 'bids' to funxion 'highest_bid'
    elif conti == 'y':
        os.system('clear')

        #print('End of bids')


print(The_bid)