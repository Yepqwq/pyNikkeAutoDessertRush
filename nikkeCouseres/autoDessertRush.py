# -*- coding: utf-8 -*-
# Edit by Yepqwq
import time

import pyautogui
import pydirectinput

button_left = pyautogui.locateOnScreen(image="img/left.png", confidence=0.7)
button_right = pyautogui.locateOnScreen(image="img/right.png", confidence=0.7)
button_py = pyautogui.locateOnScreen(image="img/pyc.png", confidence=0.7)
print("find button successful")
while 1:

    try:
        if pyautogui.locateOnScreen(image='img/cake.png',confidence=0.5):
            print("cake")
            pydirectinput.moveTo(pyautogui.center(button_left)[0],pyautogui.center(button_left)[1])
            pydirectinput.click()
    except pyautogui.ImageNotFoundException:
        print("bomb")
        pydirectinput.moveTo(pyautogui.center(button_right)[0],pyautogui.center(button_right)[1])
        pydirectinput.click()
