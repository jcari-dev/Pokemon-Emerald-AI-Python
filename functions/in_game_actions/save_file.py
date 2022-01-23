from images.comparasion_script.perform_action import perform_quick
import time


def save_file():
    perform_quick('enter')
    perform_quick('up')
    perform_quick('up')
    perform_quick('up')
    perform_quick('x')
    perform_quick('x')
    time.sleep(5)
    print('Game successfully saved!')