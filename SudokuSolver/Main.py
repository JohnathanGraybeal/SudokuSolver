from Solver import *
from FileParser import *
from InitializePuzzle import *


if __name__ == "__main__":
    print("Enter of the absolute or relative path of the puzzle file you want to use")
    user_file = input()
    parser = FileParser(fr"{user_file}")
    parser.extract_data(fr"{user_file}")
    parser.display_attributes()
    puzzle = InitializePuzzle(parser.rows, parser.cols,
                              parser.value_range, parser.start_state)
    puzzle.grids

    solve = Solver(puzzle.grids, parser.rows, parser.cols, parser.value_range)
    solve.display_grid()
    if parser.rows == 0 and parser.cols == 0:
        solve.size_zero()
    elif parser.rows == 0 and parser.cols >= 1:
        solve.zero_by_n()
    else:
        solve.check_cell(puzzle.grids)
    solve.display_grid()
