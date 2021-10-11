import pyautogui
import time
import random
pyautogui.FAILSAFE = False

CREATE_GAME = (1253,1336)
NM = (1291, 694)



def ran(i,j):
    return random.uniform(i,j)
def create_game( mode ):
    if mode == 2:
        pyautogui.moveTo(CREATE_GAME[0],CREATE_GAME[1],0.5)
        pyautogui.click(CREATE_GAME[0],CREATE_GAME[1],button='left')
        pyautogui.moveTo(NM[0],NM[1],1)
        pyautogui.click(NM[0],NM[1],button='left')
        time.sleep(ran(10,13))
def go_to_pos(pos):
    pyautogui.leftClick(pos[0],pos[1])
    pyautogui.mouseUp()
    mouse_to_center()
    time.sleep(ran(2.5,3))
    #pyautogui.moveTo(pos[0],pos[1])
def mouse_to_pos(pos):
    #mouse_to_center()
    pyautogui.moveTo(pos[0],pos[1])
    time.sleep(3)
    
def find_symbol(fn):
    pos = pyautogui.locateOnScreen(fn,confidence=0.8)
    pos_c = pyautogui.center(pos)
    pyautogui.screenshot('Part_Red.png',region=(pos_c.x,pos_c.y,235,235))
    return (pos_c.x,pos_c.y)
def mouse_to_center():
    x,y = pyautogui.size()
    pyautogui.moveTo(x/2,y/2)
def cast_spell(type,pos):
    if type == 'loot':
        pyautogui.moveTo(pos)
        pyautogui.press('f3')
        pyautogui.rightClick()
        time.sleep(ran(0.5,0.9))
    if type == 'tp':
        pyautogui.moveTo(pos)
        pyautogui.press('f2')
        pyautogui.rightClick()
        time.sleep(ran(0.3,0.7))
    if type == 'blz':
        pyautogui.moveTo(pos)
        pyautogui.press('f1')
        pyautogui.rightClick()
        time.sleep(ran(1,2))
def born_to_red():
    step1 = (902,1053)
    step2 = (892,1058)
    step3 = (949,1247)
    step4 = (1199,1204)
    step5 = (731,952)
    #step6 = (833,882)
    go_to_pos(step1)
    go_to_pos(step2)
    go_to_pos(step3)
    go_to_pos(step4)
    go_to_pos(step5)
   # go_to_pos(step6)
    step7 = find_symbol('red.png')
    cast_spell('loot',step7)
def red_to_pindle():
    step1 = (1942,197)
    step2 = (2109,194)
    step3 = (1950,177)
    step4 = (1746,567)
    step5 = (1853,487)
    step6 = (1969,369)
    cast_spell('tp',step1)
    cast_spell('tp',step2)
    cast_spell('tp',step3)
    pyautogui.press('alt')
    cast_spell('blz',step4)
    cast_spell('blz',step5)
    cast_spell('blz',step6)
    cast_spell('blz',step5)
 
def exit_game():
    pyautogui.press('esc')
    time.sleep(ran(0.3,0.6))
    pyautogui.leftClick(1279,633)
    time.sleep(9,15)
    
while True:
    time.sleep(3)
    create_game(2)
    born_to_red()
    red_to_pindle()
    exit_game()

#x, y  = pyautogui.size()
#pyautogui.screenshot('first_screenshot.png')
#pos = pyautogui.locateOnScreen('test.png',confidence=0.8)
#pos_c = pyautogui.center(pos)
#x = pos_c.x
#y = pos_c.y
#print(x)
#print(y)
#
#pyautogui.click(x,y,button='left')

"""
pyautogui.screenshot('Part.png',region=(x - 235/2,y-74/2,235,74))
for pos in pyautogui.locateAllOnScreen('shoe.jpeg',confidence=0.9):
    print(pos)
"""

