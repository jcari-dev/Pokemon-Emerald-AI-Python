import pyautogui
from images.comparasion_script.perform_action import perform


def change_text_speed_to_fast_and_start_game():

    went_down = None
    while (went_down == None):
        try:
            perform('down')
            print('attempting go to option')
            went_down = pyautogui.locateOnScreen(
                'images/begin_save/change_test_speed/option_selection.png')
            perform('x')
        except pyautogui.ImageNotFoundException:
            print('Image not found')
    went_right = None
    while (went_right == None):
        try:
            perform('right')
            went_right = pyautogui.locateOnScreen(
                'images/begin_save/change_test_speed/text_speed_fast.png')
        except pyautogui.ImageNotFoundException:
            print('Image not found (going to fast right)')
    going_back = None
    while (going_back == None):
        try:
            perform('c')
            going_back = pyautogui.locateOnScreen(
                'images/begin_save/change_test_speed/option_selection.png')
            if going_back:
                perform('up')
                perform('x')
                print('Changed successfully test speed to fast')
        except pyautogui.ImageNotFoundException:
            print('Image not found')
