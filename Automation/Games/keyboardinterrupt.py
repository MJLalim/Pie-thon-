import time
import sys
import os
import threading
import keyboard
import BackEnd

def quitScript():
    print("QUITTING...")
    time.sleep(0.2) #wait for the thread to die
    os.system('stty sane')
    sys.exit()

def keyBoardInterruptor():
    try:
        while True:
            time.sleep(5)
            BackEnd.Eternal_Inversionist.allAttack()
            print("tick")
            time.sleep(0.5)
            if keyboard.is_pressed('q'):  # if key 'q' is pressed 
                print('You Pressed A Key!')
                quitScript()
    except KeyboardInterrupt:
        quitScript()

keyBoardInterruptor()

