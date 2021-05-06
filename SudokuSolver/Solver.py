
class Solver:
    def __init__(self, grid, rows, cols, value_range):
        self.grids = grid
        self.rows = rows
        self.cols = cols
        self.value_range = value_range
        self.step = 0

    def size_zero(self):
        """If 0x0 auto solve it since it is an arbitrary puzzle """
        self.grids[0][0] = 1

    def zero_by_n(self):
        """If 0xn auto solve since it's an arbitrary puzzle """
        for i in range(self.cols):
            self.grids[0][i] = i + 1

   


    def validate_num(self, grid, row, col, num):
        """Validates that a given number is a valid choice for the overall puzzle """
        try:
            for i in range(len(grid)):
                self.step += 1
                print(
                    f"Step {self.step} attempting to select and validate a number in row {i}")
                if grid[row][i] == num:
                    self.step += 1
                    print(f"Step {self.step} found a bad value at {row},{i}")
                    return False
            # check col
            for i in range(len(grid[0])):
                self.step += 1
                print(
                    f"Step {self.step} attempting to select and validate a number in col {i}")
                if grid[i][col] == num:
                    self.step += 1
                    print(f"Step {self.step} found a bad value at {row},{i}")
                    return False
            # get top-left corner
            top_left_row_subgrid = row - row % self.rows
            top_left_col_subgrid = col - col % self.cols
            # check grid
            for i in range(top_left_row_subgrid, top_left_row_subgrid + self.rows):
                self.step += 1
                print(f"Step {self.step} checking row {i}")
                for j in range(top_left_col_subgrid, top_left_col_subgrid+self.cols):
                    self.step += 1
                    print(f"Step {self.step} checking column {j}")
                    if grid[i][j] == num:
                        self.step += 1
                        print(f"Step {self.step} found a bad value at {i},{j}")
                        return False
            # return True if none of the cases above returns False

            print(f"Number validated")
            return True
        except IndexError:
            print("Attempted to solve. Puzzle is being considered unsolvable")
    def check_cell(self, grid):
        """Goes through each row column value checks if a value is a default 
            then in the range of valid values validate the number it is attempting to place otherwise if a valid number
            isn't found backtrack when all rows are exhaused does a final validation for all numbers  """
        try:
            val = [x for x in self.value_range]
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    self.step += 1
                    print(
                        f"Step {self.step} searching cell at  {i},{j} for default value")
                    if grid[i][j] == self.value_range:
                        self.step += 1
                        print(
                            f"Step {self.step} found default value in grid at {i},{j}")
                        for num in range(val[0], val[1] + 1):  # range of valid numbers
                            self.step += 1
                            print(
                                f"Step {self.step} looking in {self.value_range} for appropiate number")
                            if self.validate_num(grid, i, j, num):
                                self.step += 1
                                print(
                                    f"Step {self.step} found valid number trying grid {i},{j} replacing {grid[i][j]} with {num}")
                                grid[i][j] = num
                                result = self.check_cell(grid)
                                if result == True:
                                    self.step += 1
                                    print(
                                        f"Step {self.step} found {num} to be a valid entry at {i}, {j}")
                                    return True  # valid number found for first empty cell
                                else:
                                    self.step += 1
                                    print(
                                        f"Step {self.step} haven't found a valid value for grid {i},{j} temporarily setting {grid[i][j]} to {self.value_range}")
                                    grid[i][j] = self.value_range
                                    print(
                                        f"couldn't find a valid number attempting to backtrack")
                                    
                        print(
                            f"no numbers in a valid range found ")
                        return False
            print(f"exhausted last row")
            self.grids = grid
            return True
        except IndexError:
            print("Attempted to solve. Puzzle is being considered unsolvable")
    

    def display_grid(self):
        """Display current state of the puzzle """
        print("-"*56)
        for grid in self.grids:
            print(grid)
