#!/usr/bin/python

import sys


def rock_paper_scissors(n):
    plays = ['rock', 'paper', 'scissors']
    permutations = []

    def recurse(current_n, perm_list):
        if current_n == 0:
            permutations.append(perm_list)
            return

        for i in range(0, len(plays)):
            recurse(current_n - 1, perm_list + [plays[i]])

    recurse(n, [])

    return permutations


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print('Usage: rps.py [num_plays]')
