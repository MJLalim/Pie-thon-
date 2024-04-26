import pyautogui as pag
import time as t

#*********THIS BLOCK IS FOR IN-BETWEEN SKILLS COOLDOWN***************#
#Theoritically takes 3 seconds
def coolDown():
        for i in range(3):
                pag.press('t'); pag.press('1'); pag.press('1'); t.sleep(1)
def archFiendCD():
        for i in range(2):
                pag.press('t'); pag.press('1'); pag.press('1'); t.sleep(1)
#*********THIS BLOCK IS FOR IN-BETWEEN SKILLS COOLDOWN***************#

#**********************THIS BLOCK IS FOR CLASSES*************************#
class Pirate: 
        def basicAttack():
                #1st skill
                pag.press('t'); pag.press('2')
                
                #cooldown
                coolDown()
                
                #2nd skill
                pag.press('t'); pag.press('4')
                
        def allSkill():
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

class ArchFiend:
        def basicAttack():
                #1st skill
                pag.press('t'); pag.press('2')   
                #cooldown
                archFiendCD()
                #2nd skill
                pag.press('t'); pag.press('4')
                
        def allSkills():
                #1st skill
                pag.press('t'); pag.press('2')
                
                #cooldown
                archFiendCD()
                
                #2nd skill
                pag.press('t');pag.press('3')
                #cooldown
                archFiendCD()

                #3rd skill
                pag.press('t'); pag.press('4')
                #cooldown
                archFiendCD()
                
                #4th skill
                pag.press('t');pag.press('5')
                
                #cooldown
                archFiendCD()

            
class Eternal_Inversionist:
        def basicAttack():
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
                

        def allAttack():
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
                 
class Mage:
        def basicAttack():
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

class LightMage:      
        #these only work for light mages   
        def basic_Combo():
                while (counter < untilThisNum ):
                pag.press('t');pag.press('2')#auto attack: skill 
                coolDown()#cooldown
                
                pag.press('t');pag.press('3')#auto attack: skill 
                coolDown()#cooldown
                
        #attack and heal      
        def basic_Attack_N_Heal():
                pag.press('t');pag.press('2')#auto attack: skill 
                coolDown()#cooldown
                
                pag.press('t');pag.press('3')#auto attack: skill 
                coolDown()#cooldown
                
                pag.press('t');pag.press('4')#auto attack: skill 
                coolDown()#cooldown

        #all skills
        def all_Skills():
                pag.press('t');pag.press('2')#auto attack: skill 
                coolDown()#cooldown
                        
                pag.press('t');pag.press('3')#auto attack: skill 
                coolDown()#cooldown
                        
                pag.press('t');pag.press('4')#auto attack: skill 
                coolDown()#cooldown
                        
                pag.press('t');pag.press('5')#auto attack: skill 
                coolDown()#cooldown
                