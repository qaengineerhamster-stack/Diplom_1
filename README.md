# Задание 1: Юнит-тесты

## Автотесты для проверки программы, которая помогает заказать бургер в Stellar Burgers

### Реализованные сценарии

Написаны юнит-тесты для класса `Burger`, покрывающие его основные методы:

- `set_buns`
- `add_ingredient`
- `remove_ingredient`
- `move_ingredient`
- `get_price`
- `get_receipt`

В тестах используются:
- `pytest`
- `mock`
- параметризация
- фикстура

Покрытие модуля `praktikum/burger.py` — **100%**.

### Структура проекта

- `praktikum` — пакет с кодом программы
- `tests` — пакет с юнит-тестами
- `tests/conftest.py` — фикстура для создания объекта `Burger`
- `tests/test_burger.py` — тесты для класса `Burger`

### Запуск автотестов

#### Установка зависимостей

```bash
pip install -r requirements.txt