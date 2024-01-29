"""
Author: Michael John Andagan Lalim
Date created: February ‎20, ‎2023, ‏‎5:21:26 PM
Description: Simple code to spam text messages; make sure to first open the messaging app and the chat box is clicked.
Purpose: To annoy my friends :)
"""
import pyautogui as pag, time as t; t.sleep(3);text = 'testttttt spamm';i=0
while i<10:
    pag.typewrite(text);t.sleep(1);pag.hotkey('enter');t.sleep(1)
