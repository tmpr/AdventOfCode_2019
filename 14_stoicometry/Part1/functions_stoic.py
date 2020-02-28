from account import Account

def compute_ore_cost(input_recipes: str) -> int:
    """
    Given some input recipe, computes the amount of ORE
    needed to produce 1 FUEL.
    """
    my_account = Account(input_recipes)
    my_account.produce_recipe(product_name="FUEL", how_often=1)

    # While there is any debt besides ORE-debt, keep on computing.
    while any([my_account.debt[material] > 0 
               for material in my_account.debt.keys() 
               if material != "ORE"]):

        debt_copy = my_account.debt.copy()
        for debt_name in debt_copy.keys():
            my_account.produce_recipe(debt_name, debt_copy[debt_name])

    return my_account.debt["ORE"]