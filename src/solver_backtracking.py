
def solve_backtracking(sudoku):

    # we guess numbers from 1-9 and:
    #  - solve if  it's a good guess
    #  - go back if it's a bad guess (backtracking algorithm)

    cell = sudoku.find_empty() # this finds the first empty cell

    if cell is None:
        return True # if there are no empty spaces, the sudoku is completed
    
    row, column = cell

    for guess in range(1,10): # 1-9
        if sudoku.valid_option(row, column, guess): # if a guess is a valid option, 
            sudoku.puzzle[row][column] = guess # then we place the guess on the puzzle

            if solve_backtracking(sudoku):  # we recursively solve the sudoku
                return True
                
            sudoku.puzzle[row][column] = 0 # if the guess is NOT a valid option, we revert and set a 0 as value
        
    return False # if none of the guesses are right, then sudoku is unsolvable