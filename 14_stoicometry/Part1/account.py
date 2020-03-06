"""File containing the Account class."""
from math import ceil
from collections import defaultdict

from recipe import Recipe

class StoiciometryAccount:
    """
    Account to manage inventory and debt, 
    also has a dictionary of recipes.
    """
    def __init__(self, recipes: str):
        self.current_ore_count = 0
        self.debt = defaultdict(int)
        self.inventory = defaultdict(int)
        self.recipes = self.parse_recipes(recipes)

    def parse_recipes(self, recipes: str):
        """
        Returns a dictionary, where the keys are
        the product names and the keys are the actual
        Recipe objects.
        """
        recipe_dictionary = dict()
        raw_recipes = [raw_recipe.split("=>") for raw_recipe 
                                  in recipes.splitlines()]

        for raw_recipe in raw_recipes:
            raw_recipe[0] = raw_recipe[0].split(", ")
            raw_recipe[0] = [part.strip() for part in raw_recipe[0]]
            current_recipe = Recipe(cost=raw_recipe[0], 
                                product_=raw_recipe[1], account_object=self)
            recipe_dictionary[current_recipe.product_name] = current_recipe
        
        return recipe_dictionary

    def produce_recipe(self, product_name: str, how_often: int):
        """Produces Recipe specified amount of times."""
        # No recipe can produce ORE
        recipe = self.recipes[product_name]
        recipe.produce(iterations=ceil(how_often / recipe.product_amount))
        self.balance_debt_and_inventory()

    def balance_debt_and_inventory(self):
        for debt in self.debt:
            current_debt = self.debt[debt]
            self.debt[debt] -= self.inventory[debt]
            self.inventory[debt] -= current_debt

            # Cannot have negative debt or inventory
            if self.debt[debt] < 1:
                self.debt[debt] = 0
            if self.inventory[debt] < 1:
                self.inventory[debt] = 0
    
    def compute_ore_cost(self):
        """
        Given some input recipe, computes the amount of ORE
        needed to produce 1 FUEL.
        """
        
        self.produce_recipe(product_name="FUEL", how_often=1)
        # While there is any debt besides ORE-debt, keep on computing.
        while any([self.debt[material] > 0 
                for material in self.debt.keys() 
                if material != "ORE"]):

            debt_copy = self.debt.copy()
            for debt_name in debt_copy.keys():
                if debt_name != "ORE":
                    self.produce_recipe(debt_name, debt_copy[debt_name])

        return self.debt["ORE"]