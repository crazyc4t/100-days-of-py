import os
import art

print(art.logo)
print("Welcome to the secret auction")

bets = {}

def dec():
    dec = input("are they any other bidders?(y/n) ")
    if dec == "y":
        betting()
    else:
        highest_bidder()

def betting():
    name = input("What is your name? ")
    bet = int(input("How much are you betting? $"))
    bets[name] = bet
    os.system("clear")
    dec()

def highest_bidder():
    highest_bid = 0
    for bidder in bets:
        current_bet = bets[bidder]
        if current_bet > highest_bid:
          highest_bid = current_bet 
          winner = bidder
    print(f"The winner is {winner} with ${highest_bid}")

betting()

