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
        subprocess.call(['open', "~../../rom/rom.gba"])
        return True
    else:
        print('If you have Linux we all cry.')
        return False

