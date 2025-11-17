from utils import load_puzzle
from utils import print_puzzle
from sudoku import Sudoku
from solver_backtracking import solve_backtracking
from solver_branchbound import solve_branchbound
# from solver_branchbound import solve_branchbound


def main():

    valid_levels = {"easy", "medium", "hard", "expert"}

    level = input("\nWhat level do you want?\nOptions: Easy, Medium, Hard, Expert\n").strip().lower()

    if level not in valid_levels:
        print("Invalid level. Try again")
        return


    filepath = f"levels/{level}.txt"

    puzzle = load_puzzle(filepath)
    print(f"\nOriginal Sudoku ({level}):\n")
    print(print_puzzle(puzzle))

    sudoku = Sudoku(puzzle)

    if solve_backtracking(sudoku):
        print("\nSudoku solved (backtracking):\n")
        print(print_puzzle(sudoku.puzzle))
    else:
        print("There's no solution for this puzzle")

    sudoku2 = Sudoku(puzzle)

    if solve_branchbound(sudoku2):
        print("\nPuzzle solved (branch&bound):\n")
        print(print_puzzle(sudoku.puzzle))
    else:
        print("There's no solution for this puzzle")


if __name__ == "__main__":
    main()