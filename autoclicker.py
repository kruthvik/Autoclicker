import pyautogui
from tkinter import*
from pynput import keyboard
import sys
import threading

root = Tk()
root.geometry("300x150")
root.wm_attributes("-topmost", 1)
root.config(background = "red")
root.resizable(False, False)

status = Label(root, fg = "white", bg = "red", text="Off", font=("Times New Roman", 25))
status.pack(pady=15)

clicking = False
running = True

DELAY = 0.005
left_click = True

click_type = Label(root, fg = "Grey", bg = "red", text = "Mode: Left Click", font=("Times New Roman", 18))
click_type.pack(pady=5)

exit_button = keyboard.Key.f12
hotkey = keyboard.Key.caps_lock



def on_release(key):
    global clicking, running, left_click

    if key == hotkey:
        clicking = not clicking
        if clicking:
            root.config(background = "green")

            status['text'] = "On"
            status['bg'] = "green"

            click_type['bg'] = 'green'
        else:
            root.config(background = "red")

            status['text'] = "Off"
            status['bg'] = "red"
            
            click_type['bg'] = 'red'

    elif key == exit_button:
        running = False
        root.destroy()

    elif key == keyboard.Key.pause:
        left_click = not left_click
        text = "Left Click" if left_click else "Right Click"
        click_type.config(text=f"Mode: {text}")

    elif key == keyboard.Key.menu:
        root.overrideredirect(1)
    

def on_press(key):
    pass

def main():
    lis = keyboard.Listener (on_release=on_release)
    lis.start()

    while running:  
        while clicking:
            pyautogui.click(button = "left" if left_click else "right")
            pyautogui.PAUSE = DELAY

def on_quit():
    global running
    root.destroy()
    running = False

a = threading.Thread(target=main)
a.start()


root.protocol("WM_DELETE_WINDOW", on_quit)
root.mainloop()


