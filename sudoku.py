def printBoard(b):
    """Prints the grid
       Takes in the grid as a parameter
    """
    n = len(b[0])
    for i in range(n):
        if i%3 == 0 and i != 0:
            print("----------------------------------------") 
        for j in range(n):
            if j%3 == 0 and j != 0:
                print(" | ",end="")
            print(b[i][j], end="   ")
        print("\n")
def findEmptyCell(grid):
    """Checks whether there exists an empty cell in the grid. 
       Takes in the grid as a parameter and return a tuple of points or a cell.
    """
    for r in range(9):
        for c in range(9):
            if grid[r][c] == 0:
                return r,c
    return None,None
def isAValideCell(grid,elem,a,b):
    """Checks the validity of a point. Returns a boolean"""
    if elem in grid[a]:
        return False
    col = [grid[i][b] for i in range(9)]
    if elem in col:
        return False
    x = (a // 3)*3
    y = (b // 3)*3
    for i in range(x,x+3):
        for j in range(y,y+3):
            if grid[i][j] == elem:
                return False
    return True
def sudokuSolver(grid):
    """This is the function that solves the sudoku. Prints the state the state of grid whether solved or not."""
    x,y = findEmptyCell(grid)
    if x is None:
        return True
    for i in range(1,10):
        if isAValideCell(grid,i,x,y):
            grid[x][y] = i
            if sudokuSolver(grid):
                return True
        grid[x][y] = 0
    return False
class SudokuSolver:
    def __init__(self,grid):
        self.grid = grid
    def solve(self):
        sudokuSolver(self.grid)
    def afterSolving(self):
        printBoard(self.grid)
        
