import time
import pyautogui
import time
from pyscreeze import ImageNotFoundException
from images.comparasion_script.perform_action import perform
from functions.in_game_actions.change_text_speed import change_text_speed_to_fast

pyautogui.useImageNotFoundException()




def get_to_select_gender():
    found_select_gender = None
    while (found_select_gender == None):
        try:
            found_select_gender = pyautogui.locateOnScreen('images/begin_save/boy_girl.png')
            print('IMAGE FOUND GENDER')
        except Exception as e:
            perform('x')

def start_new_game():
    # f = open("/images/begin_save/myfile.txt", "x")
    found_new_game = None
    while (found_new_game == None):
        try:
            found_new_game = pyautogui.locateOnScreen(
                'images/begin_save/new_game_option.png')
            print('image found')
        except Exception as e:
            perform('enter')
    change_text_speed_to_fast()
    perform('x')
    get_to_select_gender()

