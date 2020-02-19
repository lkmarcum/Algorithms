#!/usr/bin/python

import argparse


def find_max_profit(prices):
    current_low = prices[0]
    current_profit = 0
    for i in range(1, len(prices)):
        if prices[i] < prices[i - 1]:
            if prices[i - 1] - current_low > current_profit:
                current_profit = prices[i - 1] - current_low
            current_low = prices[i]

    if current_profit == 0:
        current_loss = prices[1] - prices[0]
        for i in range(2, len(prices)):
            if prices[i] - prices[i - 1] > current_loss:
                current_loss = prices[i] - prices[i - 1]
        return current_loss
    return current_profit


if __name__ == '__main__':
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(
        description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int,
                        nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(
        profit=find_max_profit(args.integers), prices=args.integers))
