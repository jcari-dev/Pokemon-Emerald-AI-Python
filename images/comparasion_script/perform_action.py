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
        return perform(action)
    else:
        print('Action completed')
        return True
    
def perform_quick(action):
    # time.sleep(3)
    image_before_action = pyautogui.screenshot('images/comparasion_script/image_before.png',
                                               region=(0, 59, 955, 630))
    # image_before_pixels = Image.open(image_before_action).getdata()
    # time.sleep(1)
    pyautogui.keyDown(action)
    # time.sleep(0.2)
    pyautogui.keyUp(action)
    image_after_action = pyautogui.screenshot('images/comparasion_script/image_after.png',
                                              region=(0, 59, 955, 630))
    img1 = Image.open('image_before.png').convert('RGB')
    img2 = Image.open('image_after.png').convert('RGB')
    difference = ImageChops.difference(img1, img2).getbbox()

    time.sleep(1)

    if difference == None:
        print('Action attempted, but screen did not changed. retrying')
        return perform(action)
    else:
        print('Action completed')
        return True
    
def perform_super_quick(action):
    # time.sleep(3)
    image_before_action = pyautogui.screenshot('images/comparasion_script/image_before.png',
                                               region=(0, 59, 955, 630))
    # image_before_pixels = Image.open(image_before_action).getdata()
    # time.sleep(1)
    pyautogui.keyDown(action)
    # time.sleep(0.2)
    pyautogui.keyUp(action)
    image_after_action = pyautogui.screenshot('images/comparasion_script/image_after.png',
                                              region=(0, 59, 955, 630))
    img1 = Image.open('image_before.png').convert('RGB')
    img2 = Image.open('image_after.png').convert('RGB')
    difference = ImageChops.difference(img1, img2).getbbox()

    # time.sleep(1)

    if difference == None:
        print('Action attempted, but screen did not changed. retrying')
        return perform(action)
    else:
        print('Action completed')
        return True
    
def just_perform_do_not_check(action):
    image_before_action = pyautogui.screenshot('images/comparasion_script/image_before.png',
                                               region=(0, 59, 955, 630))

    pyautogui.press(action)
    time.sleep(0.5)
    image_after_action = pyautogui.screenshot('images/comparasion_script/image_after.png',
                                              region=(0, 59, 955, 630))
    img1 = Image.open('image_before.png').convert('RGB')
    img2 = Image.open('image_after.png').convert('RGB')
    difference = ImageChops.difference(img1, img2).getbbox()

    time.sleep(0.5)

    if difference == None:
        print('Action attempted, but screen did not changed. retrying')
        return perform(action)
    else:
        print('Action completed')
        return True

    
# def perform_series(action, times):
#     # time.sleep(3)
#     image_before_action = pyautogui.screenshot('images/comparasion_script/image_before.png',
#                                                region=(0, 59, 955, 630))
#     # image_before_pixels = Image.open(image_before_action).getdata()
#     time.sleep(1)
#     pyautogui.keyDown(action)
#     time.sleep(0.2)
#     pyautogui.keyUp(action)
#     image_after_action = pyautogui.screenshot('images/comparasion_script/image_after.png',
#                                               region=(0, 59, 955, 630))
#     img1 = Image.open('image_before.png').convert('RGB')
#     img2 = Image.open('image_after.png').convert('RGB')
#     difference = ImageChops.difference(img1, img2).getbbox()

#     time.sleep(1)

#     if difference == None:
#         print('Action attempted, but screen did not changed. retrying')
#         return perform(action)
#     else:
#         print('Action completed')
#         return True
# time.sleep(2)
# perform_quick('right')
# perform_quick('right')
# perform_quick('right')
# perform_quick('right')