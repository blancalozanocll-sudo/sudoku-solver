
class Sudoku:

    def __init__(self, puzzle):
        self.puzzle = puzzle

    
    def find_empty(self):

        # this method finds the first row,column (cell) that is not filled yet (represented with 0)

        for i in range(9):
            for j in range(9):
                if self.puzzle[i][j] == 0:
                    return i,j
                
        return None # if we reach this point, there are no empty cells so we return None
       

    def valid_option(self, row, column, guess):

        # because we are using backtracking abd branch&bound, we need to verify that a guess to place a number in a cell is valid
        # what this method does is return a True if the number we placed in a cells belongs there and a False otherwise

        # checking rows:
        if guess in self.puzzle[row]: # remember, PUZZLE is a LIST that contains the ROWS, so we don't need to do a for loop in this case
            return False
        
        # checking columns:
        col_values = []
        for i in range(9):
            col_values.append(self.puzzle[i][column])

        if guess in col_values:
            return False
        
        # checking sub-cells:
        row_start = (row //3) * 3  # we do this to know if index is in te first set of 3 rows, second set or last set
        col_start = (column //3) * 3  # same for the columns

        # and now that we have both the starting indexes, we ittereate through the whole sub-cell to see if our guess is in the 3x3 matrix
        for i in range(row_start, row_start + 3):
            for j in range(col_start, col_start + 3):
                if self.puzzle[i][j] == guess:
                    return False
                
        return True # if we reach this point of the method, guess is NOT in our puzzle so we return TRUE
    
    def find_best_cell(self):
        min_options = 10
        best_cell = None

        for i in range(9):
            for j in range(9):
                if self.puzzle[i][j] == 0:
                    options = 0
                    for guess in range(1,10):
                        if self.valid_option(i,j,guess):
                            options += 1
                    if options < min_options:
                        min_options = options
                        best_cell = (i,j)
                        if min_options == 1:
                            return best_cell
        return best_cell








