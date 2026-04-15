from bun import Bun
from ingredient import Ingredient


class Burger:

    def __init__(self):
        self.bun = None
        self.ingredients = []

    def set_buns(self, bun: Bun):
        self.bun = bun

    def add_ingredient(self, ingredient: Ingredient):
        self.ingredients.append(ingredient)

    def remove_ingredient(self, index: int):
        del self.ingredients[index]

    def move_ingredient(self, index: int, new_index: int):
        self.ingredients.insert(new_index, self.ingredients.pop(index))

    def get_price(self):
        price = self.bun.get_price() * 2

        for ingredient in self.ingredients:
            price += ingredient.get_price()

        return price

    def get_receipt(self):
        receipt = f'(==== {self.bun.get_name()} ====)\n'

        for ingredient in self.ingredients:
            receipt += f'= {ingredient.get_type().lower()} {ingredient.get_name()} =\n'

        receipt += f'(==== {self.bun.get_name()} ====)\n\n'
        receipt += f'Price: {self.get_price()}'

        return receipt