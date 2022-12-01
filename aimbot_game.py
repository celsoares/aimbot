#http://www.aimbooster.com/

import pyautogui as py

while True:
#-------------------------------------------------------------------------------------
    p1=py.locateOnScreen('a1.png', region=(550, 380, 800, 580), confidence=0.7)

    if p1: 
        click_pos=py.center(p1)
        #py.click(click_pos[0], click_pos[1])
        py.click(int(click_pos[0]), int(click_pos[1]))

#-------------------------------------------------------------------------------------

    p2=py.locateOnScreen('a1.png', region=(550, 380, 800, 580), confidence=0.7)

    if p2: 
        click_pos=py.center(p2)
        #py.click(click_pos[0], click_pos[1])
        py.click(int(click_pos[0]), int(click_pos[1]))
#-------------------------------------------------------------------------------------
  
    p3=py.locateOnScreen('a1.png', region=(550, 380, 800, 580), confidence=0.7)

    if p3: 
        click_pos=py.center(p3)
        #py.click(click_pos[0], click_pos[1])
        py.click(int(click_pos[0]), int(click_pos[1]))
#-------------------------------------------------------------------------------------

    p4=py.locateOnScreen('a1.png', region=(550, 380, 800, 580), confidence=0.7)

    if p4: 
        click_pos=py.center(p4)
        #py.click(click_pos[0], click_pos[1])
        py.click(int(click_pos[0]), int(click_pos[1]))
#-------------------------------------------------------------------------------------

    p5=py.locateOnScreen('a1.png', region=(550, 380, 800, 580), confidence=0.7)

    if p5: 
        click_pos=py.center(p5)
        #py.click(click_pos[0], click_pos[1])
        py.click(int(click_pos[0]), int(click_pos[1]))
