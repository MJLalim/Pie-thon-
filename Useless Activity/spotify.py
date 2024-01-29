"""
Author: Michael John Andagan Lalim
Date created: February ‎6, ‎2023, ‏‎9:03:06 AM
Purpose: Listening to some tunes :)

WARNING: THIS ONLY WORKS ON MY LAPTOP: TO CONFIG USE [ print(pag.position()) ]
"""
#opens spotify and plays a random playlist
import pyautogui as pag, time as t,random as r
t.sleep(2)
#close vs code: 2877,33
pag.moveTo(2877,33);pag.leftClick();t.sleep(2)
#spotify taskbar: 1862,1877
pag.moveTo(1934,1876);pag.leftClick();t.sleep(4)
#spotify search bar: 238,305
pag.moveTo(238,305);pag.leftClick();t.sleep(2)
#spotify search bar: 881,181
pag.moveTo(881,181);pag.leftClick();t.sleep(2)
#list of playlist
playList = ['Siesta','Tuengo Rapido','Bando Rapido','Cocaine','Jimusic','Sando Bando','lover boy?','Toxicology']
#list of podcast
podcastList = ['Philosophize This!','TED Talks Daily','The Joe Rogan Experience']
#randomly chooses either music or podcast
x = r.randint(0,1)
if x == 1:
    useList = playList
else:
    useList = podcastList
#play random
y = r.randint(0,len(useList))
#search 
pag.typewrite(useList[y]);t.sleep(1);pag.hotkey('enter');t.sleep(2);pag.moveTo(1330,763);pag.leftClick();t.sleep(2)
#volume to the max
pag.moveTo(2806,1875);pag.leftClick();t.sleep(1);pag.moveTo(2930,1653);pag.leftClick();t.sleep(2)
