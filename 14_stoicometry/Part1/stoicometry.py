"""
Solution to Day 14 of the Advent of Code 2019.
Title: 'Space Stoicometry'
URL: https://adventofcode.com/2019/day/14
Author: tmpr
Date: 16th of February
"""
import os
from math import ceil


class Account:
    """Account to manage inventory and debt."""

    def __init__(self, recipes):
        self.current_ore_count = 0
        self.debt = dict()
        self.inventory = dict()
        self.recipes = list(self.parse_recipes(recipes))

    def parse_recipes(self, input_recipe: str):
        """
        Generator function which has items in the form of
        e.g. [["2 AB", "3 BC", "4 CA"], "1 FUEL"]
        """
        individual_recipes = input_recipe.splitlines()
        # * Single recipe looks like this: "2 AB, 3 BC, 4 CA => 1 FUEL"
        individual_recipes = [recipe.split("=>")
                              for recipe in individual_recipes]
        for recipe in individual_recipes:
            recipe[0] = recipe[0].split(", ")
            recipe[0] = [part.strip() for part in recipe[0]]
            # * By now, recipes are in a list and look like this:
            # * [["2 AB", "3 BC", "4 CA"], "1 FUEL"]
            yield Recipe(cost=recipe[0], product_=recipe[1], account_object=self)

    def produce_recipe(self, product_name, how_often):
        for recipe in self.recipes:
            if recipe.product_name == product_name:
                recipe.produce(
                    iterations=ceil(
                        how_often /
                        recipe.product_amount))
                self.balance_debt_and_inventory()

    def balance_debt_and_inventory(self):
        for debt in self.debt:
            if debt in self.inventory.keys():
                current_debt = self.debt[debt]
                self.debt[debt] -= self.inventory[debt]
                self.inventory[debt] -= current_debt
                if self.debt[debt] < 1:
                    self.debt[debt] = 0
                if self.inventory[debt] < 1:
                    self.inventory[debt] = 0


class Recipe:

    def __init__(self, cost: list, product_: str, account_object: Account):
        self.account = account_object
        self.product_name = product_.split()[1]
        self.product_amount = int(product_.split()[0])
        self.product = {self.product_name: self.product_amount}
        self.costs = {
            summand.split()[1]: int(
                summand.split()[0]) for summand in cost}

    def produce(self, iterations):
        """Adds product to account inventory and adds needed materials to debt."""
        for _ in range(iterations):
            temporal_cost = self.costs.copy()
            for cost in temporal_cost.keys():
                self.process_single_cost(cost, temporal_cost)
            self.add_product_to_inventory()

    def process_single_cost(self, cost, temporal_cost):
        # Use leftovers first.
        if cost in self.account.inventory.keys():
            temporal_cost[cost] -= self.account.inventory[cost]
            self.account.inventory[cost] -= self.costs[cost]
            if self.account.inventory[cost] < 1:
                self.account.inventory[cost] = 0
            if temporal_cost[cost] < 0:
                temporal_cost[cost] = 0
        # If there is still some cost, add to debt
        if cost in self.account.debt.keys():
            self.account.debt[cost] += temporal_cost[cost]
        else:
            self.account.debt[cost] = temporal_cost[cost]

    def add_product_to_inventory(self):
        if self.product_name in self.account.inventory.keys():
            self.account.inventory[self.product_name] += self.product_amount
        else:
            self.account.inventory[self.product_name] = self.product_amount

    def __repr__(self):
        return f"{self.costs} => {self.product}"


def compute_ore_cost(input_recipe: str) -> int:
    """
    Given some input recipe, computes the amount of ORE
    needed to produce 1 FUEL.
    """
    my_account = Account(input_recipe)
    my_account.produce_recipe(product_name="FUEL", how_often=1)

    # While there is any debt besides ORE-debt, keep on computing.
    while any([my_account.debt[thing] >
               0 for thing in my_account.debt.keys() if thing != "ORE"]):
        debt_copy = my_account.debt.copy()
        for debt_name in debt_copy.keys():
            my_account.produce_recipe(debt_name, debt_copy[debt_name])

    return my_account.debt["ORE"]


if __name__ == "__main__":
    with open(os.path.join("example_files", "my_input.txt"), "r") as f:
        my_input = f.read()
    print(compute_ore_cost(my_input))
