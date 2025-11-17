
def load_puzzle(filepath):

    puzzle = []

    with open(filepath, 'r') as file:
        for line in file:
            line2 = line.strip().split()
            row = [int(char) for char in line2]
            puzzle.append(row)

    return puzzle


def print_puzzle(puzzle):

    message="---------------------\n"

    for i in range(9):
        for j in range(9):
            if j % 3 == 0:
                message += "| " # vertical subgrid separator

            if puzzle[i][j] == 0:
                message += "0 "
            else:
                message += str(puzzle[i][j]) + " "

        message += "\n"

        if (i+ 1) % 3 == 0:
            message += "---------------------\n"

    return message

