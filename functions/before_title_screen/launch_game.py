import platform
import os
import subprocess
import time

from functions.before_title_screen.create_a_new_save import create_new_save
from functions.before_title_screen.check_ai_progress import check_ai_progress, check_last_progress
from images.comparasion_script.perform_action import perform_quick, perform
from .applescript_resize import emulator_resize
from .check_for_save import check_for_save_file
from .get_player_ready import start_new_game
from functions.in_game_actions.tutorial_part_1 import get_out_of_truck
from functions.in_game_actions.tutorial_part_2 import get_clock_to_actual_time
from .pass_title_screen import pass_screen_title

def check_os_launch_game():
    local_os = platform.system()

    if local_os == "Windows":
        print("Windows Detected, Launching Game!")
        os.startfile("..\\..\\rom\\rom.gba")
        return True
    elif local_os == "Darwin":
        print("MacOs Detected, Launching Game")
        valid_launch_input = False
        attempts = 4
        while valid_launch_input == False:
            launch_response = input(
                "Game may be ready to launch, do you want to launch it? (Y/N): "
            )
            if launch_response.casefold() == "y":
                valid_launch_input = True
                print("The game is ready to launch!")

                if check_for_save_file():
                    print('Save file found! Will continue from save file')
                    subprocess.call(['open', "rom/rom.gba"])
                    emulator_resize()
                    time.sleep(1)
                    if check_last_progress()[0] == 'in_the_truck':
                        pass_screen_title()
                        time.sleep(2)
                        # print('are we in truck?')
                        get_out_of_truck()
                    elif check_last_progress()[0] == 'got_to_clock':
                        print('Oh, you have not setup the in-game clock yet, lets do that!')
                        pass_screen_title()
                        get_clock_to_actual_time()
                    
                else:
                    double_check_save_file = input(
                        "=======================================================\nSince no save file was found, \nwould you like to start a new game? (Y/N): "
                    )
                    if double_check_save_file.casefold() == "y":
                        if create_new_save():
                            subprocess.call(['open', "rom/rom.gba"])
                            emulator_resize()
                            time.sleep(1)
                            start_new_game()
                    elif double_check_save_file.casefold() == 'n':
                        print(
                            "Then please double check your save file location. \nExiting application."
                        )
                    else:
                        print('Please try again, save file not found.')
                return True

            elif launch_response.casefold() == "n":
                valid_launch_input = True
                print("You cancelled the launch! Leaving now...")
                return False
            else:
                if attempts == 1:
                    print("Exiting application... please try again!")
                    return False
                attempts -= 1
                print(f"Invalid value, please try again. {attempts} remaning")

    else:
        print("If you have Linux we all cry.")
        return False
