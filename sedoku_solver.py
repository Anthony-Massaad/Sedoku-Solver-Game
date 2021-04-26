import random
import copy


# Method to solve the puzzle
def solvePuzzle(board):
    """
    Precondition: Board of 9x9 with 3x3 each exist. 
                   -> So 1 list, with 9 sub lists each having 9 elements
    Will recursively loop until all 0s are coverred. 
    """
    getZeroPos = findAnEmptySlot(board)
    # Checking if there is no more 0's.
    # if getZero is None, the negate of that is True meaning no more Zeroes
    if not getZeroPos:
        return True
    # For loop to loop from 1-9 digits
    for i in range(1, 10):
        # Checking if the i'th value is valid using validNum method
        if validNum(getZeroPos[0], getZeroPos[1], board, i):
            board[getZeroPos[0]][getZeroPos[1]] = i
            if solvePuzzle(board):
                return True
            board[getZeroPos[0]][getZeroPos[1]] = 0
    return False

# Method to check if the val is a valid int for the board at that slot
def validNum(row, col, board, val):
    # Check Row from current (row,col)
    for j in range(9):
        if board[row][j] == val:
            return False
    # Check Col from current (row,col)
    for i in range(len(board)):
        if board[i][col] == val:
            return False
    # Check 3x3 Box from current (row,col)
    curr = getCols(col)  # Get a row
    inter = getRows(row)  # get a col
    # Loop through the rows for the 3x3 box
    for i in range(inter - 3, inter):
        # Loop through the columns for the 3x3 box
        for j in range(curr, curr + 3):
            if board[i][j] == val:
                return False
    return True

# Method to get the column to iterate from
def getCols(col):
    curr = 0
    if col % 3 == 0:
        curr = col
    elif (col - 2) % 3 == 0:
        curr = col - 2
    elif (col - 1) % 3 == 0:
        curr = col - 1
    return curr

# Method to get the row to iterate from
def getRows(row):
    inter = 0
    if 0 <= row <= 2:
        inter = 3
    elif 3 <= row <= 5:
        inter = 6
    elif 6 <= row <= 8:
        inter = 9
    return inter

# Find a zero in the board
def findAnEmptySlot(board):
    # Iterate from the row 0....8 (1-9)
    for i in range(len(board)):
        # Iterate from column 0....8 (1-9)
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)
    return None

# Print the board
def printBoard(board):
    counter = 0
    print("-------------------------")
    # For loop for every for all the rows
    for i in range(len(board)):
        print("|", end=" ")
        # For loop for each individual row
        for j in range(len(board[0])):
            counter += 1
            print(board[i][j], end=" ")
            # If for every third digit printed, print a |
            if counter % 3 == 0:
                print("|", end=" ")
            # If for every ninth digit printed, print a new line
            if counter % 9 == 0:
                print()
        # If for every 3x3 created in a row, print a new line and dashes to separate
        if counter % 27 == 0:
            print("-------------------------")

# Generate unique Board
def generate(board):
    getZeroes = findAnEmptySlot(board)
    if not getZeroes:
        printBoard(board)
        for i in range(9):
            for j in range(9):
                if random.randint(1, 4) > 2:
                    board[i][j] = 0
        return True
    rows, cols = getZeroes
    for i in range(9):
        i = random.randint(1, 9)
        if validNum(rows, cols, board, i):
            board[rows][cols] = i
            if generate(board):
                return True
            board[rows][cols] = 0
    return False


# sedoku temp board
if __name__ == "__main__":
    board = [[0 for i in range(9)] for j in range(9)]
    generate(board)

    """
    board = [
        [0, 0, 0, 0, 0, 0, 6, 8, 0],
        [0, 0, 0, 0, 7, 3, 0, 0, 9],
        [3, 0, 0, 0, 0, 0, 0, 4, 5],
        [4, 9, 0, 0, 0, 0, 0, 0, 0],
        [8, 0, 3, 0, 5, 0, 9, 0, 2],
        [0, 0, 0, 0, 0, 0, 0, 3, 6],
        [9, 6, 0, 0, 0, 0, 3, 0, 0],
        [7, 0, 0, 6, 8, 0, 0, 0, 0],
        [0, 0, 8, 0, 0, 0, 0, 0, 0],
    ]
    """
    print("**UNSOLVED**")
    printBoard(board)
    solvePuzzle(board)
    print("\n**SOLVED**")
    printBoard(board)
