from images.comparasion_script.perform_action import perform_quick, perform
import pyautogui
# from pathlib import Path

def pass_screen_title():
    
    found_save_game = None

    while found_save_game == None:
        try:
            found_save_game = pyautogui.locateOnScreen(
                '/Users/jorgecaridad/Desktop/PokemonEmeraldAi/Pokemon-Emerald-AI-Python/images/pass_title_screen/continue.png')
            print('Save found!')
            perform_quick('x')
        except Exception as e:
            print('save game not found! retrying!')
            perform_quick('enter')
            # perform('x')
            
    # while loaded_save == None:
    #     try:
    #         loaded_save = pyautogui.locateOnScreen(
    #             'images/pass_title_screen/loaded_save.png', grayscale=True)
    #         print('Save found!')
    #     except Exception as e:
    #         perform('x')
    