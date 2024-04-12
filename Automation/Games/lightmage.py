"""
Author:
    Michael John Andagan Lalim
Description:
    This is an automation for the lightmage cast
    automatically heal and attack 
"""

import pyautogui as pag
import time as t

counter = 0
userInterface = int(pag.prompt(text='Hello', title='Enter number of tries', default=''))
t.sleep(5)
userInterface 
while (counter < userInterface ):
    t.sleep(1)
    pag.press('1')#auto attack
    t.sleep(1)
    pag.press('4')#auto heal
    t.sleep(1)
    counter += 1
    t.sleep(1)