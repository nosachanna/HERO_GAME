import Texts_module

class Fight_Class():

    def __init__(self, init_player_unit, init_comp_unit, init_fight_counter, init_player_team, init_comp_team):
        self.player_unit = init_player_unit
        self.comp_unit = init_comp_unit
        self.fight_counter = init_fight_counter
        self.player_team = init_player_team
        self.comp_team = init_comp_team



    def fight_board(self):
        if self.fight_counter % 2 != 0:
            attacker = self.player_unit
            defender = self.comp_unit
        else:
            attacker = self.comp_unit
            defender = self.player_unit
        print(Texts_module.fight_board(attacker, defender, self.fight_counter))




    def check_abilities(self):
        if self.fight_counter % 2 != 0:
            if self.player_unit.ability_cooldown == 0:
                print(f"{self.player_unit.name} is ready to use his Ability ({self.player_unit.ability})")
                answear = ""
                while answear[0].lower() not in ["y","n"]:
                    answear = input(f"Do you want to use {self.player_unit.name} ability? (Y/N) ---> ")

                if answear[0].lower() == "y":
                    self.player_unit.ability_cooldown  = 3
                    self.player_unit.use_ability(enemy = self.comp_unit,
                                                 self_team = self.player_team,
                                                 enemy_team = self.comp_team)
                else:
                    self.player_unit.ability_cooldown  = 0

            else:
                self.player_unit.ability_cooldown  -= 1
                self.attack(attacker = self.player_unit, defender = self.comp_unit)

        else:
            if self.comp_unit.ability_cooldown == 0:
                print(f"{self.comp_unit.name} is ready to use his Ability ({self.comp_unit.ability})")
                self.comp_unit.use_ability(enemy = self.player_unit,
                                           self_team = self.comp_team,
                                           enemy_team = self.player_team)
            else:
                self.comp_unit.ability_cooldown -= 1
                self.attack(attacker=self.comp_unit, defender=self.player_unit)



    def attack(self, attacker, defender):
        attacker_hit = attacker.hit_power_for_fight()
        attacker_defence = attacker.defence_power_for_fight()

        defender_hit = defender.hit_power_for_fight()
        defender_defence = defender.defence_power_for_fight()

        if attacker_hit > defender_defence:
            defender.health_in_arena = defender.health_in_arena - attacker_hit + defender_defence

        if defender_hit > attacker_defence:
            attacker.health_in_arena = attacker.health_in_arena - defender_hit + attacker_defence

        for unit in [attacker, defender]:
            if unit.health < 0:
                unit.health = 0
                unit.status = False

        self.result_board(attacker, defender)


    def result_board(self, attacker, defender):
        print(Texts_module.fight_result_board(attacker, defender))