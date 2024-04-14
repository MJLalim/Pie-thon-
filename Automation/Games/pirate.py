"""
Author:
    Michael John Andagan Lalim
Description:
    This is an automation for the pirate cast
    automatically heal and attack 
"""
import pyautogui as pag, time as t
class Pirate:
    def __init__(self,counter,userSkillChoice):
        self.counter = counter
        self.userSkillChoice = userSkillChoice
    #main function
    """
    def main():
        #ask user (fool proof)
        x=True
        while (x):
            try:
                counter = 0
                typeOfAttack = int(pag.prompt(text='Enter 1(no heals)\n2(with heals)\n3(all skills)\n4(all attacks no heals)', title='Type of attacks' , default=''))
            
                if (typeOfAttack == 1 or typeOfAttack == 2 or typeOfAttack == 3 or typeOfAttack == 4):
                    untilThisNum = int(pag.prompt(text='Number of runs', title='Runs: ', default=''))
                    t.sleep(2)
                    if (typeOfAttack == 1):
                        basicAttack(counter,untilThisNum)
                    elif (typeOfAttack == 2):
                        basic_Attack_N_Heal(counter,untilThisNum)
                    elif (typeOfAttack == 3):
                        all_Skills(counter,untilThisNum) 
                    else:
                        all_Attacks(counter,untilThisNum)
                    x=False
                else:
                    pag.alert(text='Error: Out Of Scope', title='Invalid Input', button='OK')
            except ValueError:
                pag.alert(text='Please enter a proper digit', title='Invalid Input', button='OK')
    """
    
    def basicAttack(counter):
        x = 0
        while(x < counter):
            t.sleep(0.5)
            pag.press('2')
            t.sleep(0.5)
            pag.press('1')
            t.sleep(2.5)
            pag.press('4')
            t.sleep(0.5)
            x+=1
    def allSkill(ounter):
        x = 0
        while(x < counter):
            t.sleep(0.5)
            pag.press('2')
            t.sleep(3)
            pag.press('3')
            t.sleep(0.3)
            pag.press('t')
            t.sleep(3)
            pag.press('4')
            t.sleep(3)
            pag.press('5')
            t.sleep(0.5)
            pag.press('1')
            x+=1

t.sleep(4)
Pirate.basicAttack(100)