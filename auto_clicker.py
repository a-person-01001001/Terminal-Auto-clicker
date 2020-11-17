import pyautogui

width, height = pyautogui.size()
pauselength = float(input("PAUSE: "))
while True:
    pyautogui.FAILSAFE = True
    pyautogui.click(pyautogui.position())
    pyautogui.PAUSE = pauselength
