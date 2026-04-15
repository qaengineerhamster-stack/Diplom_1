from database import Database
from burger import Burger


def main():
    database = Database()

    burger = Burger()

    available_buns = database.available_buns()
    available_ingredients = database.available_ingredients()

    bun = available_buns[0]
    burger.set_buns(bun)

    burger.add_ingredient(available_ingredients[0])
    burger.add_ingredient(available_ingredients[1])

    print(burger.get_receipt())


if __name__ == "__main__":
    main()