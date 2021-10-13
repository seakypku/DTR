import pyautogui
import time
import random
import json
import pynput
pyautogui.FAILSAFE = False

CREATE_GAME = (1253,1336)
NM = (1291, 694)
born_to_red_path = '[["click", [777.35546875, 420.484375, "Button.right"], 3.096381902694702], ["click", [616.94921875, 562.94921875, "Button.left"], 9.266451835632324], ["click", [718.5625, 721.1796875, "Button.left"], 13.485430002212524], ["click", [394.9375, 733.375, "Button.left"], 15.139711856842041], ["click", [563.45703125, 598.796875, "Button.left"], 16.260904788970947], ["click", [727.2421875, 449.36328125, "Button.left"], 16.75231695175171], ["click", [1096.8984375, 187.05859375,"Button.left"], 17.798149824142456], ["press", ["Key.cmd"], 19.80386471748352], ["release", ["Key.cmd"], 20.00657892227173], ["press", ["Key.shift"], 22.56843376159668], ["click", [1097.65625, 187.05859375, "Button.left"], 22.78569483757019], ["click", [1097.65625, 187.05859375, "Button.left"], 22.98658585548401], ["click", [1097.65625, 187.05859375, "Button.left"], 23.18855094909668], ["click", [1097.65625, 187.05859375, "Button.left"], 23.39003086090088], ["click", [1097.65625,187.05859375, "Button.left"], 23.624409675598145], ["click", [1097.65625, 187.05859375, "Button.left"], 23.84235382080078], ["release", ["Key.shift"], 24.088761806488037]]'

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

def play_json(jstr):
    mouse = pynput.mouse.Controller()
    keyboard = pynput.keyboard.Controller()
    # 鼠标的两个按钮
    buttons = {
        "Button.left": pynput.mouse.Button.left,
        "Button.right": pynput.mouse.Button.right
    }
    # 开始后已经经过的时间
    sTime = 0

    command_list = json.loads(jstr)

    for command in command_list:
        print(command[0])
        print(command[1])
        #print(command[1][2])
        print(command[2])
        if command[0] == "click":
            # 将鼠标移动到记录中的位置
            mouse.position = (command[1][0], command[1][1])
            # 等待一下
            time.sleep(0.1)
            # 点击
            mouse.click(buttons[command[1][2]])
        # 如果是按键按下
        elif command[0] == "press":
            # 如果是特殊按键,会记录成Key.xxx,这里判断是不是特殊按键
            if command[1][0][:3] == "Key":
                # 按下按键
                keyboard.press(eval(command[1][0], {}, {
                    "Key": pynput.keyboard.Key
                }))
            else:
                # 如果是普通按键,直接按下
                if "<255>" == command[1][0]:
                    continue
                print(command[1][0])
                print(command[1][0].split("'")[1])
                keyboard.press(command[1][0].split("'")[1])
        # 如果是按键释放
        elif command[0] == "release":

            # 如果是特殊按键
            if command[1][0][:3] == "Key":
                # 按下按键
                keyboard.release(eval(command[1][0], {}, {
                    "Key": pynput.keyboard.Key
                }))
            else:
                # 普通按键直接按下
                if "<255>" == command[1][0]:
                    continue
                print(command[1][0])
                print(command[1][0].split("'")[1])
                keyboard.release(command[1][0].split("'")[1])
        # command[2]代表此操作距离开始操作所经过的时间,用它减去已经经过的时间就是距离下一次操作的时间
        time.sleep(command[2] - sTime)
        # 更新时间
        sTime = command[2]

# 判断当前装态

if __name__=="__main__":
#    while True:
#        time.sleep(3)
#        create_game(2)
#        born_to_red()
#        red_to_pindle()
#        exit_game()
    play_json(born_to_red_path)

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


