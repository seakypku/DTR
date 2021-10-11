import pyautogui
pyautogui.FAILSAFE = False
x, y  = pyautogui.size()
pyautogui.screenshot('first_screenshot.png')
pos = pyautogui.locateOnScreen('shoe.jpeg',confidence=0.9)
pos_c = pyautogui.center(pos)
x = pos_c.x/2
y = pos_c.y/2
print(x)
print(y)
pyautogui.moveTo(x,y,0.5,pyautogui.easeInQuad)
pyautogui.click(x,y,button='left')

pyautogui.screenshot('Part.png',region=(x - 235/2,y-74/2,235,74))
for pos in pyautogui.locateAllOnScreen('shoe.jpeg',confidence=0.9):
    print(pos)


