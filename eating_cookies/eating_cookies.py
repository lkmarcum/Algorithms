#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive
# recursive solution


def eating_cookies(n, cache=None):
    # hard-coded starter list for n = 0, 1, 2
    permutations = [1, 1, 2]

    # original recursive method
    # not optimized for large values of n
    # if n <= 2:
    #     return permutations[n]
    # return eating_cookies(n - 1) + eating_cookies(n - 2) + eating_cookies(n - 3)

    # pull from starter list if n is too small
    if n <= 2:
        total_perms = permutations[n]

    # update starter list to represent calcs for n-1, n-2, n-3 for each n
    else:
        for i in range(3, n):
            permutations.append(
                permutations[0] + permutations[1] + permutations[2])
            # drop value for n-4 (not needed to calc)
            permutations.pop(0)
        # sum list to get result for n
        total_perms = sum(permutations)

    return total_perms


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_cookies = int(sys.argv[1])
        print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(
            ways=eating_cookies(num_cookies), n=num_cookies))
    else:
        print('Usage: eating_cookies.py [num_cookies]')
