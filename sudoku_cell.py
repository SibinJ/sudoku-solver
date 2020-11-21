class Cell:
    value = 0
    isValueSet = False
    possibleValues = []
    
    def __init__(self):
        self.isValueSet = False
        self.possibleValues = []
            
    def setValue(self, value):
        self.value = value        
        if value == 0:
            self.isValueSet = False
        else:    
            self.isValueSet = True
            
    def resetValue(self):
        self.value = 0
        self.isValueSet = False
    
    # Append a possible value to the list    
    def addPossibleValue(self, value):
        self.possibleValues.append(value)
        
    # Remove a value which is no longer possible
    def delPossibleValue(self, value):
        self.possibleValues.remove(value)
        
    # Empty the entire list when the correct number is found
    def purgePossibleValues(self):
        self.possibleValues.clear()