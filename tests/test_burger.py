import pytest
from unittest.mock import Mock

from burger import Burger
from ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


@pytest.fixture
def burger():
    return Burger()


@pytest.fixture
def bun():
    bun = Mock()
    bun.get_name.return_value = "black bun"
    bun.get_price.return_value = 100
    return bun


@pytest.fixture
def sauce():
    sauce = Mock()
    sauce.get_type.return_value = INGREDIENT_TYPE_SAUCE
    sauce.get_name.return_value = "hot sauce"
    sauce.get_price.return_value = 50
    return sauce


@pytest.fixture
def filling():
    filling = Mock()
    filling.get_type.return_value = INGREDIENT_TYPE_FILLING
    filling.get_name.return_value = "cutlet"
    filling.get_price.return_value = 80
    return filling


class TestBurger:
    def test_set_buns_sets_bun(self, burger, bun):
        burger.set_buns(bun)

        assert burger.bun == bun

    def test_add_ingredient_adds_ingredient_to_list(self, burger, sauce):
        burger.add_ingredient(sauce)

        assert sauce in burger.ingredients
        assert len(burger.ingredients) == 1

    def test_remove_ingredient_removes_ingredient_from_list(self, burger, sauce, filling):
        burger.add_ingredient(sauce)
        burger.add_ingredient(filling)

        burger.remove_ingredient(0)

        assert sauce not in burger.ingredients
        assert burger.ingredients == [filling]

    def test_move_ingredient_moves_ingredient_in_list(self, burger, sauce, filling):
        burger.add_ingredient(sauce)
        burger.add_ingredient(filling)

        burger.move_ingredient(0, 1)

        assert burger.ingredients == [filling, sauce]

    def test_get_price_returns_correct_price(self, burger, bun, sauce, filling):
        burger.set_buns(bun)
        burger.add_ingredient(sauce)
        burger.add_ingredient(filling)

        price = burger.get_price()

        assert price == 330

    def test_get_receipt_returns_correct_receipt(self, burger, bun, sauce, filling):
        burger.set_buns(bun)
        burger.add_ingredient(sauce)
        burger.add_ingredient(filling)

        receipt = burger.get_receipt()

        expected_receipt = (
            "(==== black bun ====)\n"
            "= sauce hot sauce =\n"
            "= filling cutlet =\n"
            "(==== black bun ====)\n"
            "\n"
            "Price: 330"
        )

        assert receipt == expected_receipt