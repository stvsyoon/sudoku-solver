import numpy as np

# initialize grid, will implement sudoku generator later
grid = [[5,3,0,0,7,0,0,0,0],
        [6,0,0,1,9,5,0,0,0],
        [0,9,8,0,0,0,0,6,0],
        [8,0,0,0,6,0,0,0,3],
        [4,0,0,8,0,3,0,0,1],
        [7,0,0,0,2,0,0,0,6],
        [0,6,0,0,0,0,2,8,0],
        [0,0,0,4,1,9,0,0,5],
        [0,0,0,0,8,0,0,7,9]]


def solve():
    return


def check_valid(x,y,n):
    '''(int, int, int) -> bool
    This function takes a coordinate of the grid (x,y) and a potential number n from 0-9
    and returns T/F whether that number is valid in that spot within the rules of Sudoku.
    It will return False if it finds n in the respective row, col, and 3x3 square of (x,y)
    and True if it is doesn't.
    '''

    # check column if valid
    for c in range(9):
        if grid[c][x] == n:
            return False
    
    # check row if valid
    for r in range(9):
        if grid[y][r] == n:
            return False
    
    # check 3x3 square if valid
    # to get the indices of the square, you must use integer division
    x_i = x//3 * 3
    y_i = y//3 * 3
    for s in range(x_i, x_i + 3):
        for l in range(y_i, y_i + 3):
            if grid[s][l] == n:
                return False
    
    return True


if __name__ == '__main__':
    print(np.matrix(grid))
