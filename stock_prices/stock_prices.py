#!/usr/bin/python

import argparse


def find_max_profit(prices):
    currentmax_profit = 0
    currentmin_index = 0
    # find index of lowest price
    for index, price in enumerate(prices):
        # Index initialized to 0
        if index > 0:
            # If the price is less than the price at index 0
            if price <= prices[currentmin_index]:
                # Update current_min_price_index
                currentmin_index = index
                # Resolves edge case of lowest number at the end of prices
                if index != len(prices)-1:
                    # Loop through everything after current_min_price_index and find new current_max_profit
                    for n in range(currentmin_index+1, len(prices)-1):
                        if prices[n]-prices[currentmin_index] > currentmax_profit:
                            currentmax_profit = prices[n] - \
                                prices[currentmin_index]
        else:
          # initialize current_max_profit based on the difference between first and second prices
          # Resolves negative profit issues relating to initializing current_max_profit at 0
            currentmax_profit = prices[1] - prices[0]
    return currentmax_profit

if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))
