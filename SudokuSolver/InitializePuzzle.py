
from FileParser import *
from Utility import clear

# <summary>
# Initializes puzzle by creating and filling grids and displaying info about grids
# </summary>


class InitializePuzzle:
    def __init__(self, file):
        self.parser = FileParser(file)
        self.display_attributes()
        self.create_grid()
        self.fill_grid()
        clear()
        print("Displaying Sudoku Puzzle")

    # <summary>
    # create grid rows and columns
    # </summary>
    def create_grid(self):
        print("Creating grid...")
        cols = self.parser.cols_per_box
        rows = self.parser.rows_per_box

        self.grid = []
        append_counter = 0

        if(self.parser.rows_per_box == 0 and self.parser.cols_per_box == 0):
            self.grid.append([])
            self.grid[0].append(self.parser.value_range)

        elif(self.parser.rows_per_box == 0 and self.parser.cols_per_box > 1):
            self.grid.append([])
            col_count = 0
            while col_count < cols:
                for i in self.grid:
                    i.append(self.parser.value_range)
                    col_count += 1
        elif(self.parser.rows_per_box == 1 and self.parser.cols_per_box == 1):
            self.grid.append([])
            col = 0
            for i in self.grid:

                while col < 2:
                    i.append(self.parser.value_range)
                    col += 1
                col = 0
        elif(self.parser.rows_per_box == 1 and self.parser.cols_per_box > 1):
            for i in range(1, self.parser.cols_per_box + 1):
                self.grid.append([])
            for i in self.grid:
                row = 0
                col = 0
                while col < self.parser.cols_per_box:
                    i.append(self.parser.value_range)
                    col += 1
        elif(self.parser.cols_per_box == 1 and self.parser.rows_per_box > 1):
            for i in range(self.parser.rows_per_box):
                self.grid.append([])
            for i in self.grid:
                row = 0
                col = 0
                while col < self.parser.cols_per_box * self.parser.rows_per_box:
                    i.append(self.parser.value_range)
                    col += 1

        else:
            for i in range(rows * cols):  # create row * col grid
                self.grid.append([])
            row = 0
            col = 0
            for i in self.grid:
                while(col < self.parser.cols_per_box * self.parser.rows_per_box):
                    self.grid[row].append(self.parser.value_range)
                    col += 1
                row += 1
                col = 0

     # <summary>
    # manage start state if a grid has one
    # </summary>
    # <param name="Geeksforgeeks"></param>

    def fill_grid(self):
        # unsolveable if puzzle not well formed so no point in filling grid
        print("Populating Grid...")
        try:

            if bool(self.parser.start_state) == False:  # check that there is a start state
                row = 0
                for i in self.grid:
                    col = 0
                    for j in i:
                        self.grid[row][col] = self.parser.value_range
                    col += 1
                row += 1
            else:
                try:
                    for key, value in self.parser.start_state.items():
                        if bool(value) == False:
                            self.grid[key[0]][key[1]
                                              ] = self.parser.value_range
                            continue
                        if type(value) is list:
                            self.grid[key[0]][key[1]] = value[0]
                        if type(value) == int:
                            self.grid[key[0]][key[1]] = value
                except IndexError:
                    print(
                        "Start state had an invalid pair attempting to solve puzzle with current values")
        except ValueError:
            print("do you want to try another one?")
            choice = input()
            if("y" or "Y" in choice):
                # open file dialog
                # create object with file
                pass
     # <summary>
    # Display info about the file
    # </summary>
    # <param name="Geeksforgeeks"></param>

    def display_attributes(self):
        print(f"File Name: {self.parser.filename}")
        print(f"Size: {self.parser.rows_per_box} x {self.parser.cols_per_box}")
        print(f"Well Formed: {self.parser.well_formed}")
        print(f"Solvable: {self.parser.solvable}")
        print(f"Unique Solution: {self.parser.unique_solution}")
        print(f"Pigeon Hole Decideable: {self.parser.pigeonhole}")
        print(f"Value Range: {self.parser.value_range}")
        print("-"*56)
