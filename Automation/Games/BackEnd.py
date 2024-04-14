import pyautogui as pag
import time as t

#*********THIS BLOCK IS FOR IN-BETWEEN SKILLS COOLDOWN***************#
#Theoritically takes 3 seconds
def coolDown():
    for i in range(3):
        pag.press('t'); pag.press('1'); pag.press('1'); t.sleep(1)
#*********THIS BLOCK IS FOR IN-BETWEEN SKILLS COOLDOWN***************#

#**********************THIS BLOCK IS FOR CLASSES*************************#
class Pirate:
    def __init__(self,counter,untilThisNum):
        self.counter = counter
        self.userSkillChoice = userSkillChoice
        
    def basicAttack(counter,untilThisNum):
        while(counter < untilThisNum):
            #1st skill
            pag.press('t'); pag.press('2')
            
            #cooldown
            coolDown()
            
            #2nd skill
            pag.press('t'); pag.press('4')
            
            counter+=1
    def allSkill(counter,untilThisNum):
        while(counter < untilThisNum):
            #1st skill
            pag.press('t'); pag.press('2')
            
            #cooldown
            coolDown()
            
            #2nd skill
            pag.press('t');pag.press('3')
            #cooldown
            coolDown()

            #3rd skill
            pag.press('t'); pag.press('4')
            #cooldown
            coolDown()
            
            #4th skill
            pag.press('t');pag.press('5')
            #cooldown
            coolDown()
            
            counter+=1

            
class Eternal_Inversionist:
    def __init__(self,counter,untilThisNum):
        self.counter = counter
        self.untilThisNum = untilThisNum
    
    def basicAttack(counter,untilThisNum):
        while (counter < untilThisNum ):
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
            
            #cooldown
            coolDown()
            
            counter += 1
    def allAttack(counter,untilThisNum):
        while (counter < untilThisNum ):
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
            
            #cooldown
            coolDown()
            
            #4th skill 
            pag.press('t'); pag.press('5')
            
            #cooldown
            coolDown()
            
            counter += 1      
class Mage:
    def __init__(self,counter,untilThisNum):
        self.counter = counter
        self.untilThisNum = untilThisNum
        
    def basicAttack(counter,untilThisNum):
        while(counter<untilThisNum):
            #skill: Attack everyone
            pag.press('t');pag.press('4')
            
            #cooldown
            coolDown()
            
            #skill: Ice
            pag.press('t');pag.press('3')
            
            #cooldown
            coolDown()
            
            #skill: Fire
            pag.press('t');pag.press('2')
            
            counter += 1

class LightMage:
    def __init__(self,counter,untilThisNum):
        self.counter = counter
        self.untilThisNum = untilThisNum
        
    #these only work for light mages   
    def basic_Combo(self):
        while (counter < untilThisNum ):
            pag.press('t');pag.press('2')#auto attack: skill 
            coolDown()#cooldown
            
            pag.press('t');pag.press('3')#auto attack: skill 
            coolDown()#cooldown
            
            counter += 1
            
    #attack and heal      
    def basic_Attack_N_Heal(counter,untilThisNum):
        while (counter < untilThisNum ):
            pag.press('t');pag.press('2')#auto attack: skill 
            coolDown()#cooldown
            
            pag.press('t');pag.press('3')#auto attack: skill 
            coolDown()#cooldown
            
            pag.press('t');pag.press('4')#auto attack: skill 
            coolDown()#cooldown
            
            counter += 1

    #all skills
    def all_Skills(counter,untilThisNum):
        while (counter < untilThisNum ):
            pag.press('t');pag.press('2')#auto attack: skill 
            coolDown()#cooldown
                
            pag.press('t');pag.press('3')#auto attack: skill 
            coolDown()#cooldown
                
            pag.press('t');pag.press('4')#auto attack: skill 
            coolDown()#cooldown
                
            pag.press('t');pag.press('5')#auto attack: skill 
            coolDown()#cooldown
                
            counter += 1

t.sleep(5)
Eternal_Inversionist.allAttack(0,100)