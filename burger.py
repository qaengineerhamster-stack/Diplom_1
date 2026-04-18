class Burger:

    def __init__(self):
        self.bun = None
        self.ingredients = []

    def set_buns(self, bun):
        self.bun = bun

    def add_ingredient(self, ingredient):
        self.ingredients.append(ingredient)

    def remove_ingredient(self, index):
        del self.ingredients[index]

    def move_ingredient(self, index, new_index):
        ingredient = self.ingredients.pop(index)
        self.ingredients.insert(new_index, ingredient)

    def get_price(self):
        price = 2 * self.bun.get_price()
        for ingredient in self.ingredients:
            price += ingredient.get_price()
        return price

    def get_receipt(self):
        receipt = f'(==== {self.bun.get_name()} ====)\n'
        for ingredient in self.ingredients:
            receipt += f'= {ingredient.get_type()} {ingredient.get_name()} =\n'
        receipt += f'(==== {self.bun.get_name()} ====)\n'
        receipt += f'\nPrice: {self.get_price()}'
        return receipt
class Burger:

    def __init__(self):
        self.bun = None
        self.ingredients = []

    def set_buns(self, bun):
        self.bun = bun

    def add_ingredient(self, ingredient):
        self.ingredients.append(ingredient)

    def remove_ingredient(self, i):
        del self.ingredients[i]

    def move_ingredient(self, index, new_index):
        self.ingredients.insert(new_index, self.ingredients.pop(index))

    def get_price(self):
        price = 2 * self.bun.get_price()
        for ingredient in self.ingredients:
            price += ingredient.get_price()
        return price

    def get_receipt(self):
        receipt = f"(==== {self.bun.get_name()} ====)\n"
        for ingredient in self.ingredients:
            receipt += f"= {ingredient.get_type().lower()} {ingredient.get_name()} =\n"
        receipt += f"(==== {self.bun.get_name()} ====)\n\n"
        receipt += f"Price: {self.get_price()}"
        return receipt