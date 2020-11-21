import pyautogui
from screenCoordinates import *

def writeValuesToScreen(grid):
    for row in grid:
        for col in row:
            screenX = left + (row.index(col) * cellWidth) + int(cellWidth / 2)
            screenY = top + (grid.index(row) * cellHeight) + int(cellHeight / 2)
            # Click on each cell
            pyautogui.click(x=screenX, y=screenY)
            # Write the value
            pyautogui.write(str(grid[grid.index(row)][row.index(col)].value))