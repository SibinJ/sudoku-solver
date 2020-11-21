from sudoku_cell import Cell

rows, cols = (9, 9)

class Grid:
    grid = [[]]
    
    def __init__(self):
        self.grid = [[Cell() for i in range(rows)] for j in range(cols)]
        
    def printGrid(self):
        print("Grid")
        for row in self.grid:
            for cell in row:
                print(cell.value, end=' ')
            print()
            
    def printNumPossibleValues(self):
        print("Num possible values")
        for row in self.grid:
            for cell in row:
                print(len(cell.possibleValues), end=' ')
            print('\n')
            
    def printPossibleValues(self):
        print("Num possible values")
        for row in self.grid:
            for cell in row:
                print(cell.possibleValues, end=' ')
            print('\n')
            
    def removeFromRowPossible(self, row, value):
        for cell in self.grid[row]:
            try:
                cell.possibleValues.remove(value)
            except:
                pass
        
    def removeFromColPossible(self, col, value):
        for row in self.grid:
            try:
                row[col].possibleValues.remove(value)
            except:
                pass
        
    def removeFromBoxPossible(self, row, col, value):
        startRow = int((row / 3)) * 3
        startCol = int((col / 3)) * 3
        for i in range(startRow, startRow + 3):
            for j in range(startCol, startCol + 3):
                try:
                    self.grid[i][j].possibleValues.remove(value)
                except:
                    pass
            
    def removeFromPossibleValues(self, row, col, value):
        self.removeFromRowPossible(row, value)
        self.removeFromColPossible(col, value)
        self.removeFromBoxPossible(row, col, value)
        
    # Set the values to cells which have only one possible value
    def setSureValues(self):
        numSetValues = 0
        for row in self.grid:
            for cell in row:
                if cell.isValueSet == False and len(cell.possibleValues) == 1:
                    numSetValues = numSetValues + 1
                    cell.setValue(cell.possibleValues[0])
                    self.removeFromPossibleValues(self.grid.index(row), row.index(cell), cell.value)
                    cell.possibleValues.clear()
        return numSetValues
                    
    # Check if the value is set in any cell in the row
    def isPresentInRow(self, row, value):
        for cell in self.grid[row]:
            if cell.isValueSet == True and cell.value == value:
                return True
        return False
        
    # Check if the value is present in any cell in the column
    def isPresentInColumn(self, col, value):
        for row in self.grid:
            if row[col].isValueSet == True and row[col].value == value:
                return True
        return False
    
    # Check if the value is present in any cell in the box
    def isPresentInBox(self, row, col, value):
        startRow = int((row / 3)) * 3
        startCol = int((col / 3)) * 3
        for i in range(startRow, startRow + 3):
            for j in range(startCol, startCol + 3):
                if self.grid[i][j].isValueSet == True and self.grid[i][j].value == value:
                    return True 
        return False
                    
    # Check if the value can be placed in this cell
    def isPossibleValue(self, row, col, value):
        if self.isPresentInRow(row, value) == False and self.isPresentInColumn(col, value) == False and self.isPresentInBox(row, col, value) == False:
            return True
        else:
            return False
        
    # Find all the possible values that can be assigned to this cell
    def findPossibleValuesForCell(self, row, col):
        cell = self.grid[row][col]
        if cell.isValueSet == False:
            # Check all values in range
            for i in range(1, rows + 1):
                if self.isPossibleValue(row, col, i):
                    # Append the possible value
                    cell.possibleValues.append(i)
        
    # Find all possible values for all cells in the grid
    def findPossibleValuesForGrid(self):
        for row in self.grid:
            for cell in row:
                self.findPossibleValuesForCell(self.grid.index(row), row.index(cell))
                
    # Delete all possible values for all cells in grid
    def purgeAllPossibleValues(self):
        for row in self.grid:
            for cell in row:
                cell.purgePossibleValues()
                
    # Checks if the grid is solved. This is true when values of all cells are set
    def isSolved(self):
        for row in self.grid:
            for cell in row:
                if cell.isValueSet == False:
                    return False
        return True
        
    # Tries each possible value that can be assigned to each cell
    def checkAllPossibleValues(self):
        if self.isSolved():
            # All cells are set. Nothing else to check
            return True
        for row in self.grid:
            for cell in row:
                if cell.isValueSet == False:
                    for value in cell.possibleValues:
                        if self.isPossibleValue(self.grid.index(row), row.index(cell), value):
                            cell.setValue(value)
                            # Now check for all other cells
                            if self.checkAllPossibleValues() == True:
                                # All cells were set correctly. Nothing else to check
                                return True
                    # A value could not be set in this cell. This is because a wrong value was set in a previous cell
                    # Hence reset this cell and check with a different value for previous cell
                    cell.resetValue()
                    return False
                
    def solve(self):
        self.findPossibleValuesForGrid()
        while self.isSolved() == False:
            #self.printPossibleValues()
            numSetValues = self.setSureValues()
            #self.printGrid()
            #self.purgeAllPossibleValues() # instead of purging all values, remove from possible values of cells in row, column, box
            
            # If no values were set in the current iteration, that means we don't have any more sure values left
            # So now resort to backtracking with the remaining cells and their possible values
            if numSetValues == 0:
                #self.findPossibleValuesForGrid()
                # Backtrack to solve for rest
                self.checkAllPossibleValues()