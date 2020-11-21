import time
from sudoku_grid import Grid
from inputReader import setInitialValuesInGrid
from outputWriter import writeValuesToScreen

#current_milli_time = lambda: int(round(time.time() * 1000))

# Give time to minimize current window
time.sleep(3)

sudoku = Grid()

if setInitialValuesInGrid(sudoku.grid) == True:
    sudoku.solve()
    writeValuesToScreen(sudoku.grid)
else:
    print('No sudoku found')

del sudoku