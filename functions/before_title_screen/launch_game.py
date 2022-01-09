import platform
import os
import subprocess


def check_os_launch_game():

    local_os = platform.system()

    if local_os == 'Windows':
        print('Windows Detected, Launching Game!')
        os.startfile("..\\..\\rom\\rom.gba")
        return True
    elif local_os == 'Darwin':
        print('MacOs Detected, Launching Game')
        valid_launch_input = False
        attempts = 4
        while(valid_launch_input == False):
            launch_response = input(
                "Game may be ready to launch, do you want to launch it? (Y/N)")
            if launch_response == "y":
                valid_launch_input = True
                print('Launching Pokemon Emerald!')
                subprocess.call(['open', "~../../rom/rom.gba"])
            elif launch_response == "n":
                valid_launch_input = True
                print('You cancelled the launch! Leaving now...')
            else:
                if(attempts == 1):
                    print('Exiting application... please try again!')
                    break
                attempts -= 1
                print(f"Invalid value, please try again. {attempts} remaning")

    else:
        print('If you have Linux we all cry.')
        return False
