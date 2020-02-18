"""File containing the Account class."""
from math import ceil

from recipe import Recipe

class Account:
    """
    Account to manage inventory and debt, 
    also has a dictionary of recipes.
    """
    def __init__(self, recipes: str):
        self.current_ore_count = 0
        self.debt = dict()
        self.inventory = dict()
        self.recipes = self.parse_recipes(recipes)

    def parse_recipes(self, input_recipe: str):
        """
        Generator function which has items in the form of
        e.g. [["2 AB", "3 BC", "4 CA"], "1 FUEL"]
        """
        recipe_dictionary = dict()
        individual_raw_recipes = input_recipe.splitlines()
        
        # * Single recipe looks like this: "2 AB, 3 BC, 4 CA => 1 FUEL"
        individual_raw_recipes = [raw_recipe.split("=>")
                              for raw_recipe in individual_raw_recipes]

        for raw_recipe in individual_raw_recipes:
            raw_recipe[0] = raw_recipe[0].split(", ")
            raw_recipe[0] = [part.strip() for part in raw_recipe[0]]
            # * By now, recipes are in a list and look like this:
            # * [["2 AB", "3 BC", "4 CA"], "1 FUEL"]
            current_recipe = Recipe(cost=raw_recipe[0], 
                                product_=raw_recipe[1], account_object=self)
            recipe_dictionary[current_recipe.product_name] = current_recipe
        
        return recipe_dictionary

    def produce_recipe(self, product_name, how_often):
        # No recipe can produce ORE
        if product_name != "ORE": 
            recipe = self.recipes[product_name]
            recipe.produce(iterations=ceil(how_often / recipe.product_amount))
            self.balance_debt_and_inventory()

    def balance_debt_and_inventory(self):
        for debt in self.debt:
            if debt in self.inventory.keys():
                current_debt = self.debt[debt]
                self.debt[debt] -= self.inventory[debt]
                self.inventory[debt] -= current_debt

                # Cannot have negative debt or inventory
                if self.debt[debt] < 1:
                    self.debt[debt] = 0
                if self.inventory[debt] < 1:
                    self.inventory[debt] = 0