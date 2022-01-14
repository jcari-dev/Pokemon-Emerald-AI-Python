import time
import pyautogui
import time
from pyscreeze import ImageNotFoundException
from images.comparasion_script.perform_action import perform
from functions.in_game_actions.change_text_speed import change_text_speed_to_fast_and_start_game
import json

pyautogui.useImageNotFoundException()


def select_gender():
    player_data_file = open('player_data/playing_data.json')

    gender_data = json.load(player_data_file)

    gender_data_selection = gender_data["gender"]

    if gender_data_selection == "boy":
        perform("x")
        perform("x")
        print("gender selected, boy")
    elif gender_data_selection == "girl":
        perform("down")
        perform("x")
        perform("x")
        print("gender selected, girl")


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
            perform('x')
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
