class Recipe:
    """
    Model of a recipe.
    
    - Attributes:
    `account` - Parent account object\n
    `product_name` - Name of the material produced\n
    `product_amount` - Amount of product the recipe produces\n
    `costs` -Dictionary of cost_name : cost_amount\n
    """
    def __init__(self, cost: list, product_: str, account_object):
        self.account = account_object
        self.product_name = product_.split()[1]
        self.product_amount = int(product_.split()[0])
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
        """Produces a cost."""
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
        return f"{self.costs} => {self.product_amount} * {self.product_name}"