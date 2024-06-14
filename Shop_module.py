import sqlite3
import time

import Team_module
import UNIT_CLASSES
import Armor_module
import Weapons_module


class Shop():
    def __init__(self, init_player_team=None, init_gold=0):
        self.player_team = init_player_team
        self.gold = init_gold

        self.player_team = Team_module.Team_class()
        self.player_team.create_start_team_for_player("ANUNAKI")
        self.gold = 1000

    def unit_shop(self):
        db = sqlite3.connect("Db_shop.db")
        cursor = db.cursor()

        cursor.execute("SELECT unit_name, unit_price FROM units")
        data = cursor.fetchall()

        print(f'''
        ----------------
            BUY UNITS
        ----------------
        Gold = {self.gold}''')

        for x in range(len(data)):
            print(f"        {x}. {data[x][0]} - {data[x][1]} gold")
        print(f"        {len(data)}. Show your team with all unit's items to analize.")
        print(f"        {len(data) + 1}. Return to previous stage.")

        while True:
            answer = input("Input the number here ---> ")

            try:
                answer = int(answer)
            except:
                continue

            if answer > len(data) + 1 or answer < 0:
                continue

            if answer == len(data) + 1:
                self.item_categories()
                break
            if answer == len(data):
                self.player_team.team_info_shop()
                continue
            else:
                chose = data[answer][0]
                self.gold = self.gold - \
                            cursor.execute(f"SELECT unit_price FROM units WHERE unit_name = '{chose}'").fetchone()[0]

                libruary = [
                    UNIT_CLASSES.Knight_class(),
                    UNIT_CLASSES.Archer_class(),
                    UNIT_CLASSES.Wizard_class(),
                    UNIT_CLASSES.Witch_class(),
                    UNIT_CLASSES.Healer_class(),
                    UNIT_CLASSES.Barbarian_class()]

                for unit in libruary:
                    if unit.name == chose:
                        self.player_team.alive_team.append(unit)
                        print(f"        You have bought {unit.name}")
                        self.item_categories()
                break

        db.close()

    def armor_shop(self):
        db = sqlite3.connect("Db_shop.db")
        cursor = db.cursor()

        cursor.execute("SELECT armor_name, value, price, armor_type_id FROM armor")
        data = cursor.fetchall()

        print(f'''
    ----------------
       BUY ARMOR
    ----------------
    Gold = {self.gold}''')

        for x in range(len(data)):
            print(f"        {x}. {data[x][0]} ({data[x][1]}power) -  {data[x][2]} gold")
        print(f"        {len(data)}. Show your team with all unit's items to analize.")
        print(f"        {len(data) + 1}. Return to previous stage.")

        while True:
            answer = input("Input the number here ---> ")

            try:
                answer = int(answer)
            except:
                continue

            if answer > len(data) + 1 or answer < 0:
                continue

            if answer == len(data) + 1:
                self.item_categories()
                break
            if answer == len(data):
                self.player_team.team_info_shop()
                continue
            else:
                armor_name = data[answer][0]
                armor_value = data[answer][1]
                armor_price = data[answer][2]
                armor_type = data[answer][3]
                if self.gold < armor_price:
                    print("Sorry, you have not enough gold to buy this armor")
                    continue
                break

        print("\n   Which unit will get this armor?")
        self.player_team.team_info_shop()

        while True:
            answer = input("Input the number here ---> ")

            try:
                answer = int(answer)
            except:
                continue

            if answer > len(self.player_team.alive_team)-1 or answer < 0:
                continue

            unit = self.player_team.alive_team[answer]
            break

        cursor.execute(f"SELECT armor_type_name FROM armor_types WHERE armor_type_id = '{armor_type}' ")
        armor_type = cursor.fetchone()[0]

        if armor_type == "helmet":
            unit.helmet = Armor_module.Helmet(armor_name, armor_value)
        elif armor_type == "bodyarmor":
            unit.bodyarmor = Armor_module.Bodyarmor(armor_name, armor_value)
        elif armor_type == "boots":
            unit.boots = Armor_module.Boots(armor_name, armor_value)
        elif armor_type == "shield":
            unit.shield = Armor_module.Shield(armor_name, armor_value)

        self.gold = self.gold - armor_price
        print(f"\n You have bought {armor_name}({armor_value} power) for {unit.name} for {armor_price} gold")

        time.sleep(1)
        self.item_categories()
        db.close()

    def weapon_shop(self):
        db = sqlite3.connect("Db_shop.db")
        cursor = db.cursor()

        print(f'''
            ----------------
               BUY WEAPON
            ----------------
            Gold = {self.gold}''')

        print("\n   Which unit will get this weapon?")
        self.player_team.team_info_shop()

        while True:
            answer = input("Input the number here ---> ")

            try:
                answer = int(answer)
            except:
                continue

            if answer > len(self.player_team.alive_team) - 1 or answer < 0:
                continue

            unit = self.player_team.alive_team[answer]
            break

        cursor.execute(f"SELECT unit_id FROM units WHERE unit_name = '{unit.name.lower()}'")
        unit_id = cursor.fetchone()[0]

        cursor.execute(f"SELECT weapon_name, value, price FROM weapons WHERE usable_for_unit = '{unit_id}'")
        data = cursor.fetchall()

        print()
        for x in range(len(data)):
            print(f"        {x}. {data[x][0]} ({data[x][1]}power) -  {data[x][2]} gold")
        print(f"        {len(data)}. Show your team with all unit's items to analize.")
        print(f"        {len(data) + 1}. Return to previous stage.")

        while True:
            answer = input("Input the number here ---> ")

            try:
                answer = int(answer)
            except:
                continue

            if answer > len(data) + 1 or answer < 0:
                continue

            if answer == len(data) + 1:
                self.item_categories()
                break
            if answer == len(data):
                self.player_team.team_info_shop()
                continue

            weapon_name = data[answer][0]
            weapon_value = data[answer][1]
            weapon_price = data[answer][2]

            if self.gold < weapon_price:
                print("Sorry, you have not enough gold to buy this armor")
                continue

            break

        unit.weapon = Weapons_module.Weapon(weapon_name, weapon_value)
        print(f"\n You have bought {weapon_name}({weapon_value} power) for {unit.name} for {weapon_price} gold")
        self.gold -= weapon_price

        time.sleep(1)
        self.item_categories()
        db.close()

    def ability_shop(self):
        print(f'''
        ----------------
           BUY ABILITY
        ----------------
        Gold = {self.gold}
           
        Which unit will get this ability?''')
        self.player_team.team_info_shop()

        while True:
            answer = input("Input the number here ---> ")

            try:
                answer = int(answer)
            except:
                continue

            if answer > len(data) + 1 or answer < 0:
                continue
            unit = self.player_team.alive_team[answer]
            break
        db = sqlite3.connect()
        cursor = db.cursor()
        cursor.execute((f"SELECT unit_id FROM units WHERE unit_name = '{unit.name.lower()}'"))
        unit_id = cursor.fetchall()[0]

        cursor.execute((f"SELECT weapon_name, value, price FROM abilities  WHERE usable_for_unit = '{unit_id}'"))
        data = cursor.fetchall()

        print()
        for x in range(len(data)):
            print(f"        {x}. {data[x][0]} ({data[x][1]}power) -  {data[x][2]} gold")
        print(f"        {len(data)}. Show your team with all unit's items to analize.")
        print(f"        {len(data) + 1}. Return to previous stage.")

        while True:
            answer = input("Input the number here ---> ")

            try:
                answer = int(answer)
            except:
                continue

            if answer > len(data) + 1 or answer < 0:
                continue

            if answer == len(data) + 1:
                self.item_categories()
                break
            if answer == len(data):
                self.player_team.team_info_shop()
                continue

            ability_name = data[answer][0]
            ability_value = data[answer][1]
            ability_price = data[answer][2]

            if self.gold < ability_price:
                print("Sorry, you have not enough gold to buy this armor")
                continue

            break



        unit.ability = ability_name
        unit.ability_value = ability_value
        print(f"\n You have bought {ability_name}({ability_value} power) for {unit.name} for {ability_price} gold")
        self.gold -= ability_price

        time.sleep(1)
        self.item_categories()


    def item_categories(self):
        print(f'''
    ----------------
    ITEM CATEGORIES
    ----------------
    Gold = {self.gold}

        0. Buy units.
        1. Buy armor.
        2. Buy weapon.
        3. Buy ability.
        4. Show your team with all unit's items to analize.
        5. Return to previous stage.''')

        while True:
            answer = input("Input the number here ---> ")
            if answer not in ["0", "1", "2", "3", "4", "5"]:
                continue

            # if answer in ["1","2","3"] and len(self.player_team.alive_team) < 5:
            #         print(" Get full team (5 units) first.")
            #         continue0


            if answer == "0":
                self.unit_shop()
            elif answer == "1":
                self.armor_shop()
            elif answer == "2":
                self.weapon_shop()
            elif answer == "3":
                self.ability_shop()
            elif answer == "4":
                self.player_team.team_info_shop()
                continue
            elif answer == "5":
                self.main()
            break

    def main(self):
        print(f'''
    ------------------------------------------
            WELCOME TO THE GAME SHOP
    ------------------------------------------
    Gold = {self.gold}''')

        print('''
    Please, choose, what would you like to do in the shop:
        0. See all item categories to buy.
        1. See your team with all unit's items to analise.
        2. Exit from the shop.''')

        while True:
            answer = input("Input the number here ---> ")
            if answer not in ["0", "1", "2"]:
                continue
            elif answer == "0":
                self.item_categories()
            elif answer == "1":
                self.player_team.team_info_shop()
                continue
            elif answer == "2":
                print("\nSee you next time, bye-bye!")
            break



