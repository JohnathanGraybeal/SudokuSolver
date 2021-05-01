from InitializePuzzle import InitializePuzzle
import time
from Utility import clear
import os

# <summary>
# Manages the solving of the puzzle and displaying of the actual grids
# </summary>
# <param name="Geeksforgeeks"></param>


class Solver:
    def __init__(self, file):

        print("Invalid time delay defaulting it to 0")

        self.puzzle = InitializePuzzle(
            r"{}".format(file))
        self.grids = self.puzzle.grid
        self.display_grid()

        clear()
        self.sieve()

     # <summary>
    # starts solving process also handles solving for trivial puzzles
    # </summary>

    def sieve(self):
        if self.puzzle.parser.rows_per_box == 0 and self.puzzle.parser.cols_per_box == 0:  # trivial case
            self.grids[0][0] = 1
            self.display_grid()

        elif self.puzzle.parser.rows_per_box == 0 and self.puzzle.parser.cols_per_box >= 1:  # trivial case
            for value in self.grids:
                i = 1
                for v, x in enumerate(value):
                    self.grids[0][v] = i
                    i += 1
            self.display_grid()
        elif self.puzzle.parser.rows_per_box == 1 and self.puzzle.parser.cols_per_box == 1:
            self.grids[0][0] = 1
            self.grids[0][1] = 2
            self.display_grid()
        else:
            self.check_cell(self.grids)
            self.display_grid()

     # <summary>
    # validates a given number to make sure that it is legal
    # </summary>
    # <param name="grid"> grid that represents a puzzle</param>
    # <param name="row"> represents 0 based row of grid</param>
    # <param name="col"> represents 0 based column of grid</param>
    # <param name="num"> number to be selected</param>
    def validate_num(self, grid, row, col, num):
        # check row
        try:
            for i in range(len(grid)):
                print(
                    f" attempting to select and validate a number in row {i}")
                if grid[row][i] == num:
                    print(f" found a bad value at {row},{i}")
                    return False
            # check col
            for i in range(len(grid[0])):
                print(
                    f" attempting to select and validate a number in col {i}")
                if grid[i][col] == num:
                    print(f" found a bad value at {row},{i}")
                    return False
            # get top-left corner
            top_left_row_subgrid = row - row % self.puzzle.parser.rows_per_box
            top_left_col_subgrid = col - col % self.puzzle.parser.cols_per_box
            # check 3x3 square
            for i in range(top_left_row_subgrid, top_left_row_subgrid + self.puzzle.parser.rows_per_box):
                print(f" checking row {i}")
                for j in range(top_left_col_subgrid, top_left_col_subgrid+self.puzzle.parser.cols_per_box):
                    print(f" checking column {j}")
                    if grid[i][j] == num:
                        print(f" found a bad value at {i},{j}")
                        return False
            # return True if none of the cases above returns False
            print(f" Number validated")
            return True
        except IndexError:
            print("Attempted to solve. Puzzle is being considered unsolvable")
    # <summary>
    # does the actual solving loops and exhaustes each row,col and recursively calles the validation function
    # </summary>
    # <param name="grid"> grid that represents a puzzle</param>

    def check_cell(self, grid):
        try:
            val = [x for x in self.puzzle.parser.value_range]
            for i in range(len(grid)):
                print(
                    f" searching cell at row {i} for default value")
                for j in range(len(grid[0])):
                    print(
                        f" searching cell at  {i},{j} for default value")
                    if grid[i][j] == self.puzzle.parser.value_range:
                        print(
                            f" found default value in grid at {i},{j}")
                        for num in range(val[0], val[1] + 1):  # range of valid numbers
                            print(
                                f" looking in value range for appropiate number")
                            if self.validate_num(grid, i, j, num):
                                print(
                                    f" found valid number trying grid {i},{j} replacing {grid[i][j]} with {num}")
                                grid[i][j] = num
                                result = self.check_cell(grid)
                                if result == True:
                                    print(
                                        f" found {num} to be a valid entry at {i}, {j}")
                                    return True  # valid number found for first empty cell
                                else:
                                    print(
                                        f"haven't found a valid value for grid {i},{j} temporarily setting {grid[i][j]} to {self.puzzle.parser.value_range}")
                                    grid[i][j] = self.puzzle.parser.value_range
                                    print(
                                        f"  couldn't find a valid number attempting to backtrack")
                        print(
                            f" no numbers in a valid range found ")
                        return False
            print(f" exhausted last row")
            return True
        except IndexError:
            print("Attempted to solve. Puzzle is being considered unsolvable")
    # <summary>
    # displays the current state of the sudoku grid
    # </summary>

    def display_grid(self):
        for grid in self.grids:
            print(grid)
