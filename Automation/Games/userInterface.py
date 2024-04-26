"""
Author: 
    Michael John Andagan Lalim
Description:
    An app for AQW auto farming
    TO DO:
    --------
    1. Buttons for the types of classes
    2. Prompts user the number of runs ( stored in untilThisNum)
    3. call the function with the right parameters
Comment:
    2024-04-14: 
        "It's hard to start learning tkinter stuff, so I copied a code from github: credits @pralabhsaxena05
        just edit some stuff up so you can actually use it"
    2024-04-16:
        "I deleted the code that I copied and copied a code from stackoverflow for quitting using a keyboard
        stroke"
"""
#Python library
import tkinter as tk
import pyautogui as pag
import time as t
import threading

def basicAttack():
    while is_running:
        #1st skill
        pag.press('t'); pag.press('2')
        
        #cooldown
        coolDown()

        #2nd skill
        pag.press('t'); pag.press('3')
        
        #cooldown
        coolDown()
        
        #3rd skill 
        pag.press('t'); pag.press('4')
        
        #4th skill 
        pag.press('t'); pag.press('5')
        
        #cooldown
        coolDown()

def coolDown():
    for i in range(2):
        if not is_running:
            break
        pag.press('t'); pag.press('1'); pag.press('1')

def toggle_attack(event=None):
    global is_running
    if is_running:
        is_running = False
    else:
        is_running = True
        threading.Thread(target=basicAttack).start()

root = tk.Tk()
root.geometry("800x600")  # Set the size of the window to 800x600
is_running = False

# Create a button that will call toggle_attack when clicked
button = tk.Button(root, text="Toggle Attack", command=toggle_attack)
button.pack()

# Bind a key (e.g., the 'Q' key) to start the attack
root.bind('<Shift-q>', toggle_attack)

# Bind a key (e.g., the 'E' key) to stop the attack
root.bind('<Shift-e>', toggle_attack)

root.mainloop()
