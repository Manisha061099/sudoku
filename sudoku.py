
grid = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

def print_grid(grid):
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("-"*21) 
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print("|", end=" ")
            print(grid[i][j], end=" ")
        print()


def is_valid(board, row, col, num):
    
    if num in board[row]:
        return False
    
    for i in range(9):
        if board[i][col] == num:
            return False
    
    start_row = (row // 3) * 3
    start_col = (col // 3) * 3
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False
    return True


def find_empty(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i, j
    return None


def solve(board):
    empty = find_empty(board)
    if not empty:
        return True  
    
    row, col = empty
    
    for num in range(1, 10):
        if is_valid(board, row, col, num):
            board[row][col] = num
            if solve(board):
                return True
            board[row][col] = 0  
    
    return False 


def play_sudoku():
    print("Welcome to Sudoku!")
    while True:
        print_grid(grid)
        row = int(input("Enter row (0-8): "))
        col = int(input("Enter column (0-8): "))
        num = int(input("Enter number (1-9): "))
        
        if is_valid(grid, row, col, num):
            grid[row][col] = num
        else:
            print("Invalid move, try again.")
        
        
        if all(grid[i][j] != 0 for i in range(9) for j in range(9)):
            print("Congratulations, you've solved the Sudoku!")
            break


def solve_and_print_solution():
    print("Attempting to solve the Sudoku...")
    if solve(grid):
        print_grid(grid)
    else:
        print("No solution found.")


if __name__ == "__main__":
    
    play_sudoku()
  
