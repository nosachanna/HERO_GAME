from .Unit_module import Unit_class


class Healer_class(Unit_class):
    # Основні характеристики
    name = "Healer"

    # Спеціальні таланти
    ability_value = 50
    ability = f"Heal all teammates by {ability_value}hp"

