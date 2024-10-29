import pyautogui as pg
import random as rd
import time

while True:
    x = rd.randint(500, 700)
    y = rd.randint(100, 1000)
    pg.moveTo(x, y, 0.5)
    time.sleep(rd.random() *2)