import time, keyboard,pyautogui
keyboardfunctions=["esc", "tab", "caps lock",
"shift", "ctrl", "alt",
"spacebar", "enter", "backspace", "delete", "up", "down", "left", "right",
"a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
"f1", "f2", "f3", "f4", "f5", "f6", "f7", "f8", "f9", "f10", "f11", "f12"]


buttonlist=[]
condition=True
while condition:
    try:
        delay=float(input("Add timer for interval"))
        condition=False
    except ValueError:
        print("You need to add correct Value not string either symbol")
        continue

loop=True
while loop:
    chooseside=input("Choose side for buttonclick").lower()
 
    if chooseside in ['left','right']:
        loop=False

    else:
        print("You need to add option left or right")
        continue

loop2=True
while loop2:
    for _ in range(2):
        buttonkey=input("Choose key button").lower()
        buttonlist.append(buttonkey)

    if all(button in keyboardfunctions for button in buttonlist):
        loop2 = False

    else:
        loop2=True
    
keyboard.wait(buttonlist[0])
if keyboard.is_pressed(buttonlist[0]):
    loop3=True
    while loop3:
        pyautogui.click(interval=delay,button=chooseside,clicks=100)

        if keyboard.is_pressed(buttonlist[1]):
            print("Loop out")
            break