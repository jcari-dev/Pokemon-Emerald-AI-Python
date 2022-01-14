
from .player_name_entry_input import validate_gender, validate_name, validate_stater, validate_starter_selection, validate_real_time_clock, starter_number_to_name
from .save_player_data import write_player_data

def time_clock(save_options):
    valid_clock_response = False
    while valid_clock_response == False:
        real_time_clock = input(
            "Do you want to use your device's time? (Y/N): ")
        if validate_real_time_clock(real_time_clock):
            valid_clock_response = True
            save_options["real_clock"] = real_time_clock
            write_player_data(save_options)
            return True
    


def starter_save(save_options):

    valid_optimal_starer = False
    valid_custom_starter = False
    while valid_optimal_starer == False and valid_custom_starter == False:
        optimal_starter_pick = input(
            "Do you want the bot, to select the optimal starter Pokemon, or you want to select one that you like? (optimal/custom): "
        )
        if validate_stater(optimal_starter_pick):
            if optimal_starter_pick.casefold() == 'optimal':
                valid_optimal_starer = True
                save_options['starter'] = optimal_starter_pick
                time_clock(save_options)
                return True
                
            else:
                while valid_custom_starter == False:
                    player_starter_pokemon = input(
                        "Select your starter Pokemon Treecko, Torchic, or Mudkip? (1,2,3): "
                    )
                    if validate_starter_selection(player_starter_pokemon):
                        save_options['starter'] = starter_number_to_name(
                            player_starter_pokemon)
                        valid_custom_starter = True
                        time_clock(save_options)
                        return True



def create_new_save():
    print("\033[92m" + "Welcome to JC's Pokemon Emerald Bot!" + "\033[0m")
    print(
        "\n======================================================= \nPlease be sure to answer these questions! If you want a random value for each response just press leave them empty! \n======================================================="
    )
    valid_player_name = False
    valid_player_gender = False
    save_options = {"name": "", "gender": "", "starter": "", "real_clock": ""}

    while valid_player_name == False:
        player_name = input(
            "What is your name? We currently support [A-z], [0-9], [,.!?/-\"'] Maximum 7 characters, e.g. Leg3n-d, cool right? \nI can also give you a name myself (not implemented yet, but soon!) just type 'nameMe': "
        )
        if validate_name(player_name):
            valid_player_name = True
            save_options['name'] = player_name
            print(f"Hello {player_name}!")

    while valid_player_gender == False:
        player_gender = input(
            "Are you a boy or a girl? (The game literally needs to know this, it's okay to lie! ) (boy/girl): "
        )
        if validate_gender(player_gender):
            valid_player_gender = True
            save_options['gender'] = player_gender
 
    if starter_save(save_options):
        return True
