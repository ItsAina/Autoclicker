import pyautogui
import keyboard

delay=float(input("What delay you wish to have\n"))
howmanyclicks=int(input("How many clicks you wish to proceed\n"))
whatbutton=str(input("What button you wish to start with?\n"))
Endbutton=str(input("You need to add button for endbutton not repeaten as whatbutton\n"))
Whatsideofclick=str(input("Do you wish to click on left or right?\n")).upper()


while True:
    if keyboard.is_pressed(whatbutton) and Whatsideofclick=="LEFT":
        pyautogui.click(button='left')
        pyautogui.click(clicks=howmanyclicks, interval=delay)
        pyautogui.click()
        if keyboard.is_pressed(Endbutton):
            print("Loop has been terminated")
            break

    elif keyboard.is_pressed(whatbutton) and Whatsideofclick=="RIGHT":
        pyautogui.click(button='right')
        pyautogui.click(clicks=howmanyclicks, interval=delay)
        pyautogui.click()
        if keyboard.is_pressed(Endbutton):
            print("Loop has been terminated")
            break


    

