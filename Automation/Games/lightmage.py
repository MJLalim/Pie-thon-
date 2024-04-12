"""
Author:
    Michael John Andagan Lalim
Description:
    This is an automation for the lightmage cast
    automatically heal and attack 
"""

import pyautogui as pag
import time as t

def main():
    #ask user (fool proof)
    x=True
    while (x):
        try:
            counter = 0
            typeOfAttack = int(pag.prompt(text='Enter 1(no heals) or 2(with heals)', title='Type of attacks' , default=''))
        
            if (typeOfAttack == 1 or typeOfAttack == 2):
                x=False
            else:
                pag.alert(text='Error: Out Of Scope', title='Invalid Input', button='OK')
        except ValueError:
            pag.alert(text='Please enter a proper digit', title='Invalid Input', button='OK')
        
        
            
    untilThisNum = int(pag.prompt(text='Number of runs', title='Runs: ', default=''))
    t.sleep(2)
    if (typeOfAttack == 1):
        attacks(counter,untilThisNum)
    else:
        all_Skills(counter,untilThisNum)   
            
#only attakcs
def attacks(counter,untilThisNum):
    while (counter < untilThisNum ):
        t.sleep(1)
        pag.press('2')#auto attack: skill 
        t.sleep(3)#cooldown
        pag.press('3')#auto attack: skill 
        t.sleep(3)#cooldown
        pag.press('1')#auto attack
        t.sleep(2)
        counter += 1

#attack and heal      
def all_Skills(counter,userInterface):
    while (counter < untilThisNum ):
        t.sleep(1)
        pag.hotkey('2')#auto attack: skill 
        t.sleep(3)#cooldown
        pag.hotkey('3')#auto attack: skill 
        t.sleep(3)#cooldown
        pag.hotkey('1')#auto attack
        t.sleep(3)#cooldown
        pag.hotkey('4')#auto heal
        counter += 1
        t.sleep(7) #giving time to cool down

main()