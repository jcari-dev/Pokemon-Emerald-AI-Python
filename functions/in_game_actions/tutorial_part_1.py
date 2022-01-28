
from images.comparasion_script.perform_action import perform_quick
import pyautogui
import json
from functions.in_game_actions.save_file import save_file
from .tutorial_part_2 import get_clock_to_actual_time
from functions.before_title_screen.check_ai_progress import update_overall_progress

def walk_into_room():
    player_data_file = open('player_data/playing_data.json')
    gender_data = json.load(player_data_file)
    gender_data_selection = gender_data["gender"]

    perform_quick('up')
    perform_quick('up')
    perform_quick('up')
    perform_quick('up')
    perform_quick('up')
    if gender_data_selection == 'girl':
        perform_quick('right')
        perform_quick('right')
        perform_quick('right')
    else:
        perform_quick('left')
        perform_quick('left')
        perform_quick('left')
    perform_quick('up')
    save_file()
    update_overall_progress("got_to_clock", True)
    return get_clock_to_actual_time()

def finish_talk_with_mom():
    print('starting talking with mom')
    player_data_file = open('player_data/playing_data.json')
    gender_data = json.load(player_data_file)
    gender_data_selection = gender_data["gender"]
    is_mom_done = None
    if gender_data_selection == 'boy':
        while (is_mom_done == None):
            try:
                is_mom_done = pyautogui.locateOnScreen(
                    'images/tutorial/is_mom_done_male.png', grayscale=True)
                print('Mom is done talking!')
            except Exception as e:
                perform_quick('c')
    else:
        while (is_mom_done == None):
            try:
                is_mom_done = pyautogui.locateOnScreen(
                    'images/tutorial/is_mom_done_female.png', grayscale=True)
                print('Mom is done talking!')
            except Exception as e:
                perform_quick('c')
    return walk_into_room()

def get_out_of_truck():
    perform_quick('right')
    perform_quick('right')
    perform_quick('right')
    perform_quick('right')
    print('get out of truck done')
    return finish_talk_with_mom()