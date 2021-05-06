
class InitializePuzzle:
    def __init__(self, row, columns, values,start_state):
        self.rows = row
        self.cols = columns
        self.value_range = values
        self.start_state = start_state

    @property
    def grids(self):
        """Create a skeleton of the grid and fill it if ther is a start state if no start state keep default values  """

        self.grid = []
        append_counter = 0

        if(self.rows == 0 and self.cols == 0):  
            self.grid.append([])
            self.grid[0].append(self.value_range)

        elif self.rows >= 1 and self.cols == 0:  
            for i in range(0, self.rows):
                self.grid.append([])
            for j in self.grid:
                j.append(self.value_range)

        elif self.rows == 0 and self.cols >= 1:  
            self.grid.append([])
            for i in range(0, self.cols):
                self.grid[0].append(self.value_range)

        elif self.rows == 1 and self.cols >= 1:  
            row = 0
            col = 0
            for i in range(0, self.rows * self.cols):
                self.grid.append([])
            for item in self.grid:
                while col < self.cols:
                    item.append(self.value_range)
                    col += 1
                row += 1
                if row == self.rows:
                    row = 0
                    col = 0
                    continue

        elif self.rows >= 1 and self.cols == 1: 
            col = 0
            row = 0
            for i in range(0, self.rows):
                self.grid.append([])
            for item in self.grid:
                while not row == self.rows * self.cols:
                    item.append(self.value_range)
                    col += 1
                    if col == self.cols * self.rows:
                        row += 1
                        col = 0
                        break
        else:
            for i in range(0, self.rows * self.cols):  
                self.grid.append([])
            row = 0
            col = 0
            for i in self.grid:  # works for >= 2 and >1
                while(col < self.cols * self.rows):
                    self.grid[row].append(self.value_range)
                    col += 1
                row += 1
                col = 0

        if bool(self.start_state) == False: 
            pass
        else:  
            try:
                for key, value in self.start_state.items():
                    if bool(value) == False:
                        self.grid[key[0]][key[1]
                                          ] = self.value_range
                        continue
                    if type(value) is list:
                        self.grid[key[0]][key[1]] = value[0]
                    if type(value) == int:
                        self.grid[key[0]][key[1]] = value
            except IndexError:
                print(
                    "Start state had an invalid pair attempting to solve puzzle with current values")

        
        return self.grid
