
import UNIT_CLASSES
import Texts_module
import Arena_module
from Team_module import Team_class
import Shop_module
import sqlite3

class Game_class():
    player_name = ""
    player_gold = 1000
    win_status = None
    all_arenas = 5
    arena_counter = 0

    def game_running(self):
        if self.arena_counter < 5:
            return True
        if len(self.player_team.alive_team) < 5:
            unit_needed = 5 - len(self.player_team.alive_team)

            db =sqlite3.connect("Db_shop.db")
            cursor =db.cursor()
            cursor.execute("SELECT unit_price from units")
            data = cursor.fetchall()

            lst = []
            for price in data:
                lst.append(price[0])
            min_price = min(lst)

            min_budget = unit_needed * min_price
            if self.player_gold > min_budget:
                return True

        return True



    def play(self):
        # Вітальний екран
        print(Texts_module.game_welcome_board())

        # Знайомство
        self.player_name = input(Texts_module.get_player_name())
        print(Texts_module.welcome_young_hero(self.player_name, self.player_gold, self.all_arenas))

        # Створення початкової команди
        self.player_team = Team_class()
        self.player_team.create_start_team_for_player(self.player_name)

        print(Texts_module.wow_you_have_a_squad(self.player_team.alive_team))

        # Основний цикл гри
        while self.game_running():
            # Ознайомлення з магазином
            shop = Shop_module.Shop(self.player_team, self.player_gold)
            shop.main()

            # створення арени, поміщення команди гравця в арену
            arena = Arena_module.Arena_class(self.player_team, self.arena_counter)
            arena.create_comp_team()
            arena.display_arena_board()
            arena.fight()

            # аналіз результатів
            arena_results = arena.arena_results()
            self.player_team.alive_team = arena_results[0]
            self.player_team.dead_team.append(arena_results[1])

            # rewards за закінчення арени
            if len(self.player_team.alive_team) > 0 :
                arena_reward = 1000
                self.player_gold += arena_reward
                print(Texts_module.arena_final_positive(arena_reward, self.arena_counter, self.player_gold))
                input()
                self.arena_counter += 1
            elif self.game_running():
                print(Texts_module.arena_final_negative())
                input()
            else:
                self.win_status = False
                break

        # Аналітика закінчення гри, фінальний екран
        if self.win_status == True:
            print(Texts_module.game_final_dashboard_winner(self.all_arenas))
        else:
            print(Texts_module.game_final_dashboard_looser())


        u_inp = ""
        while u_inp[0].lower() not in ["y", "n"]:
            u_inp = input("\n Do you wanna play one more time (yes/no) ---> ")
            if u_inp[0].lower() not in ["y", "n"]:
                print("Please, write correct answer.")

        if u_inp[0].lower() == "y":
            self.play()
        else:
            print("Thanks for playing. Good buy!")


game = Game_class()
game.play()