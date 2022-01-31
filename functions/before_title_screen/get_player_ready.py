import time
import pyautogui
import time
from images.comparasion_script.perform_action import perform, perform_quick
from functions.in_game_actions.change_text_speed import change_text_speed_to_fast_and_start_game
from functions.in_game_actions.write_player_name import get_index_of_characters
from functions.in_game_actions.save_file import save_file
from functions.before_title_screen.check_ai_progress import update_overall_progress, check_last_progress
from functions.in_game_actions.tutorial_part_1 import get_out_of_truck
import json

pyautogui.useImageNotFoundException()


def get_to_truck():

    player_data_file = open('player_data/playing_data.json')
    gender_data = json.load(player_data_file)
    gender_data_selection = gender_data["gender"]
    if gender_data_selection == 'girl':
        is_truck_there = None
        while (is_truck_there == None):
            try:
                is_truck_there = pyautogui.locateOnScreen(
                    'images/starting_truck/starting_truck_ready_female.png',
                    grayscale=True)
                print('YAY WE OUT!')
            except Exception as e:
                perform('c')
    else:
        is_truck_there = None
        while (is_truck_there == None):
            try:
                is_truck_there = pyautogui.locateOnScreen(
                    'images/starting_truck/starting_truck_ready.png',
                    grayscale=True)
                print('YAY WE OUT!')
            except Exception as e:
                perform('c')
    save_file()
    update_overall_progress("in_the_truck", True)
    get_out_of_truck()


def write_name(name):
    actions_to_perform = get_index_of_characters(name)
    print(f'Will try to write {name}')
    for action in actions_to_perform:
        perform_quick(action)
        print(f'Did {action}')
    return get_to_truck()


def select_gender():
    player_data_file = open('player_data/playing_data.json')

    gender_data = json.load(player_data_file)

    gender_data_selection = gender_data["gender"]
    name_data_selection = gender_data["name"]

    if gender_data_selection == "boy":
        perform("x")
        perform("x")
        print("gender selected, boy")
    elif gender_data_selection == "girl":
        perform("down")
        perform("x")
        perform("x")
        print("gender selected, girl")
    return write_name(name_data_selection)


def get_to_select_gender():
    found_select_gender = None
    while (found_select_gender == None):
        try:
            time.sleep(2)
            found_select_gender = pyautogui.locateOnScreen(
                'images/begin_save/boy_girl.png', grayscale=True)
            print('IMAGE FOUND GENDER')
        except Exception as e:
            print('from exception')
            perform_quick('c')
    select_gender()


def start_new_game():
    # f = open("/images/begin_save/myfile.txt", "x")
    found_new_game = None
    while (found_new_game == None):
        try:
            found_new_game = pyautogui.locateOnScreen(
                'images/begin_save/new_game_option.png', grayscale=True)
            print('image found')
        except Exception as e:
            perform('enter')
    change_text_speed_to_fast_and_start_game()

    # perform('x')
    get_to_select_gender()
