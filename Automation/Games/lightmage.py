"""
Author:
    Michael John Andagan Lalim
Description:
    This is an automation for the lightmage cast
    automatically heal and attack 
"""

import pyautogui as pag
import time as t
import BackEnd

from tkinter import *
from tkinter import messagebox
def typeOfAttack():
    
    try:
        typeClass = int(pag.prompt(text='1-Mage\n2-Pirate\n3-LightMage\n4-Eternal Inversionist',title='Type of attacks'))
        if (3 <= typeClass <= 4):
            typeOfAttack = int(pag.prompt(text='1-Basic Attacks\n2-Attack with Heals\n3-All Skills\n', title='Type of attacks'))
        elif(1 <= typeClass <= 2):
            typeOfAttack = int(pag.prompt(text='1-Basic Attacks\n2-All Skills\n', title='Type of attacks'))
        else:
            messagebox.showerror(title='Error: Value input of outscope', message='Please enter an integer within range')
        return typeOfAttack
    except ValueError:
        pag.alert(text='Please enter a proper digit', title='Invalid Input', button='OK')
def numO_Runs():
    try:
        typeClass = int(pag.prompt(text='Number of runs:\n',title='Run how many times?'))
        return typeOfAttack
    except ValueError:
        pag.alert(text='Please enter a proper digit', title='Invalid Input', button='OK')
    
def main():
    #ask user (fool proof)
    x=True
    while (x):
        try:
            counter = 0
            attackType = typeOfAttack()
            numRuns = numO_Runs()
        except ValueError:
            pag.alert(text='Please enter a proper digit', title='Invalid Input', button='OK')

t.sleep(5)
while True:
    BackEnd.Eternal_Inversionist.allAttack()