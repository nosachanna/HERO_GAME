# абілка - завдає удару всім ворогам одночасно на 50% потужності

from .Unit_module import Unit_class


class Knight_class(Unit_class):
    # Основні характеристики
    name = "Knight"

    # Спеціальні таланти
    ability_value = 0.5
    ability = f"Hit all enemy units by {int(ability_value*100)}% of attack"



