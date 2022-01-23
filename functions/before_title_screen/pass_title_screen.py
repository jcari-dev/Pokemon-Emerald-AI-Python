from images.comparasion_script.perform_action import perform_quick, perform

# from pathlib import Path

def pass_screen_title():
    
    found_save_game = None
    # loaded_save = None

    while found_save_game == None:
        try:
            found_save_game = pyautogui.locateOnScreen(
                'images/pass_title_screen/continue.png', grayscale=True, region=(0, 59, 955, 630), confidence=0.5)
            print('Save found!')
        except Exception as e:
            print('save game not found! retrying!')
            perform('enter')
            # perform('x')
            
    # while loaded_save == None:
    #     try:
    #         loaded_save = pyautogui.locateOnScreen(
    #             'images/pass_title_screen/loaded_save.png', grayscale=True)
    #         print('Save found!')
    #     except Exception as e:
    #         perform('x')
    