import pygetwindow as gw
import time
import keyboard
import random
import ctypes

keys = []

exit_key = 'j'

selected_window = None
running = True  # Flag to control the loop

# Get a list of all open windows and display them for user selection
windows = gw.getAllTitles()

# Print all open window titles for user selection
print("Please select a window by typing the number next to it:")
for i, window in enumerate(windows):
    if window.strip():
        print(f'{i}: {window}')

# User selects a window
try:
    index = int(input('Please select the window number you want to activate: '))
    selected_window_title = windows[index]  # Store the title of the selected window
    print(f"You selected: {selected_window_title}")
except (ValueError, IndexError):
    print("Invalid selection. Please restart the script and select a valid window.")
    exit()

# Get the keys to press
try:
    selected_keys = input('Please select keys that the code should press (example: w a s d): ')
    if not selected_keys:
        print("No keys selected. Please select at least one key.")
    keys = list(selected_keys.replace(" ", ""))  # Remove spaces
    keys = set(keys)  # Convert to a set to remove duplicates
except Exception as e:
    print(f"Unexpected error during execution: {e}")

# Loop to find the selected window object
selected_window = gw.getWindowsWithTitle(selected_window_title)
if not selected_window:
    print(f"{selected_window_title} not found. Make sure it is open.")
    exit()

selected_window = selected_window[0]  # Get the actual window object
print(f"Found window: {selected_window.title}")
print(f"Window handle: {selected_window._hWnd}")  # Print the window handle for debugging

# Function to bring the window to the foreground
def bring_to_foreground(hwnd):
    ctypes.windll.user32.SetForegroundWindow(hwnd)

# Try to activate the window or bring it to the foreground
try:
    if selected_window.isMinimized:
        selected_window.restore()
        print("Window was minimized, now restored.")
    if not selected_window.isMinimized:
        selected_window.minimize()
        selected_window.restore()
        print("Window wasn't minimized, still restored.")

    # Bring the window to the front using Windows API
    bring_to_foreground(selected_window._hWnd)
    print(f"Window activated: {selected_window.title}")
    
except Exception as e:
    print(f"Error activating window: {e}")  # Output the error if there's an issue
    exit()

# Function to handle stopping the script
def stop_script():
    global running  # Access the running flag
    running = False  # Set the flag to False to exit the loop

# Use a hotkey to listen for the exit key
keyboard.add_hotkey(exit_key, stop_script)

# Loop for random key presses
while running:
    try:
        # If the selected window is active, press random keys
        if gw.getActiveWindow() == selected_window:
            key = random.choice(list(keys))  # Convert back to list to use choice
            keyboard.press(key)
            time.sleep(1)
            keyboard.release(key)
        else:
            print("Window is not active, script paused.")
            time.sleep(3)
    except Exception as e:
        print(f"Unexpected error during execution: {e}")
        break

print("Script has been stopped.")  # Indicate the script has finished
