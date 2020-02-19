#!/usr/bin/python

import math


def recipe_batches(recipe, ingredients):
    smallest_ratios = []
    for key in recipe:
        if not key in ingredients:
            return 0
        else:
            smallest_ratios.append(ingredients[key] // recipe[key])
    print(smallest_ratios)
    return min(smallest_ratios)


if __name__ == '__main__':
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = {'milk': 100, 'flour': 4, 'sugar': 10, 'butter': 5}
    ingredients = {'milk': 1288, 'flour': 9, 'sugar': 95}
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
        batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
