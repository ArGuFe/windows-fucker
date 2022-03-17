import random
import pyautogui
import time

time.sleep(30)

while True:
    height = random.randint(0, 1080)
    weight = random.randint(0, 1920)

    pyautogui.click(height, weight, duration=0.1)
    pyautogui.hotkey('winleft', 'm')
