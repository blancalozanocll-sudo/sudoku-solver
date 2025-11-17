
def solve_branchbound(sudoku):
    
    # we go for the space with fewest possible guesses
    # we 'remove' a path if we find that it's not a good path to follow

    cell = sudoku.find_best_cell()

    if cell is None:
        return True
    
    row, column = cell

    for guess in range(1,10):
        if sudoku.valid_option(row,column,guess):
            sudoku.puzzle[row][column] = guess

            if solve_branchbound(sudoku):
                return True
            
            sudoku.puzzle[row][column] = 0

    return False