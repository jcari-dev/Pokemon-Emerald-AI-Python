from images.comparasion_script.perform_action import perform_quick
import time
import pyautogui

def save_file():
    perform_quick('enter')
    where_is_cursor_exit = pyautogui.locateOnScreen(
        'images/save/save_location_exit.png',
        grayscale=True)
    if where_is_cursor_exit:
        perform_quick('up')
        perform_quick('up')
    else: 
        perform_quick('up')
        perform_quick('up')
        perform_quick('up')
    perform_quick('x')
    perform_quick('x')
    time.sleep(5)
    print('Game successfully saved!')