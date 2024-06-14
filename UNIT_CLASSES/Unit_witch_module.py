# абілка - завдає удару всім ворогам одночасно на 50% потужності

from .Unit_module import Unit_class


class Witch_class(Unit_class):
    # Основні характеристики
    name = "Witch"

    # Спеціальні таланти
    ability_value = 10
    ability = f"Poison 1 enemy unit by {ability_value} for 2 next moves"



