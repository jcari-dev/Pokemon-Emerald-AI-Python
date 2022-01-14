import pyautogui
import time
from PIL import ImageChops, Image


def perform(action):
    # time.sleep(3)
    image_before_action = pyautogui.screenshot('images/comparasion_script/image_before.png',
                                               region=(0, 59, 955, 630))
    # image_before_pixels = Image.open(image_before_action).getdata()
    time.sleep(1)
    pyautogui.keyDown(action)
    time.sleep(0.2)
    pyautogui.keyUp(action)
    image_after_action = pyautogui.screenshot('images/comparasion_script/image_after.png',
                                              region=(0, 59, 955, 630))
    img1 = Image.open('image_before.png').convert('RGB')
    img2 = Image.open('image_after.png').convert('RGB')
    difference = ImageChops.difference(img1, img2).getbbox()

    time.sleep(1)

    if difference == None:
        print('Action attempted, but screen did not changed. retrying')
<<<<<<< HEAD
        return perform(action)
    else:
        print('Action completed')
        return True
=======

        return perform(action)
    else:
        print('Action completed')
        return True
>>>>>>> 26011173d62d8452cd9916a470c5935e789be1f5
