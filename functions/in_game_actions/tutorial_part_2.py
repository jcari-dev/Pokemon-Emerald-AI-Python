

from images.comparasion_script.perform_action import just_perform_do_not_check, perform_quick, perform, perform_super_quick
import pyautogui
from datetime import datetime
import time
from .save_file import save_file
from functions.before_title_screen.check_ai_progress import update_overall_progress


def select_starter():
    perform_super_quick('left')
    perform_super_quick('left')
    perform_super_quick('left')
    perform_super_quick('left')
    perform_super_quick('up')
    perform_super_quick('x')
    

def check_professor():
    perform_super_quick('left')
    perform_super_quick('left')
    perform_super_quick('left')
    perform_super_quick('left')
    perform_super_quick('up')
    perform_super_quick('up')
    perform_super_quick('up')
    perform_super_quick('up')
    perform_super_quick('up')
    perform_super_quick('up')
    perform_super_quick('up')
    perform_super_quick('up')
    perform_super_quick('up')
    time.sleep(1)
    little_girl_done = None
    while (little_girl_done == None):
        try:
            little_girl_done = pyautogui.locateOnScreen(
                'images/tutorial/little_villager_girl_done_talking_LITTLEROOT.png',
                grayscale=True)
            print('Shes done talking!')
        except Exception as e:
            perform('c')
    perform_super_quick('up')
    perform_super_quick('up')
    perform_super_quick('up')
    perform_super_quick('c')
    birch_done_talking = None
    while (birch_done_talking == None):
        try:
            birch_done_talking = pyautogui.locateOnScreen(
                'images/tutorial/birch_is_done_talking.png',
                grayscale=True)
            print('Time to select starter')
        except Exception as e:
            perform('c')
    return select_starter()

def get_out_of_rival_room():
    perform_super_quick('left')
    perform_super_quick('left')
    perform_super_quick('left')
    perform_super_quick('left')
    perform_super_quick('left')
    perform_super_quick('up')
    perform_super_quick('up')
    perform_super_quick('up')
    perform_super_quick('up')
    perform_super_quick('down')
    perform_super_quick('down')
    perform_super_quick('down')
    perform_super_quick('down')
    perform_super_quick('down')
    perform_super_quick('down')
    save_file()
    return check_professor()

def go_to_neighboor():
    perform_super_quick('right')
    perform_super_quick('right')
    perform_super_quick('right')
    perform_super_quick('right')
    perform_super_quick('right')
    perform_super_quick('right')
    perform_super_quick('right')
    perform_super_quick('right')
    perform_super_quick('right')
    perform_super_quick('right')
    perform_super_quick('up')
    rival_mom_done = None
    while (rival_mom_done == None):
        try:
            rival_mom_done = pyautogui.locateOnScreen(
                'images/tutorial/rival_mom_talking_done_male.png',
                grayscale=True)
            print('Shes done talking!')
        except Exception as e:
            perform('c')
    perform_super_quick('up')
    perform_super_quick('up')
    perform_super_quick('up')
    perform_super_quick('up')
    perform_super_quick('up')
    perform_super_quick('up')
    perform_super_quick('up')
    time.sleep(2.5)
    perform_super_quick('down')
    perform_super_quick('down')
    perform_super_quick('down')
    perform_super_quick('right')
    perform_super_quick('right')
    perform_super_quick('right')
    perform_super_quick('right')
    perform_super_quick('right')
    perform_super_quick('up')
    perform_super_quick('x')
    rival_done_pc = None
    while (rival_done_pc == None):
        try:
            rival_done_pc = pyautogui.locateOnScreen(
                'images/tutorial/rival_is_done_male.png',
                grayscale=True)
            print('Shes done talking!')
        except Exception as e:
            perform('c')



def see_dad_on_tv():
    is_mom_done = None
    while (is_mom_done == None):
        try:
            is_mom_done = pyautogui.locateOnScreen(
                'images/tutorial/mom_after_clock_male.png',
                grayscale=True)
            print('YAY WE OUT!')
        except Exception as e:
            perform('c')
    print('Mom is done talking, lets head out')
    perform_super_quick('right')
    perform_super_quick('right')
    perform_super_quick('right')
    perform_super_quick('right')
    perform_super_quick('right')
    perform_super_quick('down')
    perform_super_quick('down')
    perform_super_quick('down')
    perform_super_quick('down')
    perform_super_quick('down')
    time.sleep(2.5)
    save_file()
    return go_to_neighboor()

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
    perform_quick('up')
    time.sleep(1)
    return see_dad_on_tv()
    
    

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