import pytest
from unittest.mock import Mock


# Проверяет только установку булки в бургер через метод set_buns.
def test_set_bun(burger):
    bun = Mock()
    bun.get_name.return_value = "black bun"
    bun.get_price.return_value = 100

    burger.set_buns(bun)

    assert burger.bun == bun


# Проверяет только добавление одного ингредиента через метод add_ingredient.
def test_add_ingredient(burger):
    ingredient = Mock()
    ingredient.get_name.return_value = "cutlet"
    ingredient.get_price.return_value = 50
    ingredient.get_type.return_value = "filling"

    burger.add_ingredient(ingredient)

    assert burger.ingredients == [ingredient]


# Проверяет только удаление ингредиента по индексу через метод remove_ingredient.
def test_remove_ingredient(burger):
    ingredient_1 = Mock(name="ingredient_1")
    ingredient_2 = Mock(name="ingredient_2")

    burger.add_ingredient(ingredient_1)
    burger.add_ingredient(ingredient_2)
    burger.remove_ingredient(0)

    assert burger.ingredients == [ingredient_2]


# Проверяет только перемещение ингредиента внутри списка через метод move_ingredient.
@pytest.mark.parametrize(
    "start_index,new_index,expected_order",
    [
        (0, 2, ["ingredient_2", "ingredient_3", "ingredient_1"]),
        (2, 0, ["ingredient_3", "ingredient_1", "ingredient_2"]),
    ],
)
def test_move_ingredient(burger, start_index, new_index, expected_order):
    ingredient_1 = Mock(name="ingredient_1")
    ingredient_2 = Mock(name="ingredient_2")
    ingredient_3 = Mock(name="ingredient_3")

    burger.add_ingredient(ingredient_1)
    burger.add_ingredient(ingredient_2)
    burger.add_ingredient(ingredient_3)

    burger.move_ingredient(start_index, new_index)

    actual_order = [item._extract_mock_name() for item in burger.ingredients]

    assert actual_order == expected_order


# Проверяет только расчет цены через метод get_price.
@pytest.mark.parametrize(
    "bun_price, ingredients_prices, expected_price",
    [
        (100, [50], 250),
        (200, [100, 300], 800),
    ],
)
def test_get_price(burger, bun_price, ingredients_prices, expected_price):
    bun = Mock()
    bun.get_price.return_value = bun_price

    burger.set_buns(bun)

    for price in ingredients_prices:
        ingredient = Mock()
        ingredient.get_price.return_value = price
        burger.add_ingredient(ingredient)

    assert burger.get_price() == expected_price


# Проверяет только формирование чека через метод get_receipt.
def test_get_receipt(burger):
    bun = Mock()
    bun.get_name.return_value = "black bun"
    bun.get_price.return_value = 100

    ingredient = Mock()
    ingredient.get_name.return_value = "cutlet"
    ingredient.get_price.return_value = 50
    ingredient.get_type.return_value = "filling"

    burger.set_buns(bun)
    burger.add_ingredient(ingredient)

    receipt = burger.get_receipt()

    expected_receipt = (
        "(==== black bun ====)\n"
        "= filling cutlet =\n"
        "(==== black bun ====)\n\n"
        "Price: 250"
    )

    assert receipt == expected_receipt