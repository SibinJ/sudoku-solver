import pyautogui
import time
from sudoku_grid import Grid
from screenCoordinates import *

path = './resources/img/'
ext = '.png'

def setInitialValuesInGrid(grid):
    numSetValues = 0
    for i in range(1, 10):
        img = path + str(i) + ext
        for pos in pyautogui.locateAllOnScreen(img, region=(left, top, width, height)):
            row = int((pos.top - top) / cellHeight)
            col = int((pos.left - left) / cellWidth)
            grid[row][col].setValue(i)
            numSetValues = numSetValues + 1
    if numSetValues == 0:
        return False
    return True