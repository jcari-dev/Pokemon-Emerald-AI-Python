
from images.comparasion_script.perform_action import just_perform_do_not_check, perform_quick, perform, perform_super_quick
import pyautogui
from datetime import datetime
import time


def get_out_of_room():
    perform_quick('right')
    perform_quick('right')
    perform_quick('right')
    perform_quick('right')
    perform_quick('right')
    perform_quick('right')
    perform_quick('right')
    perform_quick('right')
    perform_quick('up')
    time.sleep(1)
    perform_quick('c')
    perform_quick('c')
    
    

def get_potion_out_of_pc():
    perform_quick('left')
    perform_quick('left')
    perform_quick('left')
    perform_quick('left')
    perform_quick('left')
    perform_quick('left')
    perform_quick('up')
    perform_quick('x')
    perform_quick('x')
    perform_quick('x')
    perform_quick('x')
    perform_quick('x')
    perform_quick('c')
    perform_quick('c')
    perform_quick('c')
    perform_quick('c')
    return get_out_of_room()

def get_clock_to_actual_time():
    perform_quick('x')
    perform_quick('c')
    perform_quick('c')
    now = datetime.now()
    current_time = now.strftime("%H:%M")
    print(current_time, 'this feature its not supported yet')
    perform_quick('x')
    perform_quick('up')
    perform_quick('x')
    time.sleep(3)
    perform_quick('c')
    perform_quick('c')
    perform_quick('c')
    perform_quick('c')
    perform_quick('c')
    return get_potion_out_of_pc()