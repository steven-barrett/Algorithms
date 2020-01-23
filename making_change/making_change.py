#!/usr/bin/python

import sys

denominations = [0, 1, 2, 5, 10, 25, 50]

def making_change(amount, denominations):
    cache = [0] * (amount + 1)
    cache[0] = 1
    
    for coin in denominations:
        for higher_amount in range(coin, amount+1):
            cache[higher_amount] += cache[higher_amount-coin]

    return cache[amount]

if __name__ == "__main__":
  # Test our your implementation from the command line
  # with `python making_change.py [amount]` with different amounts
  if 5 > 1:
    denominations = [1, 5, 10, 25, 50]
    amount = 300
    print("There are {ways} ways to make {amount} cents.".format(ways=making_change(amount, denominations), amount=amount))
  else:
    print("Usage: making_change.py [amount]")
