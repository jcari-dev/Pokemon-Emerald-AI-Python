import platform
import os
import subprocess

from functions.before_title_screen.create_a_new_save import create_new_save

from .applescript_resize import emulator_resize
from .check_for_save import check_for_save_file


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
            if launch_response == "y":
                valid_launch_input = True
                print("The game is ready to launch!")
                # subprocess.call(['open', "~../../rom/rom.gba"])
                # emulator_resize()
                if check_for_save_file():
                    continue
                else:
                    double_check_save_file = input(
                        "=======================================================\nSince no save file was found, \nwould you like to start a new game? (Y/N): "
                    )
                    if double_check_save_file.lower() == "y":
                        create_new_save()
                    else:
                        print(
                            "Then please double check your save file location. \nExiting application."
                        )

                return True
            elif launch_response == "n":
                valid_launch_input = True
                print("You cancelled the launch! Leaving now...")
                return False
            else:
                if attempts == 1:
                    print("Exiting application... please try again!")
                    return False
                    break
                attempts -= 1
                print(f"Invalid value, please try again. {attempts} remaning")

    else:
        print("If you have Linux we all cry.")
        return False
