from abc import ABC, abstractmethod
from hero_game import Armor_module
from hero_game import Weapons_module
class Unit_class(ABC):
    # Основні характеристики
    name = ""
    health = 100
    attack = 20
    defence = 5
    status = True
    health_in_arena = 0

    #Блок броні
    helmet = Armor_module.Helmet()
    bodyarmor = Armor_module.Bodyarmor()
    boots = Armor_module.Boots()
    shield = Armor_module.Shield()

    #Блок сброї
    weapon = Weapons_module.Weapon()

    # Блок спеціальних можливостей
    ability = ""
    ability_value = 0
    ability_cooldown = 3

    #Блок ефектів
    stuned = False

    def unit_info_shop(self):
        return f"{self.name}, armor - , weapon - , ability - "

    def unit_info(self):
        return f"{self.name}, Health - {self.health}, Attack - {self.attack}, Defence - {self.defence}, Ability cooldown - {self.ability_cooldown}"

    def hit_power_for_fight(self):
        power = self.attack
        return power

    def defence_power_for_fight(self):
        power = self.defence + self.helmet.value + self.bodyarmor.value + self.boots.value + self.shield.value
        return power