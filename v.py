import pyautogui as pg
import time as t
i=0
while(i<=100):
    t.sleep(2)
    pg.typewrite("heloo ")
    pg.press("enter")
    i=i+1