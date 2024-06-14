import UNIT_CLASSES

def game_welcome_board():
    return '''
    ----------------------------------------------------------------------------------------------------------------
    
                                    **********   GAME OF HEROES   **********
    
                                        -- The game by Ivan Shamrikov --
    
    ----------------------------------------------------------------------------------------------------------------
    '''

def get_player_name():
    return "Hello Hero! What is your name? --->"

def welcome_young_hero(player_name, player_gold, all_arenas):
    return f'''
        Welcome, my young hero {player_name}!
        Here is some money({player_gold}), you need to create your own squad and fight in {all_arenas} arenas.
        Let's play the Game!
        '''

def wow_you_have_a_squad(player_team):
    text = '''
        Wow! You have a squad from 4 heroes!
        '''
    for unit in player_team:
        text += "\n" + unit.unit_info()

    text += "\n" + "-"*50

    return text

def arena_final_positive(arena_reward, arena_counter, player_gold):
    return f'''\n\n
    You get {arena_reward}gold for successful battle in Arena {arena_counter}.
    Now you have {player_gold} gold!
    Are you ready to prepare for the next Arena? 
    Let's go shopping to buy new units and items!
    \n\n
    Press ENTER to continue -->
    '''

def arena_final_negative():
    return '''
        You loose in this arena. You should buy a new squad.

            Are you ready to prepare for this Arena one more time? 
            Let's go shopping to buy new units and items!

        Press ENTER to continue -->
        '''

def game_final_dashboard_winner(all_arenas):
    return f'''
        -----------------------------------------------------
                    ******** GAME OVER ********
                        You win the Game
        -----------------------------------------------------
                    You have won in all {all_arenas} Arenas
         '''

def game_final_dashboard_looser():
    return '''
        ------------------------------------------------------------
                        ******** GAME OVER ********
                           You loose the Game
        ------------------------------------------------------------
                    You have no money to buy full squad
            '''


def display_arena_board(counter_arena, player_team, comp_team):
    return f'''
            ------------------------------------------------------------
                        ******** ARENA #{counter_arena} BOARD ********
            ------------------------------------------------------------
                                Welcome to the Arena!
            {player_team.name}                VS                  {comp_team.name}

        '''

def choose_unit(fight_counter):
    return f'''
    -------------------------------
    CHOOSE UNITS TO THE FIGHT #{fight_counter}!
    '''

def fight_board(attacker, defender, fight_counter):
    return f'''
    ---------------------------------
    ******** FIGHT #{fight_counter} BOARD ********
    ---------------------------------
    Attacker     VS          Defender
    {attacker.name}                   {defender.name}
    
    Attacker - {attacker.unit_info()}
    Defender - {defender.unit_info()}
    
    LET'S THE FIGT BEGIN
    '''

def fight_result_board(attacker, defender):
    return f'''
    {attacker.name} hit {defender.name} by {attacker.hit_power_for_fight()} points
    {defender.name} hit {attacker.name} by {defender.hit_power_for_fight()} points
    
    {attacker.name} status - {attacker.status}, health: {attacker.health_in_arena}
    {defender.name} status - {defender.status}, health: {defender.health_in_arena}
        
    -------------------------------
    '''