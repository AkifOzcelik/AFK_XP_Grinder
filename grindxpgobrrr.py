import keyboard
import time
import random

keys = ['w', 'a', 's', 'd', 'p', 'space'] # creates a list for keys (p is for left click)

def press(key): # function to press keys
    keyboard.press(key)
    keyboard.block_key(key) 
    time.sleep(1) #presses the key for 1 second
    keyboard.unblock_key(key)
    keyboard.release(key)

time.sleep(2) # gives you a two seconds time span to alt-tab to the game

while True:
    key = random.choice(keys) # picks a random key from the list
    press(key)
    if keyboard.is_pressed('j'): # if you press the J it stops the script (you have to spam it)
            break